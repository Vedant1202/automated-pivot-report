# import requests
import urllib.request, urllib.parse
import json
import pandas as pd
from datetime import datetime
import json
import os
from pymongo import MongoClient

#!/usr/bin/env python
import requests

def is_valid_date(date_str: str) -> bool:
    # Define the expected date format
    date_format = "%Y-%m-%d"
    
    try:
        # Try to parse the string into a datetime object
        datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        # If parsing fails, it's not a valid date
        return False

def isDateLessThanThirdOctTwentyTwentyThree(date1: str, date2: str = '2023-10-03') -> bool:
    # Convert the strings to datetime objects
    date_format = "%Y-%m-%d"
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    
    # Compare the dates
    return d1 <= d2

# Set up MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['pivot-report-summaries']  # Replace 'database_name' with your actual database name
collection = db['md-review-summaries']  # Replace 'log_collection' with your preferred collection name

# Append logData to MongoDB collection
def append_to_mongodb(data):
    try:
        collection.insert_one(data)
        print("Data inserted into MongoDB successfully.")
    except Exception as e:
        print("An error occurred while inserting data into MongoDB:", e)

data = {
    # 'token': '3A10735CD8F78FB6643C7410F1BC2910',
    'token': '5D8E1721D73344CAA8B62EDE0ADE8ED9',
    'content': 'record',
    'action': 'export',
    'format': 'json',
    'type': 'flat',
    'csvDelimiter': '',
    'fields[0]': 'record_id',
    'fields[1]': 'site',
    'fields[2]': 'to_elig_oc',
    'fields[3]': 'par_oc',
    'fields[4]': 'par_rev_date',
    'events[0]': 'enroll_arm_1',
    'events[1]': 'baseline_arm_1',
    'events[2]': '6_week_arm_1',
    'events[3]': '12_week_arm_1',
    'events[4]': '24_week_arm_1',
    'events[5]': '52_week_arm_1',
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
        'to_attended' : 0,
        'md_clearance_required_total' : 0,
        'md_clearance_required_standard_parq' : 0,
        'md_clearance_required_modified_parq' : 0,
        'par_review_pending' : 0,
        'par_reviewed_ineligible' : 0,
        'par_reviewed_eligible' : 0
    },
    '2': {
        'to_attended' : 0,
        'md_clearance_required_total' : 0,
        'md_clearance_required_standard_parq' : 0,
        'md_clearance_required_modified_parq' : 0,
        'par_review_pending' : 0,
        'par_reviewed_ineligible' : 0,
        'par_reviewed_eligible' : 0
    },
    '3': {
        'to_attended' : 0,
        'md_clearance_required_total' : 0,
        'md_clearance_required_standard_parq' : 0,
        'md_clearance_required_modified_parq' : 0,
        'par_review_pending' : 0,
        'par_reviewed_ineligible' : 0,
        'par_reviewed_eligible' : 0
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

        # ------------------TO attended---------------
        if record['to_elig_oc'] and int(record['to_elig_oc']) > 0:
            sitesDict[site]['to_attended'] += 1

        # ------------------MD Clearance Required Total---------------
        if record['par_oc'] and int(record['par_oc']) > 0:
            sitesDict[site]['md_clearance_required_total'] += 1

            # ------------------MD Clearance Required < 10.3.23 standard PARQ---------------
            if record['par_rev_date'] and is_valid_date(record['par_rev_date']) and isDateLessThanThirdOctTwentyTwentyThree(record['par_rev_date']):
                sitesDict[site]['md_clearance_required_standard_parq'] += 1

            # ------------------MD Clearance Required > 10.3.23 modified PARQ---------------
            if record['par_rev_date'] and is_valid_date(record['par_rev_date']) and not isDateLessThanThirdOctTwentyTwentyThree(record['par_rev_date']):
                sitesDict[site]['md_clearance_required_modified_parq'] += 1

        # ------------------PAR review pending---------------
        if record['par_oc'] and int(record['par_oc']) == 2:
            sitesDict[site]['par_review_pending'] += 1

        # ------------------PAR reviewed - Ineligible---------------
        if record['par_oc'] and int(record['par_oc']) == 3:
            sitesDict[site]['par_review_pending'] += 1

        # ------------------PAR reviewed - Eligible---------------
        if record['par_oc'] and int(record['par_oc']) == 4:
            sitesDict[site]['md_clearance_required_total'] += 1

    totals = {
        'to_attended' : 0,
        'md_clearance_required_total' : 0,
        'md_clearance_required_standard_parq' : 0,
        'md_clearance_required_modified_parq' : 0,
        'par_review_pending' : 0,
        'par_reviewed_ineligible' : 0,
        'par_reviewed_eligible' : 0
    }

    for site in sitesDict.values():
        for key in site.keys():
            totals[key] += site[key]


    # site = '1'
    # # # Print the final count of invites sent
    # print('Invites sent count:' + str({sitesDict[site]['invite_sent_count']}))
    # print('Wait count:' + str({sitesDict[site]['wait_count']}))
    # print('Within 2-week wait count:' + str({sitesDict[site]['two_week_wait_count']}))
    # print('Calling in progress count:' + str({sitesDict[site]['calling_in_progress_count']}))
    # print('Requested Call count:' + str({sitesDict[site]['requested_call_count']}))      
    # print('Partial Screen count:' + str({sitesDict[site]['partial_screen_count']}))
    # # print('Not screened count:' + str({not_screened_count}))
    # print('Ineligible prior to screen count:' + str({sitesDict[site]['ineligible_prior_to_screen_count']}))
    # print('Declined to screen count:' + str({sitesDict[site]['declined_to_screen_count']}))

    # print('TOTALS')
    # print('Invites sent count:' + str({totals['invite_sent_count']}))
    # print('Wait count:' + str({totals['wait_count']}))
    # print('Within 2-week wait count:' + str({totals['two_week_wait_count']}))
    # print('Calling in progress count:' + str({totals['calling_in_progress_count']}))
    # print('Requested Call count:' + str({totals['requested_call_count']}))      
    # print('Partial Screen count:' + str({totals['partial_screen_count']}))
    # # print('Not screened count:' + str({not_screened_count}))
    # print('Ineligible prior to screen count:' + str({totals['ineligible_prior_to_screen_count']}))
    # print('Declined to screen count:' + str({totals['declined_to_screen_count']}))

    print(sitesCollect)
    logData = {
        'date': datetime.today().strftime('%Y-%m-%d'),
        # 'date': '2024-11-18',
        'sitesDict': sitesDict,
        'totals': totals,
        'sitesCollect': sitesCollect,
    }

    # df = pd.read_json(logData)
    # df_csv = df.to_csv()

    # f = open("log" + datetime.today().strftime('%Y-%m-%d') + ".json", "a")
    # f.write(logData)
    # f.close()
    append_to_mongodb(logData)
    # append_json_object('md-review-log.json', logData)
    # print(retrieve_objects_by_date('log.json', '2024-09-11'))

except ValueError:
    # If the response is not JSON or there's an error in conversion, handle it here
    print("Response is not in JSON format.")
    # print(response_json)  # Print raw text response if JSON conversion fails


