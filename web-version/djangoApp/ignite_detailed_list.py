import urllib.request
import urllib.parse
import json

def fetch_redcap_staff_report():
    """
    Fetches REDCap data and computes counts per staff for various screening and visit categories.
    
    Returns:
        dict: Contains categorized staff counts and summary statistics.
    """
    # REDCap API payload
    datacall = {
        'token': '6DDC2EADDD7968A4DAD1730FBB52AD63',
        'content': 'record',
        'action': 'export',
        'format': 'json',
        'type': 'flat',
        'csvDelimiter': '',
        'fields[0]': 'record_id',
        'fields[1]': 'to_staff',
        'fields[2]': 'ip_staff',
        'fields[3]': 'es_ra',
        'fields[4]': 'tz_staff_2',
        'fields[5]': 'tz_staff',
        'fields[6]': 'es_by',
        'fields[7]': 'vol_excl',
        'fields[8]': 'es_by_v2',
        'fields[9]': 'screen_icf_oc',
        'fields[10]': 'eligibility_screener_complete',
        'fields[11]': 'eligibility_rescreen_complete',
        'fields[12]': 'es_oc_elig',
        'fields[13]': 'es_oc_maybe',
        'fields[14]': 'to_elig_oc',
        'events[0]': 'enroll_arm_1',
        'rawOrLabel': 'raw',
        'rawOrLabelHeaders': 'raw',
        'exportCheckboxLabel': 'false',
        'exportSurveyFields': 'false',
        'exportDataAccessGroups': 'false',
        'returnFormat': 'json'
    }

    # Make the API request
    data = urllib.parse.urlencode(datacall).encode('utf-8')
    req = urllib.request.Request('https://www.redcap.ihrp.uic.edu/api/', data)
    resp = urllib.request.urlopen(req)
    response_json = json.loads(resp.read())

    # Staff ID → Name mapping
    staff_names = {
        '1': "Amruta B", '2': "Leslie S", '3': "Claudia G", '4': "Shannon G",
        '5': "Nancy W", '6': "Corina R", '7': "Nan L", '8': "Jenny J",
        '9': "Gbenga A", '10': "Abby M", '11': "Richa S", '12': "Rahul V"
    }

    # Categories and REDCap fields
    categories = {
        'Teleorientation': 'to_staff',
        'In-person Visit': 'ip_staff',
        'Eligibility screener Completed': 'es_ra',
        'In-person tech staff': 'tz_staff_2',
        'Tech zoom setup staff': 'tz_staff',
        'IES eligible': 'es_ra'
    }

    results = {cat: {sid: 0 for sid in staff_names} for cat in categories}

    # Summary counters
    self_screener_complete = 0
    total_screened_count = 0
    ies_eligible_count = 0
    ies_eligible_total = 0

    for record in response_json:
        for category, field in categories.items():
            staff_id = record.get(field)

            if not staff_id or staff_id not in staff_names:
                continue

            if category == 'Teleorientation':
                if record.get('to_elig_oc', '0') > '0':
                    results[category][staff_id] += 1

            elif category == 'In-person Visit':
                if record.get('to_elig_oc', '0') == '1':
                    results[category][staff_id] += 1

            elif category == 'Eligibility screener Completed':
                if record.get('screen_icf_oc', '0') == '1':
                    results[category][staff_id] += 1

            elif category == 'IES eligible':
                if record.get('es_oc_elig') == '1' or record.get('es_oc_maybe') == '1':
                    results[category][staff_id] += 1

            elif category in ['In-person tech staff', 'Tech zoom setup staff']:
                results[category][staff_id] += 1

        # Self-screener complete
        if record.get('es_by') == '1' and record.get('screen_icf_oc') == '1':
            self_screener_complete += 1

        # Total screened and IES eligibility
        if record.get('eligibility_screener_complete', '0') == '2' or record.get('eligibility_rescreen_complete', '0') == '2':
            if record.get('screen_icf_oc', '0') == '1':
                total_screened_count += 1
                if record.get('es_by') == '1' and (record.get('es_oc_elig') == '1' or record.get('es_oc_maybe') == '1'):
                    ies_eligible_count += 1
                if record.get('es_oc_elig') == '1' or record.get('es_oc_maybe') == '1':
                    ies_eligible_total += 1

    # Format output
    formatted_results = {
        category: {
            staff_names[sid]: count for sid, count in counts.items()
        } for category, counts in results.items()
    }

    # Add summary stats
    formatted_results['Summary'] = {
        'Total Screened': total_screened_count,
        'Self Screener Completed': self_screener_complete,
        'IES Eligible (Self)': ies_eligible_count,
        'IES Eligible (All)': ies_eligible_total
    }

    return formatted_results
