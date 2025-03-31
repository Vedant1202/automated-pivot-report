import requests
import urllib.request, urllib.parse
import json
# import pandas as pd
from datetime import datetime
from pymongo import MongoClient
import pytz


def process_redcap_data_for_ignite():
    datacall = {
        # 'token': '96EF07A3F74AE278A39C4F7C353937C2',
        'token': '6DDC2EADDD7968A4DAD1730FBB52AD63',
        'content': 'record',
        'action': 'export',
        'format': 'json',
        'type': 'flat',
        'csvDelimiter': '',
        # 'records[0]': '11232',
        # 'records[1]': '10',
        # 'records[2]': '1',
        # 'records[3]': '756',
        # 'records[4]': '510',
        # 'records[5]': '610',
        # 'records[6]': '710',
        # 'records[7]': '810',
        # 'records[8]': '910',
        # 'records[9]': '1010',
        # 'records[10]': '1110',
        'fields[0]': 'record_id',
        'fields[1]': 'cease',
        'fields[2]': 'date_invite_1',
        'fields[3]': 'can_call',
        'fields[4]': 'twilio_oc',
        'fields[5]': 'participant_log_complete',
        'fields[6]': 'invite_yn',
        'fields[7]': 'decline_invite',
        'fields[8]': 'vol_excl',
        'fields[9]': 'screen_icf_oc',
        'fields[10]': 'es_date',
        'fields[11]': 'es_oc_inelig',
        'fields[12]': 'es_oc_maybe',
        'fields[13]': 'eligibility_screener_complete',
        'fields[14]': 'es_oc_inelig_v2',
        'fields[15]': 'to_appt_status',
        'fields[16]': 'if_ies_maybe_2',
        'fields[17]': 'to_elig_oc',
        'fields[18]': 'par_oc',
        'fields[19]': 'eligibility_rescreen_complete',
        'fields[19]': 'ignite_assessment_survey_complete',
        # 'fields[20]': 'dist_status',
        'fields[21]': 'zoom_appt_status_2',
        'fields[22]': 'tech_oc',
        'fields[23]': 'blind_r1_date',
        'fields[24]': 'v1_d8_elig_oc_v2',
        'fields[25]': 'v1_d15_elig_oc_v2',
        'fields[26]': 'es_oc_elig',
        'fields[27]': 'es_oc_maybe_v2',
        'fields[28]': 'ip_outcome',
        'fields[29]': 'randomization_complete',
        'fields[30]': 'devicesetup_complete',
        'fields[31]': 'receipt_date',
        'fields[32]': 'ip_date',
        'fields[33]': 'es_oc_elig_v2',
        'fields[34]': 'ip_appt_status',
        'events[0]': 'enroll_arm_1',
        'events[1]': 'baseline_arm_1',
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

    # print("Received Data")

    invite_sent_count= 0
    wait_count= 0
    two_week_wait_count= 0
    recruit_oc_var= 0
    calling_in_progress_count= 0
    recruit_oc_know_var= 0
    request_cb_var= 0
    partial_screen_count= 0
    not_screened_count= 0
    ineligible_prior_to_screen_count= 0
    declined_to_screen_count= 0
    requested_call_count= 0
    partial_ies_var= 0
    screened_count= 0
    ineligible_count= 0
    eligible_but_declined_to_count= 0
    eligible_undecided_count= 0
    maybe_eligible_count= 0
    ies_eligible_count= 0
    appt_declined_count= 0
    appt_needed_within_week_since_ies_count= 0
    appt_needed_over_week_since_ies_count= 0
    reschedule_no_show_count= 0
    to_schedule_count= 0
    to_attend_count= 0
    ineligible_at_to_count= 0
    declined_icf_count= 0
    declined_to_proceed_count_1= 0
    eligible_pending_clearance_count= 0
    to_attend_eligible_at_to_count= 0
    needs_baseline_survey_count= 0
    # declined_to_proceed_count_2= 0
    dist_plan_tbd_count= 0
    dist_plan_in_place_count= 0
    dist_delay_problem= 0
    dist_delay_shipping= 0
    dist_plan_pending_count= 0
    tech_setup_appoint_count= 0
    after_techsetup_appt_declined_to_proceed_with_device= 0
    res_no_show_tech_appt_count= 0
    tech_setup_scheduled_count= 0
    home_tech_needed_count= 0
    after_techsetup_appt_declined_to_proceed_with_device_count= 0
    after_tech_setup_attended_ineligible_count= 0
    tech_issue_with_device_count= 0
    pending_day_8_count= 0
    self_measure_ready_count= 0
    pending_day_15_check= 0
    ineligible_bmi_count= 0
    insufficient_data_count= 0
    elig_pending_randamization_count= 0
    ceased_outreach_count= 0
    randamization_count= 0
    devicesetup_pending= 0
    devicesetup_complete= 0
    appt_needed_within_week_since_visit_count= 0
    appt_needed_over_week_since_visit_count= 0
    visit_scheduled_count = 0
    visit_attended_count = 0
    visit_appt_declined_count = 0
    tech_setup_attended_count = 0
    appt_needed_within_week_since_setup_count = 0
    appt_needed_over_week_since_setup_count = 0
    visit_ineligible_count = 0
    visit_declined_to_proceed_count = 0
    visit_eligible_count = 0
    visit_pending_oc_count = 0
    visit_reschedule_noshow_count = 0
    cd_var = ' '

    enroll_criteria_met = {}
    today = datetime.today().date()
    valid_var = ' '
    flag = ' '
    # print(response_json)
    for record in response_json:
        # print(record)
        # if record['record_id'] == '6': print(record)
        
        if 'date_invite_1' in record and record['date_invite_1'].strip():
            # Convert the string date to a date object
            invite_date = datetime.strptime(record['date_invite_1'], '%Y-%m-%d').date()

            # ------------------invitation sent---------------
            # Check if the invite_date is less than or equal to today's date
            if invite_date <= today:
                invite_sent_count += 1

            if 'can_call' in record and record['can_call'].strip():
                can_call_date = datetime.strptime(record['can_call'], '%Y-%m-%d').date()
                    # call_date > today means its status is wait 
                if can_call_date > today and record['eligibility_screener_complete'] != '2':
                    two_week_wait_count += 1

                # --------------calling in progress----------------
                if record['redcap_event_name'] != ' ':
                    if record['vol_excl'] == '1' or record['invite_yn'] == '2' or ( record['screen_icf_oc'] != '3' and record['eligibility_screener_complete'] == '2'):
                        recruit_oc_know_var = '1'
                    else:
                        recruit_oc_know_var = '0'
                else:
                    valid_var = ' '
                    
                if can_call_date <= today and recruit_oc_know_var != '1' and record['cease'] < '1' and valid_var != '':
                    calling_in_progress_count += 1

                #-----------ceased Outreach Count---------------
                if record['cease'] >= '1' and recruit_oc_know_var != '1':
                    ceased_outreach_count += 1

        #------------requested Call count------
        if record['eligibility_screener_complete'] == '0'and (record['twilio_oc'] == '1' or record['screen_icf_oc'] == '3'):
            requested_call_count += 1

        #---------partial screen count----------- 
        if record['redcap_event_name'] != '' and record['screen_icf_oc'] == '1' and record['eligibility_screener_complete'] == '0':
            partial_screen_count += 1

        # ----------inlegible prior to screen---
        if record['vol_excl'] == '1':
            ineligible_prior_to_screen_count += 1
            
        # ----------declined to screen-------
        if record['redcap_event_name'] != '' and (record['invite_yn'] == '2' or record['screen_icf_oc'] == '2'):
            declined_to_screen_count += 1

        #------screened_count-----
        if (record.get('eligibility_screener_complete', '0') == '2' or record.get('eligibility_rescreen_complete', '0') == '2') and record.get('screen_icf_oc', '0') == '1':
            screened_count += 1

        # -------ineligible--------
            if record['es_oc_inelig'] == '1' or record['es_oc_inelig'] == '2':
                ineligible_count += 1

            #-----eligible but declined TO------
            if record['es_oc_elig'] == '2' or record['es_oc_maybe'] == '2' or record['es_oc_elig_v2'] == '2' or record['es_oc_maybe_v2'] == '2':
                eligible_but_declined_to_count += 1
            
            #-------eligible but undecided count------ 
            if record['es_oc_elig'] == '3' or record['es_oc_maybe'] == '3' or record['es_oc_elig_v2'] == '3' or record['es_oc_maybe_v2'] == '3':
                eligible_undecided_count += 1

            #-----maybe eligible count-------
            if record['es_oc_maybe'] == '1':
            # if record['es_oc_maybe'] == '1' or record['es_oc_maybe_v2'] == '1':
                maybe_eligible_count += 1

            #------IES eligible--------
            if record['es_oc_elig'] == '1':
                # print(record['record_id'])
            # if record['es_oc_elig'] == '1' or record['es_oc_maybe'] == '1':
                ies_eligible_count += 1

        #--------appointment_decline/ceased---------- 
        if record['to_appt_status'] == '4':
            appt_declined_count += 1
            
        #----appt needed within week since ies---- 
        if 'es_date' in record and record['es_date'].strip():
            appt_date = datetime.strptime(record['es_date'], '%Y-%m-%d').date()
            if (today - appt_date).days < 8 and record['to_appt_status'] == '2':
                appt_needed_within_week_since_ies_count += 1

            if (today - appt_date).days >= 8 and record['to_appt_status'] =='2':
                appt_needed_over_week_since_ies_count += 1

        #------ rescedule no show----------- 
        if record['to_appt_status'] == '3':
            reschedule_no_show_count += 1

        if (record['es_oc_inelig_v2'] == '1' or record['es_oc_inelig'] == '2'):
            cd_var = '1'
        else:
            cd_var = '0'

        #-------TO Schedule -----------
        if record['to_appt_status'] == '1' and record['to_elig_oc'] < '1' and cd_var != '1':
            to_schedule_count += 1
            
        #-------to attend----------
        if record['to_elig_oc'] > '0':
            to_attend_count += 1
            
        if record['es_oc_inelig_v2'] != '1':
                #-------ineligible at TO-------- 
            if (record['to_elig_oc'] == '2' or record['par_oc'] == '3' or record['if_ies_maybe_2'] == '2'):
                ineligible_at_to_count += 1

                #-----declined icf--------
            if record['to_elig_oc'] == '4':
                declined_icf_count += 1
            
                #------declined to process------- this is in TO section
            if record['to_elig_oc'] == '5':
                declined_to_proceed_count_1 += 1

                #-----eligible_undecided--------
            if record['to_elig_oc'] == '6':
                eligible_undecided_count += 1

                #-----eligible undecided-------- 
            if record['to_elig_oc'] == '3' and record['par_oc'] == '2' and record['if_ies_maybe_2'] =='3':
                eligible_pending_clearance_count += 1
            
                #------eligible at TO-------- 
            if record['to_elig_oc'] == '1' and ( record['par_oc'] == '1' or record['par_oc'] == '4' )and record['if_ies_maybe_2'] !='3':
                to_attend_eligible_at_to_count += 1

        #------------------------------------------------
        #------needs baseline survey----
        # if (record['to_elig_oc'] == '1' and record['if_ies_maybe_2'] !='3' and record['redcap_event_name'] == 'enroll_arm_1' and (record['par_oc'] == '1' or record['par_oc'] == '4') ): #----CP = 1 value 
        if (record['to_elig_oc'] == '1' and record['redcap_event_name'] == 'enroll_arm_1' and (record['par_oc'] == '1' or record['par_oc'] == '4') ): #----CP = 1 value 
            # print("implemented for  " + record['record_id'])
            flag == '1'
            enroll_criteria_met[record['record_id']] = {
                # 'dist_status': record['dist_status'],
                'tech_oc': record['tech_oc'],
                'devicesetup_complete': record['devicesetup_complete'],
                'zoom_appt_status_2': ' ',
                'receipt_date': record['receipt_date'],
                # 'ship_delivered': record['ship_delivered']
            }
        
        if 'zoom_appt_status_2' in record and record['redcap_event_name'] == 'enroll_arm_1' and record['zoom_appt_status_2'] in ['4','3','1']:
            # print("Second imppmm for "  + record['record_id'])
            enroll_criteria_met[record['record_id']] = {
                # 'dist_status': record['dist_status'],
                'tech_oc': record['tech_oc'],
                'devicesetup_complete': record['devicesetup_complete'],
                'zoom_appt_status_2': record['zoom_appt_status_2'],
                'receipt_date': record['receipt_date'],
                # 'ship_delivered': record['ship_delivered']
            }
        
        #---------visit declined/ deceased------ 
        if record['to_elig_oc'] == '1' and record['ip_appt_status'] == '4':
            visit_appt_declined_count += 1   

        #------eligibility visit appointment scheduled block-----
        if 'survey_datebundle' in record and record['es_date'].strip():
            appt1_date = datetime.strptime(record['survey_datebundle'], '%Y-%m-%d').date()
            if (today - appt1_date).days < 8 and record['ip_appt_status'] == '2':
                appt_needed_within_week_since_setup_count += 1

            if (today - appt1_date).days >= 8 and record['ipa_appt_status'] =='2':
                appt_needed_over_week_since_setup_count += 1

        #-------reschedule No show visit-------
        if record['ip_appt_status'] == '3':
            visit_reschedule_noshow_count += 1

        #-------visit Scheduled------- In person Visit scheduled Report
        if (record['par_oc'] == '1' or record['par_oc'] == '4' ) and (record['to_elig_oc'] == '1' or record['to_elig_oc'] == '3') and record['ip_appt_status'] != '4':
            visit_scheduled_count += 1
        
        #--------visit attended------ in person attended OC report 
        if record['to_elig_oc'] == '1':
        # if record['to_elig_oc'] == '1' and record.get('ip_date') not in [None, '', ' '] and record.get('ip_outcome') not in [None, '', ' ']:
            # print(record['record_id'])
            visit_attended_count += 1
        
        #-----visit ineligible-------
        if record['ip_outcome'] == '2':
            visit_ineligible_count += 1

        #-----visit declined to proceed-------
        if record['ip_outcome'] == '4':
            visit_declined_to_proceed_count += 1

        #--------pending outcome------
        if record['ip_outcome'] == '3':
            visit_pending_oc_count += 1    
        
        #--------Visit Eligible------
        if record['ip_outcome'] == '1':
            # print(record['record_id'])
            visit_eligible_count += 1 
        
        #-----rescheudle no show count in tech appt -------
        if record['tech_oc'] < '1' and record['zoom_appt_status_2'] == '3':
            res_no_show_tech_appt_count += 1

        #------tech setup scheduled count  ----  from pivot ( in pivot this value is in the first half tech_schedule_setup_count)
        if record['tech_oc'] < '1' and record['zoom_appt_status_2'] == '1':
            tech_setup_attended_count += 1

        #--------declined to procees with device after tech setup attended----- from pivot 
        if record['tech_oc'] == '4':
            after_techsetup_appt_declined_to_proceed_with_device_count += 1

        #--------ineligible--------
        if record['tech_oc'] == '2':
            after_tech_setup_attended_ineligible_count += 1

        #-------pending resolution tech issue ------
        if record['tech_oc'] == '3':
            tech_issue_with_device_count += 1
            
        #--------self measures ready-------------
        if record['tech_oc'] == '1':
            self_measure_ready_count += 1

            #------r1 randamization------
        if record['randomization_complete'] == '2' and record['redcap_event_name'] !=' ' :
            randamization_count += 1


    # print(enroll_criteria_met)
    for record in response_json:

        # Check if 'enroll_arm_1' criteria were met for this record_id
        if record['record_id'] in enroll_criteria_met:
            # print(enroll_criteria_met)

            tech_oc_from_enroll = enroll_criteria_met[record['record_id']]['tech_oc']
            zoom_appt_status_2_enroll = enroll_criteria_met[record['record_id']]['zoom_appt_status_2']
            device_setup_complete = enroll_criteria_met[record['record_id']]['devicesetup_complete']
            receipt_date = enroll_criteria_met[record['record_id']]['receipt_date']

            if record['redcap_event_name'] == 'baseline_arm_1':
                
                #---------needs baseline survey------- from needs baseline survey report 
                # Check for 'ignite_assessment_survey_complete' < '2'
                if record['ignite_assessment_survey_complete'] < '2':
                    # print(record['record_id'] + ' here is a split value ' + record['ignite_assessment_survey_complete'])
                    needs_baseline_survey_count += 1

                #--------device_setup_pending------ Device Setup Needed Report
                if record['ignite_assessment_survey_complete'] == '2' and (device_setup_complete != '1' or device_setup_complete == ' '):
                    # print(enroll_criteria_met)
                    devicesetup_pending += 1

                #--------device_setup_complete------
                if device_setup_complete == '1' and record['ignite_assessment_survey_complete'] == '2':
                    devicesetup_complete += 1
            
                #----calcs!$BX4:$BX30000,1,calcs!$CY4:$CY30000,0,calcs!$CT4:$CT30000,"<>1",calcs!$BY4:$BY30000,"<>1"
                #-----dist plan is pending---------
                if record['ignite_assessment_survey_complete'] == '2' and device_setup_complete == '1': # and dist_status_from_enroll in ['2', '3']:
                    cy_var = '1'
                else:
                    cy_var = '0'
                
                if record['ignite_assessment_survey_complete'] == '2' and device_setup_complete == '1' and cy_var == '0' and (zoom_appt_status_2_enroll == '4' or tech_oc_from_enroll == '4'): # or dist_status_from_enroll == '7'):
                    by_var = '1'
                else:  
                    by_var = '0'
                
                #-------appt needed with/over week count for tech setup appt 
                if receipt_date.strip():
                # #----DD var----=IF(ISNUMBER(DB7),DB7,IF(ISNUMBER(DC7),DC7,""))
                    receipt_date_count = today - datetime.strptime(receipt_date, '%Y-%m-%d').date()
                    if isinstance(receipt_date_count.days, int):
                        dd_var = '1'
                    else:
                        dd_var = '0'

                    # print('record_id: ' + record['record_id'] + ' receipt_date_count: ' + str(receipt_date_count.days) + ' dd_var: ' + dd_var + ' cy_var: ' + cy_var + ' zoom_appt_status_2_enroll: ' + zoom_appt_status_2_enroll + ' device_setup_complete: ' + device_setup_complete + ' dist_status_from_enroll: ' + dist_status_from_enroll)
                    if (zoom_appt_status_2_enroll == '2' or zoom_appt_status_2_enroll == '0') and cy_var == '1' and tech_oc_from_enroll < '1' and dd_var == '1' and str(receipt_date_count.days) < '7':
                        
                        # print('record_id: ' + record['record_id'] + ' site: ' + site + ' receipt_date: ' + receipt_date + ' receipt_date_count: ' + str(receipt_date_count.days))
                        appt_needed_within_week_since_visit_count += 1
                
                    if (zoom_appt_status_2_enroll == '2' or zoom_appt_status_2_enroll == '0') and cy_var == '1' and dd_var == '1' and tech_oc_from_enroll < '1' and str(receipt_date_count.days) > '7':
                        appt_needed_over_week_since_visit_count += 1

                #------tech setup appointment-------
                if record['ignite_assessment_survey_complete'] == '2': # and(dist_status_from_enroll == '2' or dist_status_from_enroll == '3'):   #-----CX=1 value

                    #-------------decline to proceed with device---- Tech Zoom Scheduling report - from pivot but needs to be updated acc to ignite report. 
                    if zoom_appt_status_2_enroll == '4':
                        after_techsetup_appt_declined_to_proceed_with_device += 1

                    #-------Tech Schedule Setup count------ Tech Zoom Scheduling report - from pivot but needs to be updated acc to ignite report. 
                    if zoom_appt_status_2_enroll == '1' and tech_oc_from_enroll < '1':
                        tech_setup_scheduled_count += 1

                #----------pending day 8 check----------
                if tech_oc_from_enroll == '1' and record['blind_r1_date'] == '' :
                    # print("inside here")
                    if record['v1_d8_elig_oc_v2'] < '1':
                        pending_day_8_count += 1
                
                    #---------pending day 15 check-------
                    if record['v1_d8_elig_oc_v2'] == '3'and record['v1_d15_elig_oc_v2'] < '1':
                        pending_day_15_check += 1
                
                #---------ineligible BMI----------
                    if record['v1_d8_elig_oc_v2'] == '2' or record['v1_d15_elig_oc_v2'] == '2':
                        ineligible_bmi_count += 1
                    
                #--------ineligible insufficient data-----------
                    if record['v1_d8_elig_oc_v2'] == '3' or record['v1_d15_elig_oc_v2'] == '3':
                        insufficient_data_count += 1

                #------elig pending randomization---------
                    if record['v1_d8_elig_oc_v2'] == '1' or record['v1_d15_elig_oc_v2'] == '1':
                        elig_pending_randamization_count += 1

    results = {
        "invite_sent_count": invite_sent_count,
        "two_week_wait_count": two_week_wait_count,
        "calling_in_progress_count": calling_in_progress_count,
        "requested_call_count": requested_call_count,
        "ceased_outreach_count": ceased_outreach_count,
        "partial_screen_count": partial_screen_count,
        "ineligible_prior_to_screen_count": ineligible_prior_to_screen_count,
        "declined_to_screen_count": declined_to_screen_count,
        "screened_count": screened_count,
        "ineligible_count": ineligible_count,
        "eligible_but_declined_to_count": eligible_but_declined_to_count,
        "eligible_undecided_count": eligible_undecided_count,
        "maybe_eligible_count": maybe_eligible_count,
        "ies_eligible_count": ies_eligible_count,
        "appt_declined_count": appt_declined_count,
        "appt_needed_within_week_since_ies_count": appt_needed_within_week_since_ies_count,
        "appt_needed_over_week_since_ies_count": appt_needed_over_week_since_ies_count,
        "reschedule_no_show_count": reschedule_no_show_count,
        "to_schedule_count": to_schedule_count,
        "to_attended_count": to_attend_count,
        "ineligible_at_to_count": ineligible_at_to_count,
        "declined_icf_count": declined_icf_count,
        "declined_to_proceed_count_1": declined_to_proceed_count_1,
        "eligible_undecided_count": eligible_undecided_count,
        "eligible_pending_clearance_count": eligible_pending_clearance_count,
        "to_attend_eligible_at_TO_count": to_attend_eligible_at_to_count,
        "needs_baseline_survey_count": needs_baseline_survey_count,
        "setup_pending_count": devicesetup_pending,
        "setup_complete_count": devicesetup_complete,
        "visit_appt_declined_count": visit_appt_declined_count,
        "appt_needed_within_week_since_setup_count": appt_needed_within_week_since_setup_count,
        "appt_needed_over_week_since_setup_count": appt_needed_over_week_since_setup_count,
        "visit_reschedule_noshow_count": visit_reschedule_noshow_count,
        "visit_scheduled_count": visit_scheduled_count,
        "visit_attended_count": visit_attended_count,
        "visit_ineligible_count": visit_ineligible_count,
        "visit_declined_to_proceed_count": visit_declined_to_proceed_count,
        "visit_pending_oc_count": visit_pending_oc_count,
        "visit_eligible_count": visit_eligible_count,
        "after_techsetup_appt_declined_to_proceed_with_device": after_techsetup_appt_declined_to_proceed_with_device,
        "appt_needed_within_week_since_visit_count": appt_needed_within_week_since_visit_count,
        "appt_needed_over_week_since_visit_count": appt_needed_over_week_since_visit_count,
        "res_no_show_tech_appt_count": res_no_show_tech_appt_count,
        "tech_setup_schedule_count": tech_setup_scheduled_count,
        "tech_setup_attended_count": tech_setup_attended_count,
        "after_techsetup_appt_declined_to_proceed_with_device_count": after_techsetup_appt_declined_to_proceed_with_device_count,
        "after_tech_setup_attended_ineligible_count": after_tech_setup_attended_ineligible_count,
        "tech_issue_with_device_count": tech_issue_with_device_count,
        "self_measure_ready_count": self_measure_ready_count,
        "pending_day_8_count": pending_day_8_count,
        "pending_day_15_check": pending_day_15_check,
        "ineligible_bmi_count": ineligible_bmi_count,
        "insufficient_data_count": insufficient_data_count,
        "elig_pending_randamization_count": elig_pending_randamization_count,
        "randamization_count": randamization_count
    }

    return results

if __name__ == "__main__":
    try:
        # Get current time in Central Time
        central_tz = pytz.timezone("US/Central")
        now_central = datetime.now(central_tz).isoformat()
        print(f"[INFO] Fetching IGNITE recruitment data at {now_central} CST/CDT...")

        # Get processed data
        data = process_redcap_data_for_ignite()

        if not data:
            print("[ERROR] No data received.")
        else:
            # Add timestamp to the data dictionary
            data["timestamp"] = now_central

            # Connect to MongoDB
            client = MongoClient("mongodb://localhost:27017/")  # update if needed
            db = client["ignite_report_db"]
            collection = db["ignite_recruitment_records"]

            # Insert the data
            collection.insert_one(data)
            print("[SUCCESS] Data inserted into MongoDB.")
    except Exception as e:
        print(f"[ERROR] Something went wrong: {e}")
