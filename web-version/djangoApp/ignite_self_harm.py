import urllib.request
import urllib.parse
import json
from datetime import datetime

def process_self_harm_data():
    REDCAP_API_URL = 'https://www.redcap.ihrp.uic.edu/api/'
    API_TOKEN = '752892A3A8C0CD86CF2480B203EE1EC0'

    data = {
        'token': API_TOKEN,
        'content': 'record',
        'format': 'json',
        'type': 'flat',
        'rawOrLabel': 'label',
        'rawOrLabelHeaders': 'label',
        'exportCheckboxLabel': 'false',
        'exportSurveyFields': 'false',
        'exportDataAccessGroups': 'false',
        'returnFormat': 'json'
    }

    encoded_data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(REDCAP_API_URL, encoded_data)
    resp = urllib.request.urlopen(req)
    jsondata = json.loads(resp.read())

    self_harm = jsondata
    today = datetime.today()

    def try_parse_date(dt_str):
        if not dt_str:
            return None
        for fmt in ('%Y-%m-%d %H:%M:%S.%f', '%Y-%m-%d %H:%M', '%Y-%m-%d %H:%S'):
            try:
                return datetime.strptime(dt_str, fmt)
            except:
                continue
        return None

    def init_metrics():
        return {
            'within_closed_reached': 0,
            'within_closed_not_reached': 0,
            'outside_closed_reached': 0,
            'outside_closed_not_reached': 0,
            'open_active': 0,
            'open_delayed': 0,
            'call911_yes': 0,
            'call911_no': 0
        }

    metrics = {
        'crc': init_metrics(),
        'intervention': init_metrics(),
        'system': init_metrics(),
        'system_lumen': init_metrics()
    }

    for i in self_harm:
        if i.get('dr_duplicate') == 'Yes':
            continue

        is_closed = i.get('ignite_psychiatrist_response_complete') == 'Complete'
        contacted = i.get('dr_part_contacted') == 'Yes'
        solved_time = try_parse_date(i.get('dr_date_time')) or today

        def process_entry(key, detection_field):
            detection_time = try_parse_date(i.get(detection_field))
            if not detection_time:
                return
            m = metrics[key]
            if i.get('dr_call911') == 'Yes':
                m['call911_yes'] += 1
            if i.get('dr_call911') == 'No':
                m['call911_no'] += 1
            if is_closed:
                days = (solved_time - detection_time).days
                if days <= 4:
                    m['within_closed_reached' if contacted else 'within_closed_not_reached'] += 1
                else:
                    m['outside_closed_reached' if contacted else 'outside_closed_not_reached'] += 1
            else:
                days = (today - detection_time).days
                m['open_active' if days <= 4 else 'open_delayed'] += 1

        if i.get('staff_detected_crc_complete') == 'Complete':
            process_entry('crc', 'crc_time_detection')

        if i.get('staff_detected_intervention_complete') == 'Complete':
            process_entry('intervention', 'crc_time_detection_v2')

        if i.get('system_self_harm_complete') == 'Complete' and not i.get('system_study_id_v2'):
            process_entry('system', 'system_time_detection')

        if i.get('system_study_id_v2') and i.get('staff_detected_intervention_complete') != 'Complete':
            process_entry('system_lumen', 'system_time_detection_v2')

    def sum_fields(field):
        return sum(metrics[key][field] for key in metrics)

    result = {
        "run_date": today.strftime('%B %d, %Y'),
        "study_md_reached_patient": sum_fields('within_closed_reached'),
        "unable_to_reach_patient_closed": sum_fields('within_closed_not_reached'),
        "study_md_reached_patient_directly_closed": sum_fields('outside_closed_reached'),
        "study_md_unable_to_reach_patient_closed": sum_fields('outside_closed_not_reached'),
        "active_case_open_within_4_day_window": sum_fields('open_active'),
        "delayed_response_open_after_4_days": sum_fields('open_delayed'),
        "open_alerts_patient_not_yet_reached": sum_fields('open_active') + sum_fields('open_delayed'),
        "closed_within_4_day_window": sum_fields('within_closed_reached') + sum_fields('within_closed_not_reached'),
        "closed_outside_4_day_window": sum_fields('outside_closed_reached') + sum_fields('outside_closed_not_reached'),
        "closed_alerts": (
            sum_fields('within_closed_reached') + sum_fields('within_closed_not_reached') +
            sum_fields('outside_closed_reached') + sum_fields('outside_closed_not_reached')
        ),
        "self_harm_alerts_to_date": (
            sum_fields('within_closed_reached') + sum_fields('within_closed_not_reached') +
            sum_fields('outside_closed_reached') + sum_fields('outside_closed_not_reached') +
            sum_fields('open_active') + sum_fields('open_delayed')
        ),
        "high_severe_risk_alerts_Yes": sum_fields('call911_yes'),
        "high_severe_risk_alerts_No": sum_fields('call911_no')
    }

    return result
