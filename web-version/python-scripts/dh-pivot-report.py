import requests
import urllib.request, urllib.parse
import json
import pandas as pd
from datetime import datetime

datacall = {
    'token': '5D8E1721D73344CAA8B62EDE0ADE8ED9',
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
    'fields[19]': 'pivot_survey_bundle_complete',
    'fields[20]': 'dist_status',
    'fields[21]': 'zoom_appt_status_2',
    'fields[22]': 'tech_oc',
    'fields[23]': 'blind_r1_date',
    'fields[24]': 'v1_d8_elig_oc_v2',
    'fields[25]': 'v1_d15_elig_oc_v2',
    'fields[26]': 'es_oc_elig',
    'fields[27]': 'es_oc_maybe_v2',
    'fields[28]': 'site',
    'fields[29]': 'randomization_complete',
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
print(jsondata)

print("Received Data")
default_structure = {
    'invite_sent_count': 0,
    'wait_count': 0,
    'two_week_wait_count': 0,
    'recruit_oc_var': 0,
    'calling_in_progress_count': 0,
    'recruit_oc_know_var': 0,
    'request_cb_var': 0,
    'partial_screen_count': 0,
    'not_screened_count': 0,
    'ineligible_prior_to_screen_count': 0,
    'declined_to_screen_count': 0,
    'requested_call_count': 0,
    'partial_ies_var': 0,
    'screened_count': 0,
    'ineligible_count': 0,
    'eligible_but_declined_to_count': 0,
    'eligible_undecided_count': 0,
    'maybe_eligible_count': 0,
    'ies_eligible_count': 0,
    'appt_declined_count': 0,
    'appt_needed_within_week_since_ies_count': 0,
    'appt_needed_over_week_since_ies_count': 0,
    'reschedule_no_show_count': 0,
    'to_schedule_count': 0,
    'to_attend_count': 0,
    'ineligible_at_to_count': 0,
    'declined_icf_count': 0,
    'declined_to_proceed_count_1': 0,
    'eligible_pending_clearance_count': 0,
    'eligible_at_to_count': 0,
    'needs_baseline_survey_count': 0,
    'declined_to_proceed_count_2': 0,
    'dist_plan_tbd_count': 0,
    'dist_plan_in_place_count': 0,
    'dist_delay_problem': 0,
    'dist_delay_shipping': 0,
    'dist_complete': 0,
    'declined_to_proceed_with_device': 0,
    'res_no_show_tech_appt_count': 0,
    'tech_schedule_setup_count': 0,
    'home_tech_needed_count': 0,
    'declined_to_proceed_with_device_count': 0,
    'ineligible_to_proceed_with_device_count': 0,
    'tech_issue_with_device_count': 0,
    'pending_day_8_count': 0,
    'self_measure_ready_count': 0,
    'pending_day_15_check': 0,
    'ineligible_bmi_count': 0,
    'insufficient_data_count': 0,
    'elig_pending_randamization_count': 0,
    'ceased_outreach_count': 0,
    'randamization_count': 0
}

# Initialize the site dictionary with the same default structure for each site
siteDict = {str(i): default_structure.copy() for i in range(1, 4)}



sitesCollect = {
    '1': 0,
    '2': 0,
    '3': 0,
    '': 0
}

enroll_criteria_met = {}
today = datetime.today().date()
valid_var = ' '
for record in response_json:

    # print(record)
    site = str(record['site'])
    sitesCollect[site] += 1

    
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
                
                # print('before' + valid_var + ':' + recruit_oc_know_var+ ' end')
            if can_call_date <= today and recruit_oc_know_var != '1' and record['cease'] < '1' and valid_var != '':
                siteDict[site]['calling_in_progress_count'] += 1


            #-----------ceased Outreach Count---------------
            if record['cease'] >= '1' and recruit_oc_know_var != '1':
                siteDict[site]['ceased_outreach_count'] += 1


    #------------requested Call count-------------
    if record['eligibility_screener_complete'] == '0'and (record['twilio_oc'] == '1' or record['screen_icf_oc'] == '3'):
        siteDict[site]['requested_call_count'] += 1

    #---------partial screen count-----------  
    if record['redcap_event_name'] != '' and record['screen_icf_oc'] == '1' and record['eligibility_screener_complete'] == '0':
        siteDict[site]['partial_screen_count'] += 1

    # ----------inlegible prior to screen-----------
    if record['vol_excl'] == '1':
        siteDict[site]['ineligible_prior_to_screen_count'] += 1

    # ----------declined to screen-----------
    if record['redcap_event_name'] != '' and (record['invite_yn'] == '2' or record['screen_icf_oc'] == '2'):
        siteDict[site]['declined_to_screen_count'] += 1

    if record['eligibility_screener_complete'] == '2' and record['screen_icf_oc'] == '1':
        siteDict[site]['screened_count'] += 1

        #-------ineligible--------
        if record['es_oc_inelig'] == '1' or record['es_oc_inelig'] == '2':
            siteDict[site]['ineligible_count'] += 1

            #-----eligible but declined TO------
        if record['es_oc_elig'] == '2' or record['es_oc_maybe'] == '2':
            siteDict[site]['eligible_but_declined_to_count'] += 1

            #--------eligile_undecided---------
        if record['es_oc_elig'] == '3' or record['es_oc_maybe'] == '3':
            siteDict[site]['eligible_undecided_count'] += 1

            #-----maybe eligible------
        if record['es_oc_maybe'] == '1' or record['es_oc_maybe_v2'] == '1':
            siteDict[site]['maybe_eligible_count'] += 1

             # ------IES eligible -------
        if record['es_oc_elig'] == '1' or record['es_oc_maybe_v2'] == '1':
            siteDict[site]['ies_eligible_count'] += 1

    #------------------------------------------------------
        #--------appointment_decline/ceased----------
    if record['to_appt_status'] == '4':
        siteDict[site]['appt_declined_count'] += 1
    
    #----appt needed within week since ies----
    if 'es_date' in record and record['es_date'].strip():
        appt_date = datetime.strptime(record['es_date'], '%Y-%m-%d').date()
        if (today - appt_date).days < 8 and record['to_appt_status'] == '2':
            siteDict[site]['appt_needed_within_week_since_ies_count'] += 1

        if (today - appt_date).days >= 8 and record['to_appt_status'] =='2':
            siteDict[site]['appt_needed_over_week_since_ies_count'] += 1

    #------ rescedule no show-----------
    if record['to_appt_status'] == '3':
        siteDict[site]['reschedule_no_show_count'] += 1

    #-------TO Schedule -----------
    if record['to_appt_status'] == '1' and record['to_elig_oc'] < '1' and record['es_oc_inelig_v2'] == '1':
        siteDict[site]['to_schedule_count'] += 1

        #-------to attend----------
    if record['to_elig_oc'] > '0':
        siteDict[site]['to_attend_count'] += 1


    if record['es_oc_inelig_v2'] != '1':
            #-------ineligible at TO--------
        if (record['to_elig_oc'] == '2' or record['par_oc'] == '3' or record['if_ies_maybe_2'] == '2'):
            siteDict[site]['ineligible_at_to_count'] += 1

            #-----declined icf--------
        if record['to_elig_oc'] == '4':
            siteDict[site]['declined_icf_count'] += 1
        
            #------declined to process-------
        if record['to_elig_oc'] == '5':
            siteDict[site]['declined_to_proceed_count_1'] += 1

            #-----eligible_undecided--------
        if record['to_elig_oc'] == '6':
            siteDict[site]['eligible_undecided_count'] += 1

            #-----eligible undecided--------
        if record['to_elig_oc'] == '3' and record['par_oc'] == '2' and record['if_ies_maybe_2'] =='3':
            siteDict[site]['eligible_pending_clearance_count'] += 1
        
            #------eligible at TO--------
        if record['to_elig_oc'] == '1' and ( record['par_oc'] == '1' or record['par_oc'] == '4' )and record['if_ies_maybe_2'] !='3':
            siteDict[site]['eligible_at_to_count'] += 1
             
    #------needs baseline survey----
    if (record['to_elig_oc'] == '1' and record['if_ies_maybe_2'] !='3' and record['redcap_event_name'] == 'enroll_arm_1' and (record['par_oc'] == '1' or record['par_oc'] == '4') ): #----CP = 1 value 
        # print("implemented for  " + record['record_id'])
        enroll_criteria_met[record['record_id']] = {
            'site': record['site'],
            'dist_status': record['dist_status'],
            'tech_oc': record['tech_oc'],
            'zoom_appt_status_2': ' '
        }

    if 'zoom_appt_status_2' in record and record['redcap_event_name'] == 'enroll_arm_1' and record['zoom_appt_status_2'] in ['4','3','1']:
        # print("Second imppmm for "  + record['record_id'])
        enroll_criteria_met[record['record_id']] = {
            'site': record['site'],
            'dist_status': record['dist_status'],
            'tech_oc': record['tech_oc'],
            'zoom_appt_status_2': record['zoom_appt_status_2']
        }
        # enroll_criteria_met[record['record_id']]['zoom_appt_status_2'] = record['zoom_appt_status_2']

            #------reschedule no show------------
    if record['tech_oc'] < '1' and record['zoom_appt_status_2'] == '3':
        siteDict[site]['res_no_show_tech_appt_count'] += 1

            #------tech schedule set up ----
    if record['tech_oc'] < '1' and record['zoom_appt_status_2'] == '1':
        siteDict[site]['tech_schedule_setup_count'] += 1

        #--------declined to procees with device-----
    if record['tech_oc'] == '4':
        siteDict[site]['declined_to_proceed_with_device_count'] += 1

        #--------ineligible--------
    if record['tech_oc'] == '2':
        siteDict[site]['ineligible_to_proceed_with_device_count'] += 1

         #-------tech issue pending resolution------
    if record['tech_oc'] == '3':
        siteDict[site]['tech_issue_with_device_count'] += 1

        #--------self measures ready-------------
    if record['tech_oc'] == '1':
        siteDict[site]['self_measure_ready_count'] += 1

        #------r1 randamization------
    if record['randomization_complete'] == '2' and record['redcap_event_name'] !=' ' :
        siteDict[site]['randamization_count'] += 1


for record in response_json:

    # Check if 'enroll_arm_1' criteria were met for this record_id
    if record['record_id'] in enroll_criteria_met:
        site = enroll_criteria_met[record['record_id']]['site']
        dist_status_from_enroll = enroll_criteria_met[record['record_id']]['dist_status']
        tech_oc_from_enroll = enroll_criteria_met[record['record_id']]['tech_oc']
        zoom_appt_status_2_enroll = enroll_criteria_met[record['record_id']]['zoom_appt_status_2']
        # print(enroll_criteria_met)
        # print(zoom_appt_status_2_enroll + 'zoom_appt_value ' + record['record_id'] + 'record_id: site: ' + site + ' tech OC value: ' + tech_oc_from_enroll + " " +record['redcap_event_name'] + " " + record['v1_d8_elig_oc_v2'] + " " + record['blind_r1_date'])
        # print(record['record_id'] + ' record_id: site: ' + site + ' tech OC value: ' + tech_oc_from_enroll + " " + record['redcap_event_name'] + " " + record['v1_d8_elig_oc_v2'] + " " + record['blind_r1_date'])
        # print(record['record_id'] + " value " + site + 'values: '+ dist_status_from_enroll )
        # Process 'baseline_arm_1' related conditions
        if record['redcap_event_name'] == 'baseline_arm_1':
            # Check for 'pivot_survey_bundle_complete' < '2'
            
            if record['pivot_survey_bundle_complete'] < '2':
                # print(record['record_id'] + ' here is a split value ' + record['pivot_survey_bundle_complete'])
                siteDict[site]['needs_baseline_survey_count'] += 1
            
            # Check for 'pivot_survey_bundle_complete' == '2' and 'dist_status' == '7'
            if record['pivot_survey_bundle_complete'] == '2' and dist_status_from_enroll == '7':
                # print(record['record_id'] + ' here' + dist_status_from_enroll)
                siteDict[site]['declined_to_proceed_count_2'] += 1

            #-----distribution plan TBD------
            if record['pivot_survey_bundle_complete'] == '2' and dist_status_from_enroll == '0':
                # print('value is zero here ')
                siteDict[site]['dist_plan_tbd_count'] += 1

        #-----dist plan in place-------
            if record['pivot_survey_bundle_complete'] == '2' and dist_status_from_enroll == '1':
                # print('value 1 here')
                siteDict[site]['dist_plan_in_place_count'] += 1

        #-----dist delay/problem pickup-----
            if record['pivot_survey_bundle_complete'] == '2' and dist_status_from_enroll == '6':
                # print('value 6 here')
                siteDict[site]['dist_delay_problem'] += 1

        #---dist delay shipping----
            if record['pivot_survey_bundle_complete'] == '2' and (dist_status_from_enroll == '5' or dist_status_from_enroll == '4'):
                # print('value 5/6 here')
                siteDict[site]['dist_delay_shipping'] += 1

        #---dist complete-------
            if record['pivot_survey_bundle_complete'] == '2' and(dist_status_from_enroll == '2' or dist_status_from_enroll == '3'):   #-----CX=1 value
                # print('value 2/3 here')
                siteDict[site]['dist_complete'] += 1
                # print('before here')

                #-------------decline to proceed with device
                if zoom_appt_status_2_enroll == '4':
                    siteDict[site]['declined_to_proceed_with_device'] += 1

                if zoom_appt_status_2_enroll == '1' and tech_oc_from_enroll < '1':
                    siteDict[site]['tech_schedule_setup_count'] += 1

                else:
                    if tech_oc_from_enroll > '0':
                        siteDict[site]['home_tech_needed_count'] += 1

            #----------pending day 8 check----------
            if tech_oc_from_enroll == '1' and record['blind_r1_date'] == '' :
                # print("inside here")
                if record['v1_d8_elig_oc_v2'] < '1':
                    siteDict[site]['pending_day_8_count'] += 1
            
                  #---------pending day 15 check-------
                if record['v1_d8_elig_oc_v2'] == '3'and record['v1_d15_elig_oc_v2'] < '1':
                    siteDict[site]['pending_day_15_check'] += 1
            
               #---------ineligible BMI----------
                if record['v1_d8_elig_oc_v2'] == '2' or record['v1_d15_elig_oc_v2'] == '2':
                    siteDict[site]['ineligible_bmi_count'] += 1
                
            #--------ineligible insufficient data-----------
                if record['v1_d8_elig_oc_v2'] == '3' or record['v1_d15_elig_oc_v2'] == '3':
                    siteDict[site]['insufficient_data_count'] += 1

             #------elig pending randomization---------
                if record['v1_d8_elig_oc_v2'] == '1' or record['v1_d15_elig_oc_v2'] == '1':
                    siteDict[site]['elig_pending_randamization_count'] += 1


for site in ['1','2','3']:
#     # Print the final count of invites sent for the current site
    print('-------site-' + site + '---------')
    print('Invites sent count: ' + str(siteDict[site]['invite_sent_count']))
    print('Two week wait count: ' + str(siteDict[site]['two_week_wait_count']))
    print('calling_in_progress_count: ' + str(siteDict[site]['calling_in_progress_count']))
    print('requested_call_count: ' + str(siteDict[site]['requested_call_count']))
    print('ceased_outreach_count: ' + str(siteDict[site]['ceased_outreach_count']))
    print('partial_screen_count: ' + str(siteDict[site]['partial_screen_count']))
    print('not_screened_count: ' + str(siteDict[site]['ineligible_prior_to_screen_count'] + siteDict[site]['declined_to_screen_count']))
    print('ineligible_prior_to_screen_count: ' + str(siteDict[site]['ineligible_prior_to_screen_count']))
    print('declined_to_screen_count: ' + str(siteDict[site]['declined_to_screen_count']))
    print('screened_count: ' + str(siteDict[site]['screened_count']))
    print('ineligible_count: ' + str(siteDict[site]['ineligible_count']))
    print('eligible_but_declined_to_count: ' + str(siteDict[site]['eligible_but_declined_to_count']))
    print('eligible_undecided_count: ' + str(siteDict[site]['eligible_undecided_count']))
    print('maybe_eligible_count: ' + str(siteDict[site]['maybe_eligible_count']))
    print('ies_eligible_count: ' + str(siteDict[site]['ies_eligible_count']))
    print('appt_declined_count: ' + str(siteDict[site]['appt_declined_count']))
    print('appt_needed_within_week_since_ies_count: ' + str(siteDict[site]['appt_needed_within_week_since_ies_count']))
    print('appt_needed_over_week_since_ies_count: ' + str(siteDict[site]['appt_needed_over_week_since_ies_count']))
    print('reschedule_no_show_count: ' + str(siteDict[site]['reschedule_no_show_count']))
    print('to_schedule_count: ' + str(siteDict[site]['to_schedule_count']))
    print('to_attend_count: ' + str(siteDict[site]['to_attend_count']))
    print('ineligible_at_to_count: ' + str(siteDict[site]['ineligible_at_to_count']))
    print('declined_icf_count: ' + str(siteDict[site]['declined_icf_count']))
    print('declined_to_proceed_count_1: ' + str(siteDict[site]['declined_to_proceed_count_1']))
    print('eligible_undecided_count: ' + str(siteDict[site]['eligible_undecided_count']))
    print('eligible_pending_clearance_count: ' + str(siteDict[site]['eligible_pending_clearance_count']))
    print('to_attend_eligible_at_to_countcount: ' + str(siteDict[site]['eligible_at_to_count']))
    print('needs_baseline_survey_count: ' + str(siteDict[site]['needs_baseline_survey_count']))
    print('declined_to_proceed_count_2: ' + str(siteDict[site]['declined_to_proceed_count_2']))
    print('dist_plan_tbd_count: ' + str(siteDict[site]['dist_plan_tbd_count']))
    print('dist_plan_in_place_count: ' + str(siteDict[site]['dist_plan_in_place_count']))
    print('dist_delay_problem: ' + str(siteDict[site]['dist_delay_problem']))
    print('dist_delay_shipping: ' + str(siteDict[site]['dist_delay_shipping']))
    print('dist_complete: ' + str(siteDict[site]['dist_complete']))
    print('declined_to_proceed_with_device: ' + str(siteDict[site]['declined_to_proceed_with_device']))
    print('res_no_show_tech_appt_count: ' + str(siteDict[site]['res_no_show_tech_appt_count']))
    print('tech_schedule_setup_count: ' + str(siteDict[site]['tech_schedule_setup_count']))
    print('home_tech_needed_count: ' + str(siteDict[site]['home_tech_needed_count']))
    print('declined_to_proceed_with_device_count_in TO: ' + str(siteDict[site]['declined_to_proceed_with_device_count']))
    print('ineligible_to_proceed_with_device_count: ' + str(siteDict[site]['ineligible_to_proceed_with_device_count']))
    print('tech_issue_with_device_count: ' + str(siteDict[site]['tech_issue_with_device_count']))
    print('self_measure_ready_count: ' + str(siteDict[site]['self_measure_ready_count']))
    print('pending_day_8_count: ' + str(siteDict[site]['pending_day_8_count']))
    print('pending_day_15_check: ' + str(siteDict[site]['pending_day_15_check']))
    print('ineligible_bmi_count: ' + str(siteDict[site]['ineligible_bmi_count']))
    print('insufficient_data_count: ' + str(siteDict[site]['insufficient_data_count']))
    print('elig_pending_randamization_count: ' + str(siteDict[site]['elig_pending_randamization_count']))
    print('randamization_count: ' + str(siteDict[site]['randamization_count']))


# Initialize a dictionary to hold the sum of all values from sites 1, 2, and 3
# Initialize a dictionary to hold the total values for each metric
total_values = {key: 0 for key in default_structure.keys()}

# Calculate the total values for each metric across all sites
for site in ['1', '2', '3']:
    for key in siteDict[site]:
        total_values[key] += siteDict[site][key]

# Print the total values in the desired format
print("-------Total Values Across All Sites---------")
print("Invites sent count: " + str(total_values['invite_sent_count']))
print("Two week wait count: " + str(total_values['two_week_wait_count']))
print("calling_in_progress_count: " + str(total_values['calling_in_progress_count']))
print("requested_call_count: " + str(total_values['requested_call_count']))
print("ceased_outreach_count: " + str(total_values['ceased_outreach_count']))
print("partial_screen_count: " + str(total_values['partial_screen_count']))
print("not_screened_count: " + str(total_values['ineligible_prior_to_screen_count'] + total_values['declined_to_screen_count']))
print("ineligible_prior_to_screen_count: " + str(total_values['ineligible_prior_to_screen_count']))
print("declined_to_screen_count: " + str(total_values['declined_to_screen_count']))
print("screened_count: " + str(total_values['screened_count']))
print("ineligible_count: " + str(total_values['ineligible_count']))
print("eligible_but_declined_to_count: " + str(total_values['eligible_but_declined_to_count']))
print("eligible_undecided_count: " + str(total_values['eligible_undecided_count']))
print("maybe_eligible_count: " + str(total_values['maybe_eligible_count']))
print("ies_eligible_count: " + str(total_values['ies_eligible_count']))
print("appt_declined_count: " + str(total_values['appt_declined_count']))
print("appt_needed_within_week_since_ies_count: " + str(total_values['appt_needed_within_week_since_ies_count']))
print("appt_needed_over_week_since_ies_count: " + str(total_values['appt_needed_over_week_since_ies_count']))
print("reschedule_no_show_count: " + str(total_values['reschedule_no_show_count']))
print("to_schedule_count: " + str(total_values['to_schedule_count']))
print("to_attend_count: " + str(total_values['to_attend_count']))
print("ineligible_at_to_count: " + str(total_values['ineligible_at_to_count']))
print("declined_icf_count: " + str(total_values['declined_icf_count']))
print("declined_to_proceed_count_1: " + str(total_values['declined_to_proceed_count_1']))
print("eligible_undecided_count: " + str(total_values['eligible_undecided_count']))
print("eligible_pending_clearance_count: " + str(total_values['eligible_pending_clearance_count']))
print("to_attend_eligible_at_to_countcount: " + str(total_values['eligible_at_to_count']))
print("needs_baseline_survey_count: " + str(total_values['needs_baseline_survey_count']))
print("declined_to_proceed_count_2: " + str(total_values['declined_to_proceed_count_2']))
print("dist_plan_tbd_count: " + str(total_values['dist_plan_tbd_count']))
print("dist_plan_in_place_count: " + str(total_values['dist_plan_in_place_count']))
print("dist_delay_problem: " + str(total_values['dist_delay_problem']))
print("dist_delay_shipping: " + str(total_values['dist_delay_shipping']))
print("dist_complete: " + str(total_values['dist_complete']))
print("declined_to_proceed_with_device: " + str(total_values['declined_to_proceed_with_device']))
print("res_no_show_tech_appt_count: " + str(total_values['res_no_show_tech_appt_count']))
print("tech_schedule_setup_count: " + str(total_values['tech_schedule_setup_count']))
print("home_tech_needed_count: " + str(total_values['home_tech_needed_count']))
print("declined_to_proceed_with_device_count_in TO: " + str(total_values['declined_to_proceed_with_device_count']))
print("ineligible_to_proceed_with_device_count: " + str(total_values['ineligible_to_proceed_with_device_count']))
print("tech_issue_with_device_count: " + str(total_values['tech_issue_with_device_count']))
print("self_measure_ready_count: " + str(total_values['self_measure_ready_count']))
print("pending_day_8_count: " + str(total_values['pending_day_8_count']))
print("pending_day_15_check: " + str(total_values['pending_day_15_check']))
print("ineligible_bmi_count: " + str(total_values['ineligible_bmi_count']))
print("insufficient_data_count: " + str(total_values['insufficient_data_count']))
print("elig_pending_randamization_count: " + str(total_values['elig_pending_randamization_count']))
print("randamization_count: " + str(total_values['randamization_count']))