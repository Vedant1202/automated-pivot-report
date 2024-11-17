#!/usr/bin/env python
import requests
import urllib.request, urllib.parse
import json
import pandas as pd
from datetime import datetime
import json
import os
from pymongo import MongoClient

# Set up MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['pivot-report-summaries']  # Replace 'database_name' with your actual database name
collection = db['summaries']  # Replace 'log_collection' with your preferred collection name

# Append logData to MongoDB collection
def append_to_mongodb(data):
    try:
        collection.insert_one(data)
        print("Data inserted into MongoDB successfully.")
    except Exception as e:
        print("An error occurred while inserting data into MongoDB:", e)

data = {
    'token': '3A10735CD8F78FB6643C7410F1BC2910',
    'content': 'record',
    'action': 'export',
    'format': 'json',
    'type': 'flat',
    'csvDelimiter': '',
    'fields[0]': 'record_id',
    'fields[1]': 'site',
    'fields[2]': 'cease',
    'fields[3]': 'date_invite_1',
    'fields[4]': 'can_call',
    'fields[5]': 'twilio_oc',
    'fields[6]': 'vol_excl',
    'fields[7]': 'screen_icf_oc',
    'fields[8]': 'eligibility_screener_complete',
    'fields[9]': 'invite_yn',
    'fields[10]': 'es_date',
    'fields[11]': 'es_oc_inelig',
    'fields[12]': 'es_oc_maybe',
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
    'fields[30]': 'participant_log_complete',
    'fields[31]': 'decline_invite',

    'events[0]': 'enroll_arm_1',
    'events[1]': 'baseline_arm_1',
    'events[2]': '6_week_arm_1',
    'events[3]': '12_week_arm_1',
    'events[4]': '24_week_arm_1',

    'rawOrLabel': 'raw',
    'rawOrLabelHeaders': 'raw',
    'exportCheckboxLabel': 'false',
    'exportSurveyFields': 'false',
    'exportDataAccessGroups': 'false',
    'returnFormat': 'json'
}

r = requests.post('https://www.redcap.ihrp.uic.edu/api/',data=data)
print('HTTP Status: ' + str(r.status_code))

jsondata = r.json()
response_json = jsondata

sitesDict = {
    '1': {
        'invite_sent_count' : 0,
        'wait_count' : 0,
        'two_week_wait_count' : 0,
        'recruit_oc_var' : 0,
        'calling_in_progress_count' : 0,
        'recruit_oc_know_var' : 0,
        'request_cb_var' : 0,
        'partial_screen_count' : 0,
        'not_screened_count' : 0,
        'ineligible_prior_to_screen_count' : 0,
        'declined_to_screen_count' : 0,
        'valid_var' : '',
        'requested_call_count' : 0,
        'partial_ies_var' : 0,
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
    },
    '2': {
        'invite_sent_count' : 0,
        'wait_count' : 0,
        'two_week_wait_count' : 0,
        'recruit_oc_var' : 0,
        'calling_in_progress_count' : 0,
        'recruit_oc_know_var' : 0,
        'request_cb_var' : 0,
        'partial_screen_count' : 0,
        'not_screened_count' : 0,
        'ineligible_prior_to_screen_count' : 0,
        'declined_to_screen_count' : 0,
        'valid_var' : '',
        'requested_call_count' : 0,
        'partial_ies_var' : 0,
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
    },
    '3': {
        'invite_sent_count' : 0,
        'wait_count' : 0,
        'two_week_wait_count' : 0,
        'recruit_oc_var' : 0,
        'calling_in_progress_count' : 0,
        'recruit_oc_know_var' : 0,
        'request_cb_var' : 0,
        'partial_screen_count' : 0,
        'not_screened_count' : 0,
        'ineligible_prior_to_screen_count' : 0,
        'declined_to_screen_count' : 0,
        'valid_var' : '',
        'requested_call_count' : 0,
        'partial_ies_var' : 0,
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
}
today = datetime.today().date()
sitesCollect = {
    '1': 0,
    '2': 0,
    '3': 0,
    '': 0
}

def append_json_object(file_path, new_data):
    # Check if the file exists, if not create an empty list
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            json.dump([], file)
    
    # Read the existing data from the file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Append the new data to the list
    data.append(new_data)

    # Write the updated list back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def retrieve_objects_by_date(file_path, date_value):
    # Read the data from the file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Filter objects by 'date'
    matching_objects = [obj for obj in data if obj.get('date') == date_value]

    return matching_objects

try:
    # response_json = r.json()
    # print(response_json)      # Prints the JSON response

    for record in response_json:
        # print(record)
        # print(record['record_id'] + "event name: " + record['redcap_event_name']+" cease: " + record['cease'] + " invite_date:  " + record['date_invite_1'] + " can_call:  " + record['can_call'] + " twilight_oc:  " + record['twilio_oc'] + " log completed:  " + record['participant_log_complete'] + " invite_yn: " + record['invite_yn'] + " invite decline:  " + record['decline_invite'] + " vol_excl: " + record['vol_excl'] + " screen_icf:  " + record['screen_icf_oc'] + " eleg_screener_complete: " + record['eligibility_screener_complete'])
        site = str(record['site'])
        sitesCollect[site] += 1
        enroll_criteria_met = {}
        # print(site)
        # print(type(site))
        # valid_var = ''

        # print(sitesDict[site])
        # print(sitesDict[site]['invite_sent_count'])

        # ------------------invitation sent---------------
        if record['date_invite_1'] and record['date_invite_1'] != '':
            # Convert the string date to a date object
            invite_date = datetime.strptime(record['date_invite_1'], '%Y-%m-%d').date()

            # Check if the invite_date is less than or equal to today's date
            if invite_date <= today:
                sitesDict[site]['invite_sent_count'] += 1
            else:  # If the invite_date is greater than today's date
                sitesDict[site]['wait_count'] += 1

            # --------------within 2-week wait----------------
            if record['can_call'] != '':
                can_call_date = datetime.strptime(record['can_call'], '%Y-%m-%d').date()

                # call_date > today means its status is wait 
                if can_call_date > today and record['eligibility_screener_complete'] != '2':
                    sitesDict[site]['two_week_wait_count'] += 1

            # --------------calling in progress----------------
                # ---------------rec_oc_known-------------
                if record['redcap_event_name'] != '':
                    if record['vol_excl'] == '1' or record['invite_yn'] == '2' or ( record['screen_icf_oc'] != '3' and record['eligibility_screener_complete'] == '2'):
                        recruit_oc_know_var = '1'
                    else:
                        recruit_oc_know_var = '0'

                else:
                    sitesDict[site]['valid_var'] = ''

                if can_call_date <= today and recruit_oc_know_var != '1' and record['cease'] < '1' and sitesDict[site]['valid_var'] != '':
                    sitesDict[site]['calling_in_progress_count'] += 1

        #------------requested Call count-------------
        if record['eligibility_screener_complete'] == '0' and (record['twilio_oc'] == '4' or record['screen_icf_oc'] == '3'):
            request_cb_var = '1'

            if request_cb_var == ' 1':
                sitesDict[site]['requested_call_count'] += 1

        else:
            request_cb_var = '0'

            

        #---------partial screen count-----------
        if record['redcap_event_name'] != '' and record['screen_icf_oc'] == '1' and record['eligibility_screener_complete'] == '0':
            partial_ies_var = '1'
            sitesDict[site]['partial_screen_count'] += 1
            
        else: 
            partial_ies_var = '0'

        # ----------inlegible prior to screen-----------
        if record['vol_excl'] == '1':
            sitesDict[site]['ineligible_prior_to_screen_count'] += 1

        # ----------declined to screen-----------
        if record['redcap_event_name'] != '' and (record['invite_yn'] == '2' or record['screen_icf_oc'] == '2'):
            sitesDict[site]['declined_to_screen_count'] += 1

        if record['eligibility_screener_complete'] == '2' and record['screen_icf_oc'] == '1':
            sitesDict[site]['screened_count'] += 1

            #-------ineligible--------
            if record['es_oc_inelig'] == '1' or record['es_oc_inelig'] == '2':
                sitesDict[site]['ineligible_count'] += 1

                #-----eligible but declined TO------
            if record['es_oc_elig'] == '2' or record['es_oc_maybe'] == '2':
                sitesDict[site]['eligible_but_declined_to_count'] += 1

                #--------eligile_undecided---------
            if record['es_oc_elig'] == '3' or record['es_oc_maybe'] == '3':
                sitesDict[site]['eligible_undecided_count'] += 1

                #-----maybe eligible------
            if record['es_oc_maybe'] == '1' or record['es_oc_maybe_v2'] == '1':
                sitesDict[site]['maybe_eligible_count'] += 1

                # ------IES eligible -------
            if record['es_oc_elig'] == '1' or record['es_oc_maybe_v2'] == '1':
                sitesDict[site]['ies_eligible_count'] += 1

        #------------------------------------------------------
            #--------appointment_decline/ceased----------
        if record['to_appt_status'] == '4':
            sitesDict[site]['appt_declined_count'] += 1
        
        #----appt needed within week since ies----
        if 'es_date' in record and record['es_date'].strip():
            appt_date = datetime.strptime(record['es_date'], '%Y-%m-%d').date()
            if (today - appt_date).days < 8 and record['to_appt_status'] == '2':
                sitesDict[site]['appt_needed_within_week_since_ies_count'] += 1

            if (today - appt_date).days >= 8 and record['to_appt_status'] =='2':
                sitesDict[site]['appt_needed_over_week_since_ies_count'] += 1

        #------ rescedule no show-----------
        if record['to_appt_status'] == '3':
            sitesDict[site]['reschedule_no_show_count'] += 1

        #-------TO Schedule -----------
        if record['to_appt_status'] == '1' and record['to_elig_oc'] < '1' and record['es_oc_inelig_v2'] == '1':
            sitesDict[site]['to_schedule_count'] += 1

            #-------to attend----------
        if record['to_elig_oc'] > '0':
            sitesDict[site]['to_attend_count'] += 1


        if record['es_oc_inelig_v2'] != '1':
                #-------ineligible at TO--------
            if (record['to_elig_oc'] == '2' or record['par_oc'] == '3' or record['if_ies_maybe_2'] == '2'):
                sitesDict[site]['ineligible_at_to_count'] += 1

                #-----declined icf--------
            if record['to_elig_oc'] == '4':
                sitesDict[site]['declined_icf_count'] += 1
            
                #------declined to process-------
            if record['to_elig_oc'] == '5':
                sitesDict[site]['declined_to_proceed_count_1'] += 1

                #-----eligible_undecided--------
            if record['to_elig_oc'] == '6':
                sitesDict[site]['eligible_undecided_count'] += 1

                #-----eligible undecided--------
            if record['to_elig_oc'] == '3' and record['par_oc'] == '2' and record['if_ies_maybe_2'] =='3':
                sitesDict[site]['eligible_pending_clearance_count'] += 1
            
                #------eligible at TO--------
            if record['to_elig_oc'] == '1' and ( record['par_oc'] == '1' or record['par_oc'] == '4' )and record['if_ies_maybe_2'] !='3':
                sitesDict[site]['eligible_at_to_count'] += 1
                
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
            sitesDict[site]['res_no_show_tech_appt_count'] += 1

                #------tech schedule set up ----
        if record['tech_oc'] < '1' and record['zoom_appt_status_2'] == '1':
            sitesDict[site]['tech_schedule_setup_count'] += 1

            #--------declined to procees with device-----
        if record['tech_oc'] == '4':
            sitesDict[site]['declined_to_proceed_with_device_count'] += 1

            #--------ineligible--------
        if record['tech_oc'] == '2':
            sitesDict[site]['ineligible_to_proceed_with_device_count'] += 1

            #-------tech issue pending resolution------
        if record['tech_oc'] == '3':
            sitesDict[site]['tech_issue_with_device_count'] += 1

            #--------self measures ready-------------
        if record['tech_oc'] == '1':
            sitesDict[site]['self_measure_ready_count'] += 1

            #------r1 randamization------
        if record['randomization_complete'] == '2' and record['redcap_event_name'] !=' ' :
            sitesDict[site]['randamization_count'] += 1


    totals = {
        'invite_sent_count' : 0,
        'wait_count' : 0,
        'two_week_wait_count' : 0,
        'recruit_oc_var' : 0,
        'calling_in_progress_count' : 0,
        'recruit_oc_know_var' : 0,
        'request_cb_var' : 0,
        'partial_screen_count' : 0,
        'not_screened_count' : 0,
        'ineligible_prior_to_screen_count' : 0,
        'declined_to_screen_count' : 0,
        'valid_var' : '',
        'requested_call_count' : 0,
        'partial_ies_var' : 0,
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

    for site in sitesDict.values():
        for key in site.keys():
            if key in totals.keys():
                totals[key] += site[key]


    site = '1'
    # # Print the final count of invites sent
    print('Invites sent count:' + str({sitesDict[site]['invite_sent_count']}))
    print('Wait count:' + str({sitesDict[site]['wait_count']}))
    print('Within 2-week wait count:' + str({sitesDict[site]['two_week_wait_count']}))
    print('Calling in progress count:' + str({sitesDict[site]['calling_in_progress_count']}))
    print('Recruit OC Known:' + str({recruit_oc_know_var}))
    print('Requested Call count:' + str({sitesDict[site]['requested_call_count']}))      
    print('Partial Screen count:' + str({sitesDict[site]['partial_screen_count']}))
    # print('Not screened count:' + str({not_screened_count}))
    print('Ineligible prior to screen count:' + str({sitesDict[site]['ineligible_prior_to_screen_count']}))
    print('Declined to screen count:' + str({sitesDict[site]['declined_to_screen_count']}))

    print('TOTALS')
    print('Invites sent count:' + str({totals['invite_sent_count']}))
    print('Wait count:' + str({totals['wait_count']}))
    print('Within 2-week wait count:' + str({totals['two_week_wait_count']}))
    print('Calling in progress count:' + str({totals['calling_in_progress_count']}))
    print('Recruit OC Known:' + str({recruit_oc_know_var}))
    print('Requested Call count:' + str({totals['requested_call_count']}))      
    print('Partial Screen count:' + str({totals['partial_screen_count']}))
    # print('Not screened count:' + str({not_screened_count}))
    print('Ineligible prior to screen count:' + str({totals['ineligible_prior_to_screen_count']}))
    print('Declined to screen count:' + str({totals['declined_to_screen_count']}))

    print(sitesCollect)
    logData = {
        'date': datetime.today().strftime('%Y-%m-%d'),
        # 'date': '2024-11-01',
        'sitesDict': sitesDict,
        'totals': totals,
        'sitesCollect': sitesCollect,
    }
    append_to_mongodb(logData)
    print("==================== Appended to MongoDB ======================")

    # df = pd.read_json(logData)
    # df_csv = df.to_csv()

    # f = open("log" + datetime.today().strftime('%Y-%m-%d') + ".json", "a")
    # f.write(logData)
    # f.close()
    append_json_object('log.json', logData)
    # print(retrieve_objects_by_date('log.json', '2024-09-11'))

except ValueError:
    # If the response is not JSON or there's an error in conversion, handle it here
    print("Response is not in JSON format.")
    # print(respdata.text)  # Print raw text response if JSON conversion fails


