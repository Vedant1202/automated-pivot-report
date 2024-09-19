#!/usr/bin/env python
# import requests
import urllib.request, urllib.parse
import json
import pandas as pd
from datetime import datetime
import json
import os

#!/usr/bin/env python
import requests
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
    }

    for site in sitesDict.values():
        for key in site.keys():
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
        # 'date': '2024-09-11',
        'sitesDict': sitesDict,
        'totals': totals,
        'sitesCollect': sitesCollect,
    }

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


