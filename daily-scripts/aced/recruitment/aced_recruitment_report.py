import requests
import urllib.request, urllib.parse
import json

# import pandas as pd
from datetime import datetime, timedelta

def fetch_aced_recruitment_data():

    datacall = {
        # 'token': '5D8E1721D73344CAA8B62EDE0ADE8ED9',
        'token': '47F4F8FA1815CC6DEF2C77FAE213ABB3',
        'content': 'record',
        'action': 'export',
        'format': 'json',
        'type': 'flat',
        'csvDelimiter': '',
        'fields[0]': 'record_id',
        # 'records[0]': '165',
        # 'records[1]': '274',
        # 'records[2]': '297',
        # 'records[3]': '311',
        # 'records[4]': '1',
        # 'records[5]': '610',
        'fields[1]': 'aced_site',
        # 'fields[2]': 'date_invite_1',
        'fields[3]': 'fraud_flag',
        'fields[4]': 'dupe_rec',
        'fields[5]': 'es_inelig_score',
        'fields[6]': 'es_inelig_score_v2',
        'fields[7]': 'invite_yn',
        'fields[8]': 'vol_excl',
        'fields[9]': 'screen_icf_oc',
        'fields[10]': 'es_elig_score',
        'fields[11]': 'es_oc_inelig',
        'fields[12]': 'es_oc_elig',
        'fields[13]': 'eligibility_screener_complete',
        'fields[14]': 'es_oc_inelig_v2',
        'fields[15]': 'to_appt_status',
        'fields[16]': 'es_oc_elig_v2',
        'fields[17]': 'es_elig_score_v2',
        'fields[18]': 'ehr_match',
        'fields[19]': 'wn_status_1',
        'fields[20]': 'es_date',
        'fields[21]': 'to_elig_oc',
        'fields[22]': 'to_icf_oc',
        'fields[23]': 'agree_biaffect',
        'fields[24]': 'agree_nda',
        'fields[25]': 'wn_status_2',
        'fields[26]': 'day1',
        'fields[27]': 'webneuro_schedule_complete',
        'fields[28]': 'd392',
        'fields[29]': 'dropout_type',
        'fields[30]': 'd7',
        'fields[31]': 'd15',
        'fields[32]': 'd28',
        'fields[33]': 'd57',
        'fields[34]': 'd84',
        'fields[35]': 'd183',
        'fields[36]': 'd210',
        'fields[37]': 'd274',
        'fields[38]': 'd301',
        'fields[39]': 'd365',
        'fields[40]': 'dropout_timepoint',
        'fields[41]': 'wn_status_3',
        'fields[42]': 't1_oc',
        'fields[43]': 't2_oc',
        'fields[44]': 't3_oc',
        'fields[45]': 't4_oc',
        'fields[46]': 't5_oc',
        'fields[47]': 't6_oc',
        'events[0]': 'enroll_arm_1',
        'rawOrLabel': 'raw',
        'rawOrLabelHeaders': 'raw',
        'exportCheckboxLabel': 'false',
        'exportSurveyFields': 'false',
        'exportDataAccessGroups': 'false',
        'returnFormat': 'json'
    }

    data = urllib.parse.urlencode(datacall).encode('utf-8')
    req = urllib.request.Request('https://www.redcap.ihrp.uic.edu/api/', data)
    resp = urllib.request.urlopen(req)
    respdata = resp.read()
    jsondata = json.loads(respdata)
    response_json = jsondata

    print("Received Data")
    today = datetime.today().date()

    default_structure = {
        'ineligible_prior_to_screen_count': 0,
        'declined_to_screen_count': 0,
        'ineligible_count': 0,
        'eligible_but_declined_to_count': 0,
        'eligible_undecided_count': 0,
        'screened_eligible_count': 0,
        'ehr_mismatch_count': 0,
        'appt_declined_count': 0,
        'appt_needed_within_week_since_ies_count': 0,
        'appt_needed_over_week_since_ies_count': 0,
        'reschedule_no_show_count': 0,
        'to_schedule_count': 0,
        'to_attended_count': 0,
        'ineligible_at_to_count': 0,
        'declined_icf_count': 0,
        'to_declined_to_proceed_count': 0,
        'to_elig_undecided_count': 0,
        'to_elig_pending_md_clearance_count': 0,
        'consented_count': 0,
        'consented_biaffect_count': 0,
        'consented_nda_count': 0,
        'consesnted_and_eligible_count': 0,
        't1_baseline_prewindow_count': 0,
        't1_baseline_inwindow_count': 0,
        't1_baseline_complete_fully_enrolled_count': 0,
        't1_baseline_incomplete_webneuro_only_count': 0,
        't1_baseline_incomplete_pros_only_count': 0,
        't1_baseline_missing_count': 0,
        't2_baseline_prewindow_count': 0,
        't2_baseline_inwindow_count': 0,
        't2_baseline_complete_fully_enrolled_count': 0,
        't2_baseline_incomplete_webneuro_only_count': 0,
        't2_baseline_incomplete_pros_only_count': 0,
        't2_baseline_missing_count': 0,
        't2_baseline_total_entered_count': 0,
        't3_baseline_prewindow_count': 0,
        't3_baseline_inwindow_count': 0,
        't3_baseline_complete_fully_enrolled_count': 0,
        't3_baseline_incomplete_webneuro_only_count': 0,
        't3_baseline_incomplete_pros_only_count': 0,
        't3_baseline_total_entered_count': 0,
        't4_baseline_prewindow_count': 0,
        't4_baseline_inwindow_count': 0,
        't4_baseline_complete_fully_enrolled_count': 0,
        't4_baseline_missing_count': 0,
        't4_baseline_total_entered_count': 0,
        't5_baseline_prewindow_count': 0,
        't5_baseline_inwindow_count': 0,
        't5_baseline_complete_fully_enrolled_count': 0,
        't5_baseline_missing_count': 0,
        't5_baseline_total_entered_count': 0,
        't6_baseline_prewindow_count': 0,
        't6_baseline_inwindow_count': 0,
        't6_baseline_complete_fully_enrolled_count': 0,
        't6_baseline_missing_count': 0,
        't6_baseline_total_entered_count': 0,
        'off_study_count': 0,
        'withdraw_t1_count': 0,
        'withdraw_t2_count': 0,
        'withdraw_t3_count': 0,
        'withdraw_t4_count': 0,
        'withdraw_t5_count': 0,
        'withdraw_t6_count': 0,
        'invite_sent_count': 0,
        'two_week_wait_count': 0,
        'calling_in_progress_count': 0,
        'ceased_outreach_count': 0,
        'requested_call_count': 0,
        'partial_screen_count': 0,
    }

    milestones = [
        (48, "8/1/25"),
        (130, "12/1/25"),
        (232, "4/1/26"),
        (344, "8/1/26"),
        (466, "12/1/26"),
        (588, "4/1/27"),
        (710, "8/1/27"),
        (832, "12/1/27"),
        (954, "4/1/28"),
        (1078, "8/1/28"),
        (1200, "12/1/28"),
    ]

    for target, milestone_date in milestones:
        milestone_dt = datetime.strptime(milestone_date, "%m/%d/%y").date()
        if milestone_dt >= today:
            new_milestone = (target, milestone_dt)
            break

    target_value = new_milestone[0] 
    milestone_date = new_milestone[1].strftime('%m/%d/%y')

    # print("New Milestone set:", target_value, milestone_date)
    # Initialize the site dictionary with the same default structure for each site
    siteDict = {str(i): default_structure.copy() for i in range(1, 4)}

    sitesCollect = {
        '1': 0,
        '2': 0,
        '': 0
    }

    enroll_criteria_met = {}

    for i in response_json:

        # print(record)
        site = str(i['aced_site'])
        sitesCollect[site] += 1

        #-------NOt Screened---------
        if i['vol_excl'] == '1':
            siteDict[site]['ineligible_prior_to_screen_count'] += 1

        if i['redcap_event_name'] == 'enroll_arm_1' and  i['eligibility_screener_complete'] == '2' and (i['invite_yn'] == '2' or i['screen_icf_oc'] == '2'):
            siteDict[site]['declined_to_screen_count'] += 1

        #-------Screened---------
        if i['redcap_event_name'] == 'enroll_arm_1' and i['eligibility_screener_complete'] == '2' and i['fraud_flag'] != '2' and i['dupe_rec'] != '2' and i['record_id'] != '36':  # a little weird checking 36

            if i['es_inelig_score'] == '1' or i['es_inelig_score_v2'] == '1' and i['screen_icf_oc'] == '1':
                siteDict[site]['ineligible_count'] += 1

            if (i['es_elig_score'] == '1' or i['es_elig_score_v2'] == '1'):

                if (i['es_oc_elig'] == '2' or i['es_oc_elig_v2'] == '2'):
                    siteDict[site]['eligible_but_declined_to_count'] += 1

                if (i['es_oc_elig'] == '3' or i['es_oc_elig_v2'] == '3'):
                    siteDict[site]['eligible_undecided_count'] += 1

                if (i['es_oc_elig'] == '1' or i['es_oc_elig_v2'] == '1'):
                    siteDict[site]['screened_eligible_count'] += 1

        if (i['es_elig_score'] == '1' or i['es_elig_score_v2'] == '1') and i['es_oc_elig'] == '1' and  i['dupe_rec'] != '2' and i['fraud_flag'] != '2':
        
            if i['ehr_match'] == '2' and i['to_appt_status'] != '4':
                siteDict[site]['ehr_mismatch_count'] += 1

            #---TeleOrientation--------
            if i['to_appt_status'] == '4':
                siteDict[site]['appt_declined_count'] += 1  

        if 'es_date' in i and i['es_date'].strip():
            appt_date = datetime.strptime(i['es_date'], '%Y-%m-%d').date()
            if (today - appt_date).days < 8 and i['to_appt_status'] == '2':
                siteDict[site]['appt_needed_within_week_since_ies_count'] += 1

            if (today - appt_date).days >= 8 and i['to_appt_status'] =='2':
                siteDict[site]['appt_needed_over_week_since_ies_count'] += 1  

        if i['to_appt_status'] == '3':
            siteDict[site]['reschedule_no_show_count'] += 1

        if i['es_oc_elig'] == '1' and i['to_appt_status'] == '1' and (i['es_elig_score'] == '1' or i['es_elig_score_v2'] == '1') and i['dupe_rec'] != '2' and i['fraud_flag'] != '2':
            siteDict[site]['to_schedule_count'] += 1

        #------TO Attended----------
        if i['to_elig_oc'] is not None and i['to_appt_status'] != '4' and i['dupe_rec'] != '2' and i['fraud_flag'] != '2':
            siteDict[site]['to_attended_count'] += 1

        if i['to_appt_status'] != '4' and i['dupe_rec'] != '2' and i['fraud_flag'] != '2':
            if i['to_elig_oc'] == '2':
                siteDict[site]['ineligible_at_to_count'] += 1

            if ['to_elig_oc'] == '4':
                siteDict[site]['declined_icf_count'] += 1

            if i['to_elig_oc'] == '5':
                siteDict[site]['to_declined_to_proceed_count'] += 1

            if i['to_elig_oc'] == '6':
                siteDict[site]['to_elig_undecided_count'] += 1

            if i['to_elig_oc'] == '3':
                siteDict[site]['to_elig_pending_md_clearance_count'] += 1

        #Consented
        if i['to_icf_oc'] == '1':
            siteDict[site]['consented_count'] += 1

            if i['agree_biaffect'] == '1':
                siteDict[site]['consented_biaffect_count'] += 1
            
            if i['agree_nda'] == '1':
                siteDict[site]['consented_nda_count'] += 1

            if i['to_elig_oc'] == '1':
                siteDict[site]['consesnted_and_eligible_count'] += 1

        #------T1 Baseline-------
        if i['day1'].strip():
            # day1_date = datetime.strptime(i['day1'], '%Y-%m-%d').date()
            # d392_date = datetime.strptime(i['d392'], '%Y-%m-%d').date()

            enroll_criteria_met[i['record_id']] = {
                'record_id': i['record_id'],
                'aced_site': i.get('aced_site'),
                'to_elig_oc': i.get('to_elig_oc'),
                'webneuro_schedule_complete': i.get('webneuro_schedule_complete'),
                'd392': i.get('d392'),
                'to_icf_oc': i.get('to_icf_oc'),
                'day1': i.get('day1'),
                'dropout_type': i.get('dropout_type'),
                'd7': i.get('d7'),
                'd15': i.get('d15'),
                'd28': i.get('d28'),
                'd57': i.get('d57'),
                'd84': i.get('d84'),
                'd183': i.get('d183'),
                'd210': i.get('d210'),
                'd274': i.get('d274'),
                'd301': i.get('d301'),
                'd365': i.get('d365'),
                'dropout_timepoint': i.get('dropout_timepoint'),
                'wn_status_1': i.get('wn_status_1'),
                'wn_status_2': i.get('wn_status_2'),
                'wn_status_3': i.get('wn_status_3'),
                't1_oc': i.get('t1_oc'),
                't2_oc': i.get('t2_oc'),
                't3_oc': i.get('t3_oc'),
                't4_oc': i.get('t4_oc'),
                't5_oc': i.get('t5_oc'),
                't6_oc': i.get('t6_oc')
            }



    #-------- Data call for T-1 timepoint-------
    datacall1 = {
        # 'token': '5D8E1721D73344CAA8B62EDE0ADE8ED9',
        'token': '47F4F8FA1815CC6DEF2C77FAE213ABB3',
        'content': 'record',
        'action': 'export',
        'format': 'json',
        'type': 'flat',
        'csvDelimiter': '',
        'fields[0]': 'record_id',
        # 'records[0]': '274',
        'fields[1]': 'treatment_survey_baseline_complete',
        'fields[2]': 'webneuro_data_complete',
        'fields[3]': 'aced2_assessment_survey_complete',
        'fields[4]': 'treatment_survey_follow_up_complete',
        'fields[5]': 'treatment_survey_baseline_complete',
        # 'fields[6]': 'wn_status_1',
        'fields[7]': 't2_oc',
        # 'fields[8]': 'wn_status_2',
        'fields[9]': 't3_oc',
        # 'fields[10]': 'wn_status_3',
        # 'fields[11]': 't4_oc',
        # 'fields[12]': 't5_oc',
        # 'fields[13]': 't6_oc',
        'events[0]': 't1_arm_1',
        'events[1]': 't2_arm_1',
        'events[2]': 't3_arm_1',
        'events[3]': 't4_arm_1',
        'events[4]': 't5_arm_1',
        'events[5]': 't6_arm_1',
        # 'events[6]': 'enroll_arm_1',
        'rawOrLabel': 'raw',
        'rawOrLabelHeaders': 'raw',
        'exportCheckboxLabel': 'false',
        'exportSurveyFields': 'false',
        'exportDataAccessGroups': 'false',
        'returnFormat': 'json'
    }

    data1 = urllib.parse.urlencode(datacall1).encode('utf-8')
    req1 = urllib.request.Request('https://www.redcap.ihrp.uic.edu/api/', data1)
    resp1 = urllib.request.urlopen(req1)
    respdata1 = resp1.read()
    jsondata1 = json.loads(respdata1)
    response_json1 = jsondata1

    print("Received Data1")

    # print(enroll_criteria_met)
    #----------Calculate Baseline Data------------
    for record in response_json1:

        if record['record_id'] in enroll_criteria_met:
            site = enroll_criteria_met[record['record_id']]['aced_site']
            to_elig_oc = enroll_criteria_met[record['record_id']]['to_elig_oc']
            # print(f"Processing record {record['record_id']} for elig_oc {to_elig_oc} ")
            webneuro_schedule_complete = enroll_criteria_met[record['record_id']]['webneuro_schedule_complete']
            dropout_timepoint = enroll_criteria_met[record['record_id']]['dropout_timepoint']
            wn_status_1 = enroll_criteria_met[record['record_id']]['wn_status_1']
            wn_status_2 = enroll_criteria_met[record['record_id']]['wn_status_2']
            wn_status_3 = enroll_criteria_met[record['record_id']]['wn_status_3']

            t1_oc = enroll_criteria_met[record['record_id']]['t1_oc']
            t2_oc = enroll_criteria_met[record['record_id']]['t2_oc']
            t3_oc = enroll_criteria_met[record['record_id']]['t3_oc']
            t4_oc = enroll_criteria_met[record['record_id']]['t4_oc']
            t5_oc = enroll_criteria_met[record['record_id']]['t5_oc']
            t6_oc = enroll_criteria_met[record['record_id']]['t6_oc']

            d392_date = enroll_criteria_met[record['record_id']]['d392']
            if d392_date:
                d392_date = datetime.strptime(d392_date, "%Y-%m-%d").date()

            day1_date = enroll_criteria_met[record['record_id']]['day1']
            if day1_date:
                day1_date = datetime.strptime(day1_date, "%Y-%m-%d").date()

            to_icf_oc = enroll_criteria_met[record['record_id']]['to_icf_oc']
            dropout_type = enroll_criteria_met[record['record_id']]['dropout_type']

            d7_date = enroll_criteria_met[record['record_id']]['d7']
            if d7_date:
                d7_date = datetime.strptime(d7_date, "%Y-%m-%d").date()

            d15_date = enroll_criteria_met[record['record_id']]['d15']
            if d15_date:
                d15_date = datetime.strptime(d15_date, "%Y-%m-%d").date()

            d28 = enroll_criteria_met[record['record_id']]['d28']
            if d28:
                d28 = datetime.strptime(d28, "%Y-%m-%d").date()

            d57 = enroll_criteria_met[record['record_id']]['d57']
            if d57:
                d57 = datetime.strptime(d57, "%Y-%m-%d").date()

            d84 = enroll_criteria_met[record['record_id']]['d84']
            if d84:
                d84 = datetime.strptime(d84, "%Y-%m-%d").date()

            d183 = enroll_criteria_met[record['record_id']]['d183']
            if d183:
                d183 = datetime.strptime(d183, "%Y-%m-%d").date()

            d210 = enroll_criteria_met[record['record_id']]['d210']
            if d210:
                d210 = datetime.strptime(d210, "%Y-%m-%d").date()

            d274 = enroll_criteria_met[record['record_id']]['d274']
            if d274:
                d274 = datetime.strptime(d274, "%Y-%m-%d").date()

            d301 = enroll_criteria_met[record['record_id']]['d301']
            if d301:
                d301 = datetime.strptime(d301, "%Y-%m-%d").date()

            d365 = enroll_criteria_met[record['record_id']]['d365']
            if d365:
                d365 = datetime.strptime(d365, "%Y-%m-%d").date()
        
            #-------Final Disposition---------
            if dropout_type == '' and (today > d392_date):
                siteDict[site]['off_study_count'] += 1
        
            if dropout_type > '0' and dropout_timepoint == '1':
                siteDict[site]['withdraw_t1_count'] += 1
                
            if dropout_type > '0' and dropout_timepoint == '2':
                siteDict[site]['withdraw_t2_count'] += 1
        
            if dropout_type > '0' and dropout_timepoint == '3':
                siteDict[site]['withdraw_t3_count'] += 1
            
            if dropout_type > '0' and dropout_timepoint == '4':
                siteDict[site]['withdraw_t4_count'] += 1
        
            if dropout_type > '0' and dropout_timepoint == '5':
                siteDict[site]['withdraw_t5_count'] += 1
        
            if dropout_type > '0' and dropout_timepoint == '6':
                siteDict[site]['withdraw_t6_count'] += 1

        #----------Calculate T1 Baseline Data------------
        # Check if 'enroll_arm_1' criteria were met for this record_id
        if record['record_id'] in enroll_criteria_met and record['redcap_event_name'] == 't1_arm_1':
            
            if to_elig_oc == '1' and webneuro_schedule_complete == '2' and to_icf_oc == '1' and dropout_type == '':
                if (day1_date > today) and record.get('treatment_survey_baseline_complete') == '2':
                    siteDict[site]['t1_baseline_prewindow_count'] += 1

            if to_icf_oc == '1': # and dropout_type == '':
                # if (day1_date - today).days <= 0 and (d7_date - today).days >= 0 and (record['webneuro_data_complete'] == '0' or record['aced2_assessment_survey_complete'] == '0' or record['treatment_survey_follow_up_complete'] == '0'):
                # print(f"Processing record {record['record_id']} webneuro_schedule_complete: {webneuro_schedule_complete}, aced2_assessment_survey_complete: {record['aced2_assessment_survey_complete']}, treatment_survey_follow_up_complete: {record['treatment_survey_follow_up_complete']}")
                if day1_date <= today <= d7_date and (record['webneuro_data_complete'] == '0' or record['aced2_assessment_survey_complete'] == '0' or record['treatment_survey_baseline_complete'] == '0'):
                    # print(f"Processing record {record['record_id']}")
                    siteDict[site]['t1_baseline_inwindow_count'] += 1

                if record['webneuro_data_complete'] == '2' and record['aced2_assessment_survey_complete'] == '2' and record['treatment_survey_follow_up_complete'] == '2':
                    siteDict[site]['t1_baseline_complete_fully_enrolled_count'] += 1

                if (d7_date < today) and t1_oc == '2' and wn_status_1 == '3':
                    siteDict[site]['t1_baseline_incomplete_webneuro_only_count'] += 1

                if (d7_date < today) and t1_oc == '2' and wn_status_1 != '3':
                    siteDict[site]['t1_baseline_incomplete_pros_only_count'] += 1

                if (d7_date < today) and t1_oc == '3':
                    siteDict[site]['t1_baseline_missing_count'] += 1


        #---------T2 Baseline Data----------
        if record['record_id'] in enroll_criteria_met and record['redcap_event_name'] == 't2_arm_1':

            if to_icf_oc == '1' and dropout_type == '':
                if to_elig_oc == '1' and d7_date < today < d15_date:
                    siteDict[site]['t2_baseline_prewindow_count'] += 1

                if (d15_date <= today <= d28) and (record['webneuro_data_complete'] == '0' or record['aced2_assessment_survey_complete'] == '0' or record['treatment_survey_follow_up_complete'] == '0'):
                    siteDict[site]['t2_baseline_inwindow_count'] += 1

                if record['webneuro_data_complete'] == '2' and record['aced2_assessment_survey_complete'] == '2' and record['treatment_survey_follow_up_complete'] == '2':
                    siteDict[site]['t2_baseline_complete_fully_enrolled_count'] += 1

                if (d28 < today) and t2_oc == '2' and wn_status_2 == '3':
                    siteDict[site]['t2_baseline_incomplete_webneuro_only_count'] += 1

                if (d28 < today) and t2_oc == '2' and wn_status_2 != '3':
                    siteDict[site]['t2_baseline_incomplete_pros_only_count'] += 1

                if (d28 < today) and t2_oc == '3':
                    siteDict[site]['t2_baseline_missing_count'] += 1
                
                if (d28 < today) and t2_oc == '1':
                    siteDict[site]['t2_baseline_total_entered_count'] += 1


        #---------T3 Baseline Data----------
        if record['record_id'] in enroll_criteria_met and record['redcap_event_name'] == 't3_arm_1':

            if to_icf_oc == '1' and dropout_type == '':
                if to_elig_oc == '1' and d28 < today < d57:
                    siteDict[site]['t3_baseline_prewindow_count'] += 1

                if (d57 <= today <= d84) and (record['webneuro_data_complete'] == '0' or record['aced2_assessment_survey_complete'] == '0' or record['treatment_survey_follow_up_complete'] == '0'):
                    siteDict[site]['t3_baseline_inwindow_count'] += 1

                if record['webneuro_data_complete'] == '2' and record['aced2_assessment_survey_complete'] == '2' and record['treatment_survey_follow_up_complete'] == '2':
                    siteDict[site]['t3_baseline_complete_fully_enrolled_count'] += 1

                if (d84 < today) and t3_oc == '2' and wn_status_3 == '3':
                    siteDict[site]['t3_baseline_incomplete_webneuro_only_count'] += 1

                if (d84 < today) and t3_oc == '2' and wn_status_3 != '3':
                    siteDict[site]['t3_baseline_incomplete_pros_only_count'] += 1

                if (d84 < today) and t3_oc == '3':
                    siteDict[site]['t3_baseline_missing_count'] += 1

                if (d84 < today) and t3_oc == '1':
                    siteDict[site]['t3_baseline_total_entered_count'] += 1

        #---------T4 Baseline Data----------
        if record['record_id'] in enroll_criteria_met and record['redcap_event_name'] == 't4_arm_1':

            if to_icf_oc == '1' and dropout_type == '' :
                if to_elig_oc == '1' and d84 < today < d183:    
                    siteDict[site]['t4_baseline_prewindow_count'] += 1

                if d183 <= today <= d210 and (record['webneuro_data_complete'] == '0' or record['aced2_assessment_survey_complete'] == '0' or record['treatment_survey_follow_up_complete'] == '0'):
                    siteDict[site]['t4_baseline_inwindow_count'] += 1

                if record['webneuro_data_complete'] == '2' and record['aced2_assessment_survey_complete'] == '2' and record['treatment_survey_follow_up_complete'] == '2':
                    siteDict[site]['t4_baseline_complete_fully_enrolled_count'] += 1

                if (d210 < today) and t4_oc == '3':
                    siteDict[site]['t4_baseline_missing_count'] += 1

                if (d210 < today) and t4_oc == '1':
                    siteDict[site]['t4_baseline_total_entered_count'] += 1

        #---------T5 Baseline Data----------
        if record['record_id'] in enroll_criteria_met and record['redcap_event_name'] == 't5_arm_1':

            if to_icf_oc == '1' and dropout_type == '':
                if to_elig_oc == '1' and (d210 < today < d274):
                    siteDict[site]['t5_baseline_prewindow_count'] += 1
            
                if d274 <= today <= d301 and (record['webneuro_data_complete'] == '0' or record['aced2_assessment_survey_complete'] == '0' or record['treatment_survey_follow_up_complete'] == '0'):
                    siteDict[site]['t5_baseline_inwindow_count'] += 1

                if record['webneuro_data_complete'] == '2' and record['aced2_assessment_survey_complete'] == '2' and record['treatment_survey_follow_up_complete'] == '2':
                    siteDict[site]['t5_baseline_complete_fully_enrolled_count'] += 1

                if (d301 < today) and t5_oc == '3':
                    siteDict[site]['t5_baseline_missing_count'] += 1

                if (d301 < today) and t5_oc == '3':
                    siteDict[site]['t5_baseline_total_entered_count'] += 1

        #---------T6 Baseline Data----------
        if record['record_id'] in enroll_criteria_met and record['redcap_event_name'] == 't6_arm_1':

            if to_icf_oc == '1' and dropout_type == '':
                if to_elig_oc == '1' and (d301 < today < d365):
                    siteDict[site]['t6_baseline_prewindow_count'] += 1
            
                if (d365 <= today <= d392_date) and (record['webneuro_data_complete'] == '0' or record['aced2_assessment_survey_complete'] == '0' or record['treatment_survey_follow_up_complete'] == '0'):
                    siteDict[site]['t6_baseline_inwindow_count'] += 1

                if record['webneuro_data_complete'] == '2' and record['aced2_assessment_survey_complete'] == '2' and record['treatment_survey_follow_up_complete'] == '2':
                    siteDict[site]['t6_baseline_complete_fully_enrolled_count'] += 1

                if (d392_date < today) and t6_oc == '3':
                    siteDict[site]['t6_baseline_missing_count'] += 1

                if (d392_date < today) and t6_oc == '1':
                    siteDict[site]['t6_baseline_total_entered_count'] += 1

            


    #----------Call 3 for REcruitment Data UIC---------
    datacall2 = {
        # 'token': '5D8E1721D73344CAA8B62EDE0ADE8ED9',
        'token': 'ED46C5516CF3E6AB78B089502DBAD799',
        'content': 'record',
        'action': 'export',
        'format': 'json',
        'type': 'flat',
        'csvDelimiter': '',
        'fields[0]': 'record_id',
        'fields[1]': 'date_invite_1',
        'fields[2]': 'can_call',
        'fields[3]': 'eligibility_screener_complete',
        'fields[4]': 'vol_excl',
        'fields[5]': 'invite_yn',
        'fields[6]': 'screen_icf_oc',
        'fields[7]': 'cease',
        'fields[8]': 'twilio_oc',
        'fields[9]': 'aced_site',
        'events[0]': 'enroll_arm_1',
        'events[1]': 't2_arm_1',
        'rawOrLabel': 'raw',
        'rawOrLabelHeaders': 'raw',
        'exportCheckboxLabel': 'false',
        'exportSurveyFields': 'false',
        'exportDataAccessGroups': 'false',
        'returnFormat': 'json'
    }

    data2 = urllib.parse.urlencode(datacall2).encode('utf-8')
    req2 = urllib.request.Request('https://www.redcap.ihrp.uic.edu/api/', data2)
    resp2 = urllib.request.urlopen(req2)
    respdata2 = resp2.read()
    jsondata2 = json.loads(respdata2)
    response_json2 = jsondata2

    print("Received Data2")
    valid_var = ' '
    for record in response_json2:

        # print(record)
        site = str(i['aced_site'])
        
        if 'date_invite_1' in record and record['date_invite_1'].strip():
            # Convert the string date to a date object
            invite_date = datetime.strptime(record['date_invite_1'], '%Y-%m-%d').date()

            # ------------------invitation sent---------------
            # Check if the invite_date is less than or equal to today's date
            if invite_date <= today:
                siteDict[site]['invite_sent_count'] += 1

            if 'can_call' in record and record['can_call'].strip():
                can_call_date = datetime.strptime(record['can_call'], '%Y-%m-%d').date()

                    # call_date > today means its status is wait 
                if can_call_date > today and record['eligibility_screener_complete'] != '2':
                    siteDict[site]['two_week_wait_count'] += 1

                # --------------calling in progress----------------
                # if record['redcap_event_name'] != ' ':
                if record['redcap_event_name'] != ' ':
                    if record['vol_excl'] == '1' or record['invite_yn'] == '2' or ( record['screen_icf_oc'] != '3' and record['eligibility_screener_complete'] == '2'):
                        recruit_oc_know_var = '1'
                    else:
                        recruit_oc_know_var = '0'

                else:
                    valid_var = ' '
                    
                if can_call_date <= today and recruit_oc_know_var != '1' and record['cease'] < '1' and valid_var != '':
                    siteDict[site]['calling_in_progress_count'] += 1


                #-----------ceased Outreach Count---------------
                if record['cease'] >= '1' and recruit_oc_know_var != '1':
                    siteDict[site]['ceased_outreach_count'] += 1


        #------------requested Call count-------------
        if record['eligibility_screener_complete'] == '0'and (record['twilio_oc'] == '1' or record['screen_icf_oc'] == '3'):
            siteDict[site]['requested_call_count'] += 1

        #---------partial screen count--------  
        if record['screen_icf_oc'] == '1' and record['eligibility_screener_complete'] == '0':
            siteDict[site]['partial_screen_count'] += 1


    #----------Call 4 for Standford Honest broker---------
    datacall3 = {
        # 'token': '5D8E1721D73344CAA8B62EDE0ADE8ED9',
        'token': '81C1C88F4E9C8FD1B572ADB54276017C',
        'content': 'record',
        'action': 'export',
        'format': 'json',
        'type': 'flat',
        'csvDelimiter': '',
        'fields[0]': 'record_id',
        'fields[2]': 'es_date',
        'fields[3]': 'eligibility_screener_complete',
        'fields[4]': 'screen_icf_oc',
        'fields[7]': 'cease',
        'events[0]': 'enroll_arm_1',
        'rawOrLabel': 'raw',
        'rawOrLabelHeaders': 'raw',
        'exportCheckboxLabel': 'false',
        'exportSurveyFields': 'false',
        'exportDataAccessGroups': 'false',
        'returnFormat': 'json'
    }

    data3 = urllib.parse.urlencode(datacall3).encode('utf-8')
    req3 = urllib.request.Request('https://www.redcap.ihrp.uic.edu/api/', data3)
    resp3 = urllib.request.urlopen(req3)
    respdata3 = resp3.read()
    jsondata3 = json.loads(respdata3)
    response_json3 = jsondata3

    honest_broker_ceased_outreach_count = 0
    honest_broker_partial_screen = 0 

    print("Received Data3")
    for i in response_json3:
        if i['cease'] >= '1':
            honest_broker_ceased_outreach_count += 1
        
        if i['eligibility_screener_complete'] != '' and i['screen_icf_oc'] == '1' and i['es_date'] != '':
            honest_broker_partial_screen += 1

    #----------Call 5 for Standford Public---------
    datacall4 = {
        # 'token': '5D8E1721D73344CAA8B62EDE0ADE8ED9',
        'token': 'B660F9B9F70142502AC1C998C733996F',
        'content': 'record',
        'action': 'export',
        'format': 'json',
        'type': 'flat',
        'csvDelimiter': '',
        'fields[0]': 'record_id',
        'fields[2]': 'es_date',
        'fields[3]': 'eligibility_screener_complete',
        'fields[4]': 'screen_icf_oc',
        'fields[7]': 'cease',
        'events[0]': 'enroll_arm_1',
        'rawOrLabel': 'raw',
        'rawOrLabelHeaders': 'raw',
        'exportCheckboxLabel': 'false',
        'exportSurveyFields': 'false',
        'exportDataAccessGroups': 'false',
        'returnFormat': 'json'
    }

    data4 = urllib.parse.urlencode(datacall4).encode('utf-8')
    req4 = urllib.request.Request('https://www.redcap.ihrp.uic.edu/api/', data4)
    resp4 = urllib.request.urlopen(req4)
    respdata4 = resp4.read()
    jsondata4 = json.loads(respdata4)
    response_json4 = jsondata4

    stanford_public_ceased_outreach_count = 0
    stanford_public_partial_screen = 0 

    print("Received Data3")
    for i in response_json4:
        if i['cease'] >= '1':
            stanford_public_ceased_outreach_count += 1
        
        if i['eligibility_screener_complete'] != '' and i['screen_icf_oc'] == '1' and i['es_date'] != '':
            stanford_public_partial_screen += 1

    fetchedData = {
        "siteDict": siteDict,
        "milestone_date": milestone_date,
        "target_value": target_value,
        "stanford_summary_data": {
            "honest_broker_ceased_outreach_count": honest_broker_ceased_outreach_count,
            "honest_broker_partial_screen": honest_broker_partial_screen,
            "stanford_public_ceased_outreach_count": stanford_public_ceased_outreach_count,
            "stanford_public_partial_screen": stanford_public_partial_screen
        }
    }

    return fetchedData
    