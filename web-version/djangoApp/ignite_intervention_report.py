import requests
import urllib.request, urllib.parse
import json
from datetime import datetime, timedelta, date

# import pandas as pd
from datetime import datetime

def fetch_ignite_intervention_report():
    datacall = {
        # 'token': '96EF07A3F74AE278A39C4F7C353937C2',
        'token': '065B39DB545BAA2DB65B224A6279E10A',
        'content': 'record',
        'action': 'export',
        'format': 'json',
        'type': 'flat',
        'csvDelimiter': '',
        'fields[0]': 'record_id',
        'fields[1]': 'randomization_group',
        'fields[2]': 'r1_participant_notified_phone',
        'fields[3]': 'participant_status',
        'fields[4]': 's5_appoint',
        'fields[5]': 's1_date',
        'fields[6]': 's1_appoint',
        'fields[7]': 's2_appoint',
        'fields[8]': 's3_appoint',
        'fields[9]': 's4_appoint',
        'fields[10]': 's6_appoint',
        'fields[11]': 's7_appoint',
        'fields[12]': 's8_appoint',
        'fields[13]': 's9_appoint',
        'fields[14]': 's2_date',
        'fields[15]': 's3_date',
        'fields[16]': 's4_date',
        'fields[17]': 's5_date',
        'fields[18]': 's6_date',
        'fields[19]': 's7_date',
        'fields[20]': 's8_date',
        'fields[21]': 's9_date',
        'fields[22]': 'lumen_administered_phq9_complete',
        'fields[23]': 'active_phase_message_1_complete',
        'fields[24]': 'active_phase_message_2_complete',
        'fields[25]': 'active_phase_message_3_complete',
        'fields[26]': 'active_phase_message_4_complete',
        'fields[27]': 'active_phase_message_5_complete',
        'fields[28]': 'active_phase_message_6_complete',
        'fields[29]': 'active_phase_message_7_complete',
        'fields[30]': 'active_phase_message_8_complete',
        'fields[31]': 'active_phase_message_9_complete',
        'fields[32]': 'active_phase_message_10_complete',
        'fields[33]': 'active_phase_message_11_complete',
        'fields[34]': 'maintenance_phase_message_1_complete',
        'fields[35]': 'maintenance_phase_message_2_complete',
        'fields[36]': 'maintenance_phase_message_3_complete',
        'fields[37]': 'maintenance_phase_message_4_complete',
        'fields[38]': 'maintenance_phase_message_5_complete',
        'fields[39]': 'maintenance_phase_message_6_complete',
        'fields[40]': 'maintenance_phase_message_7_complete',
        'fields[41]': 'maintenance_phase_message_8_complete',
        'fields[42]': 'maintenance_phase_message_9_complete',
        'fields[43]': 'maintenance_phase_message_10_complete',
        'fields[44]': 'evaluation_survey_complete',
        'fields[45]': 'technical_check_survey_complete',
        'fields[46]': 'r2_participant_notified_phone',
        'fields[47]': 'ap1_date',
        'fields[48]': 'date_of_withdrawal',
        'fields[49]': 'zoom_appt_date',
        'fields[50]': 'adhoc_date',
        'fields[51]': 'ad_hoc_completed_session',
        # 'events[0]': 'enroll_arm_1',
        'events[0]': 'baseline_arm_1',
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

    e_rand_notified_by_phn_count = 0
    l_rand_notified_by_phn_count = 0
    l_rand_2_notified_by_phn_count = 0
    e_intervention_withdrawal = 0
    l_study_withdrawal = 0
    e_study_withdrawal = 0
    l_intervention_withdrawal = 0
    e_post_rand_excl = 0
    l_post_rand_excl = 0




    print("Received Data")

    date_today = datetime.today().date()


    ###--------table 1-------------
        # --------------Early v care---------
    for i in response_json:
        group = i.get('randomization_group', '').strip()
        if group == '1':
            if i['r1_participant_notified_phone'] == '1':
                e_rand_notified_by_phn_count += 1

            if i['participant_status'] == '2':
                e_intervention_withdrawal += 1

            if i['participant_status'] == '3':
                e_post_rand_excl += 1

        # --------------Later v care---------
        if group == '2':
            if i['r1_participant_notified_phone'] == '1':
                l_rand_notified_by_phn_count += 1

            if i['r2_participant_notified_phone'] == '1':
                l_rand_2_notified_by_phn_count += 1

            if i['participant_status'] == '2':
                l_intervention_withdrawal += 1

            if i['participant_status'] == '3':
                l_post_rand_excl += 1



    e_total_table_1 = e_rand_notified_by_phn_count + e_intervention_withdrawal + e_post_rand_excl
    l_total_table_1 = l_rand_notified_by_phn_count + l_intervention_withdrawal + l_post_rand_excl + l_rand_2_notified_by_phn_count


    # Initialize counters for early and late message completion groups
    e_apm_msg_1_no_count = 0
    e_apm_msg_2_no_count = 0
    e_apm_msg_3_no_count = 0
    e_apm_msg_4_no_count = 0
    e_apm_msg_5_no_count = 0
    e_apm_msg_6_no_count = 0
    e_apm_msg_7_no_count = 0
    e_apm_msg_8_no_count = 0
    e_apm_msg_9_no_count = 0
    e_apm_msg_10_no_count = 0
    e_apm_msg_11_no_count = 0

    e_apm_msg_1_yes_count = 0
    e_apm_msg_2_yes_count = 0
    e_apm_msg_3_yes_count = 0
    e_apm_msg_4_yes_count = 0
    e_apm_msg_5_yes_count = 0
    e_apm_msg_6_yes_count = 0
    e_apm_msg_7_yes_count = 0
    e_apm_msg_8_yes_count = 0
    e_apm_msg_9_yes_count = 0
    e_apm_msg_10_yes_count = 0
    e_apm_msg_11_yes_count = 0

    e_apm_msg_1_withdrawn_count = 0
    e_apm_msg_2_withdrawn_count = 0
    e_apm_msg_3_withdrawn_count = 0
    e_apm_msg_4_withdrawn_count = 0
    e_apm_msg_5_withdrawn_count = 0
    e_apm_msg_6_withdrawn_count = 0
    e_apm_msg_7_withdrawn_count = 0
    e_apm_msg_8_withdrawn_count = 0
    e_apm_msg_9_withdrawn_count = 0
    e_apm_msg_10_withdrawn_count = 0
    e_apm_msg_11_withdrawn_count = 0

    e_apm_msg_1_ip_count = 0
    e_apm_msg_2_ip_count = 0
    e_apm_msg_3_ip_count = 0
    e_apm_msg_4_ip_count = 0
    e_apm_msg_5_ip_count = 0
    e_apm_msg_6_ip_count = 0
    e_apm_msg_7_ip_count = 0
    e_apm_msg_8_ip_count = 0
    e_apm_msg_9_ip_count = 0
    e_apm_msg_10_ip_count = 0
    e_apm_msg_11_ip_count = 0

    e_apm_msg_1_scheduled_count = 0
    e_apm_msg_2_scheduled_count = 0
    e_apm_msg_3_scheduled_count = 0
    e_apm_msg_4_scheduled_count = 0
    e_apm_msg_5_scheduled_count = 0
    e_apm_msg_6_scheduled_count = 0
    e_apm_msg_7_scheduled_count = 0
    e_apm_msg_8_scheduled_count = 0
    e_apm_msg_9_scheduled_count = 0
    e_apm_msg_10_scheduled_count = 0
    e_apm_msg_11_scheduled_count = 0

    l_apm_msg_1_no_count = 0
    l_apm_msg_2_no_count = 0
    l_apm_msg_3_no_count = 0
    l_apm_msg_4_no_count = 0
    l_apm_msg_5_no_count = 0
    l_apm_msg_6_no_count = 0
    l_apm_msg_7_no_count = 0
    l_apm_msg_8_no_count = 0
    l_apm_msg_9_no_count = 0
    l_apm_msg_10_no_count = 0
    l_apm_msg_11_no_count = 0

    l_apm_msg_1_yes_count = 0
    l_apm_msg_2_yes_count = 0
    l_apm_msg_3_yes_count = 0
    l_apm_msg_4_yes_count = 0
    l_apm_msg_5_yes_count = 0
    l_apm_msg_6_yes_count = 0
    l_apm_msg_7_yes_count = 0
    l_apm_msg_8_yes_count = 0
    l_apm_msg_9_yes_count = 0
    l_apm_msg_10_yes_count = 0
    l_apm_msg_11_yes_count = 0

    l_apm_msg_1_withdrawn_count = 0
    l_apm_msg_2_withdrawn_count = 0
    l_apm_msg_3_withdrawn_count = 0
    l_apm_msg_4_withdrawn_count = 0
    l_apm_msg_5_withdrawn_count = 0
    l_apm_msg_6_withdrawn_count = 0
    l_apm_msg_7_withdrawn_count = 0
    l_apm_msg_8_withdrawn_count = 0
    l_apm_msg_9_withdrawn_count = 0
    l_apm_msg_10_withdrawn_count = 0
    l_apm_msg_11_withdrawn_count = 0

    l_apm_msg_1_ip_count = 0
    l_apm_msg_2_ip_count = 0
    l_apm_msg_3_ip_count = 0
    l_apm_msg_4_ip_count = 0
    l_apm_msg_5_ip_count = 0
    l_apm_msg_6_ip_count = 0
    l_apm_msg_7_ip_count = 0
    l_apm_msg_8_ip_count = 0
    l_apm_msg_9_ip_count = 0
    l_apm_msg_10_ip_count = 0
    l_apm_msg_11_ip_count = 0

    l_apm_msg_1_scheduled_count = 0
    l_apm_msg_2_scheduled_count = 0
    l_apm_msg_3_scheduled_count = 0
    l_apm_msg_4_scheduled_count = 0
    l_apm_msg_5_scheduled_count = 0
    l_apm_msg_6_scheduled_count = 0
    l_apm_msg_7_scheduled_count = 0
    l_apm_msg_8_scheduled_count = 0
    l_apm_msg_9_scheduled_count = 0
    l_apm_msg_10_scheduled_count = 0
    l_apm_msg_11_scheduled_count = 0

    #--------table 2------------
        #-------Early v care Message Completion-----------
    for i in response_json:

        group = i.get('randomization_group', '').strip()
        status = i.get('participant_status', '').strip()
        withdrawn_date = i.get('date_of_withdrawal', '').strip()

        if group == '1':

            #-----checking msg-1--------------
            if 's5_appoint' in i and i['s5_appoint'].strip():

                s5_date = datetime.strptime(i['s5_appoint'], '%Y-%m-%d').date()

                #----for withdrawn participants-----
                if withdrawn_date and s5_date > withdrawn_date:
                    e_apm_msg_1_withdrawn_count += 1

                #----scheduled msgs------
                elif (s5_date - date_today).days > -3 and i.get("active_phase_message_1_complete") != "2":
                    e_apm_msg_1_scheduled_count += 1

                #----for yes msgs-----
                elif (s5_date - date_today).days <= -3 and i.get("active_phase_message_1_complete") == "2":
                    e_apm_msg_1_yes_count += 1

                #----for ip msgs-----
                elif (s5_date - date_today).days <= -3 and i.get("active_phase_message_1_complete") == "1":
                    e_apm_msg_1_ip_count += 1

                #----for no msgs-----
                elif (s5_date - date_today).days <= -3 and i.get("active_phase_message_1_complete") == "0":
                    e_apm_msg_1_no_count += 1

            if i['ap1_date'].strip() and 'ap1_date' in i:
                ap1_date = datetime.strptime(i['ap1_date'], '%Y-%m-%d').date()

                #------check msg - 2--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=7) > withdrawn_date):
                    e_apm_msg_2_withdrawn_count += 1

                #----scheduled msgs------
                elif (ap1_date - date_today).days > -3 and i.get("active_phase_message_2_complete") != "2":
                    e_apm_msg_2_scheduled_count += 1

                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 7 and i.get("active_phase_message_2_complete") == "2":
                    e_apm_msg_2_yes_count += 1

                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 7 and i.get("active_phase_message_2_complete") == "1":
                    e_apm_msg_2_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 7 and i.get("active_phase_message_2_complete") == "0":
                    e_apm_msg_2_no_count += 1

                #------check msg - 3--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=14) > withdrawn_date):
                    e_apm_msg_3_withdrawn_count += 1

                #----scheduled msgs------
                elif (ap1_date - date_today).days > 14 and i.get("active_phase_message_3_complete") != "2":
                    e_apm_msg_3_scheduled_count += 1

                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 14 and i.get("active_phase_message_3_complete") == "2":
                    e_apm_msg_3_yes_count += 1

                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 14 and i.get("active_phase_message_3_complete") == "1":
                    e_apm_msg_3_ip_count += 1

                #----for no msgs-----
                elif (ap1_date - date_today).days <= 14 and i.get("active_phase_message_3_complete") == "0":
                    e_apm_msg_3_no_count += 1

                #------check msg - 4--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=21) > withdrawn_date):
                    e_apm_msg_4_withdrawn_count += 1
                #----scheduled msgs------
                elif (ap1_date - date_today).days > 21 and i.get("active_phase_message_4_complete") != "2":
                    e_apm_msg_4_scheduled_count += 1

                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 21 and i.get("active_phase_message_4_complete") == "2":
                    e_apm_msg_4_yes_count += 1
                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 21 and i.get("active_phase_message_4_complete") == "1":
                    e_apm_msg_4_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 21 and i.get("active_phase_message_4_complete") == "0":
                    e_apm_msg_4_no_count += 1

                #------check msg - 5--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=28) > withdrawn_date):
                    e_apm_msg_5_withdrawn_count += 1
                #----scheduled msgs------
                elif (ap1_date - date_today).days > 28 and i.get("active_phase_message_5_complete") != "2":
                    e_apm_msg_5_scheduled_count += 1

                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 28 and i.get("active_phase_message_5_complete") == "2":
                    e_apm_msg_5_yes_count += 1
                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 28 and i.get("active_phase_message_5_complete") == "1":
                    e_apm_msg_5_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 28 and i.get("active_phase_message_5_complete") == "0":
                    e_apm_msg_5_no_count += 1


                #------check msg - 6--------------
                if withdrawn_date and (ap1_date + timedelta(days=35) > withdrawn_date):
                    e_apm_msg_6_withdrawn_count += 1
                #----scheduled msgs------
                elif (ap1_date - date_today).days > 35 and i.get("active_phase_message_5_complete") != "2":
                    e_apm_msg_6_scheduled_count += 1

                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 35 and i.get("active_phase_message_5_complete") == "2":
                    e_apm_msg_6_yes_count += 1
                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 35 and i.get("active_phase_message_5_complete") == "1":
                    e_apm_msg_6_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 35 and i.get("active_phase_message_5_complete") == "0":
                    e_apm_msg_6_no_count += 1

                #------check msg - 7--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=42) > withdrawn_date):
                    e_apm_msg_7_withdrawn_count += 1
                #----scheduled msgs------
                elif (ap1_date - date_today).days > 42 and i.get("active_phase_message_7_complete") != "2":
                    e_apm_msg_7_scheduled_count += 1
                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 42 and i.get("active_phase_message_7_complete") == "2":
                    e_apm_msg_7_yes_count += 1
                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 42 and i.get("active_phase_message_7_complete") == "1":
                    e_apm_msg_7_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 42 and i.get("active_phase_message_7_complete") == "0":
                    e_apm_msg_7_no_count += 1

                #------check msg - 8--------------
                if withdrawn_date and (ap1_date + timedelta(days=49) > withdrawn_date):
                    e_apm_msg_8_withdrawn_count += 1
                #----scheduled msgs------
                elif (ap1_date - date_today).days > 49 and i.get("active_phase_message_8_complete") != "2":
                    e_apm_msg_8_scheduled_count += 1
                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 49 and i.get("active_phase_message_8_complete") == "2":
                    e_apm_msg_8_yes_count += 1
                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 49 and i.get("active_phase_message_8_complete") == "1":
                    e_apm_msg_8_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 49 and i.get("active_phase_message_8_complete") == "0":
                    e_apm_msg_8_no_count += 1

                #------check msg - 9--------------
                    #-----withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=56) > withdrawn_date):
                    e_apm_msg_9_withdrawn_count += 1
                #----scheduled msgs------
                elif (ap1_date - date_today).days > 56 and i.get("active_phase_message_9_complete") != "2":
                    e_apm_msg_9_scheduled_count += 1
                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 56 and i.get("active_phase_message_9_complete") == "2":
                    e_apm_msg_9_yes_count += 1
                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 56 and i.get("active_phase_message_9_complete") == "1":
                    e_apm_msg_9_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 56 and i.get("active_phase_message_9_complete") == "0":
                    e_apm_msg_9_no_count += 1

                #------check msg - 10--------------
                if withdrawn_date and (ap1_date + timedelta(days=63) > withdrawn_date):
                    e_apm_msg_10_withdrawn_count += 1
                #----scheduled msgs------
                elif (ap1_date - date_today).days > 63 and i.get("active_phase_message_10_complete") != "2":
                    e_apm_msg_10_scheduled_count += 1
                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 63 and i.get("active_phase_message_10_complete") == "2":
                    e_apm_msg_10_yes_count += 1
                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 63 and i.get("active_phase_message_10_complete") == "1":
                    e_apm_msg_10_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 63 and i.get("active_phase_message_10_complete") == "0":
                    e_apm_msg_10_no_count += 1

                #------check msg - 11--------------
                if withdrawn_date and (ap1_date + timedelta(days=70) > withdrawn_date):
                    e_apm_msg_11_withdrawn_count += 1
                #----scheduled msgs------
                elif (ap1_date - date_today).days > 70 and i.get("active_phase_message_11_complete") != "2":
                    e_apm_msg_11_scheduled_count += 1
                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 70 and i.get("active_phase_message_11_complete") == "2":
                    e_apm_msg_11_yes_count += 1
                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 70 and i.get("active_phase_message_11_complete") == "1":
                    e_apm_msg_11_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 70 and i.get("active_phase_message_11_complete") == "0":
                    e_apm_msg_11_no_count += 1

        #--------Late v care Message Completion-----------
        if group == '2':
            #-----checking msg-1--------------
            if 's5_appoint' in i and i['s5_appoint'].strip():

                s5_date = datetime.strptime(i['s5_appoint'], '%Y-%m-%d').date()

                #----for withdrawn participants-----
                if withdrawn_date and s5_date > withdrawn_date:
                    l_apm_msg_1_withdrawn_count += 1
                #----scheduled msgs------
                elif (s5_date - date_today).days > -3 and i.get("active_phase_message_1_complete") != "2":
                    l_apm_msg_1_scheduled_count += 1
                #----for yes msgs-----
                elif (s5_date - date_today).days <= -3 and i.get("active_phase_message_1_complete") == "2":
                    l_apm_msg_1_yes_count += 1

                #----for ip msgs-----
                elif (s5_date - date_today).days <= -3 and i.get("active_phase_message_1_complete") == "1":
                    l_apm_msg_1_ip_count += 1

                #----for no msgs-----
                elif (s5_date - date_today).days <= -3 and i.get("active_phase_message_1_complete") == "0":
                    l_apm_msg_1_no_count += 1

            if i['ap1_date'].strip() and 'ap1_date' in i:
                ap1_date = datetime.strptime(i['ap1_date'], '%Y-%m-%d').date()

                #------check msg - 2--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=7) > withdrawn_date):
                    l_apm_msg_2_withdrawn_count += 1
                #----scheduled msgs------
                elif (ap1_date - date_today).days > 7 and i.get("active_phase_message_2_complete") != "2":
                    l_apm_msg_2_scheduled_count += 1
                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 7 and i.get("active_phase_message_2_complete") == "2":
                    l_apm_msg_2_yes_count += 1

                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 7 and i.get("active_phase_message_2_complete") == "1":
                    l_apm_msg_2_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 7 and i.get("active_phase_message_2_complete") == "0":
                    l_apm_msg_2_no_count += 1

                #------check msg - 3--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=14) > withdrawn_date):
                    l_apm_msg_3_withdrawn_count += 1
                #----scheduled msgs------
                elif (ap1_date - date_today).days > 14 and i.get("active_phase_message_3_complete") != "2":
                    l_apm_msg_3_scheduled_count += 1
                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 14 and i.get("active_phase_message_3_complete") == "2":
                    l_apm_msg_3_yes_count += 1

                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 14 and i.get("active_phase_message_3_complete") == "1":
                    l_apm_msg_3_ip_count += 1

                #----for no msgs-----
                elif (ap1_date - date_today).days <= 14 and i.get("active_phase_message_3_complete") == "0":
                    l_apm_msg_3_no_count += 1

                #------check msg - 4--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=21) > withdrawn_date):
                    l_apm_msg_4_withdrawn_count += 1
                #----scheduled msgs------
                elif (ap1_date - date_today).days > 21 and i.get("active_phase_message_4_complete") != "2":
                    l_apm_msg_4_scheduled_count += 1
                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 21 and i.get("active_phase_message_4_complete") == "2":
                    l_apm_msg_4_yes_count += 1
                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 21 and i.get("active_phase_message_4_complete") == "1":
                    l_apm_msg_4_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 21 and i.get("active_phase_message_4_complete") == "0":
                    l_apm_msg_4_no_count += 1

                #------check msg - 5--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=28) > withdrawn_date):
                    l_apm_msg_5_withdrawn_count += 1
                #----scheduled msgs------
                elif (ap1_date - date_today).days > 28 and i.get("active_phase_message_5_complete") != "2":
                    l_apm_msg_5_scheduled_count += 1
                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 28 and i.get("active_phase_message_5_complete") == "2":
                    l_apm_msg_5_yes_count += 1
                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 28 and i.get("active_phase_message_5_complete") == "1":
                    l_apm_msg_5_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 28 and i.get("active_phase_message_5_complete") == "0":
                    l_apm_msg_5_no_count += 1

                #------check msg - 6--------------
                if withdrawn_date and (ap1_date + timedelta(days=35) > withdrawn_date):
                    l_apm_msg_6_withdrawn_count += 1
                #----scheduled msgs------
                elif (ap1_date - date_today).days > 35 and i.get("active_phase_message_5_complete") != "2":
                    l_apm_msg_6_scheduled_count += 1
                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 35 and i.get("active_phase_message_5_complete") == "2":
                    l_apm_msg_6_yes_count += 1
                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 35 and i.get("active_phase_message_5_complete") == "1":
                    l_apm_msg_6_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 35 and i.get("active_phase_message_5_complete") == "0":
                    l_apm_msg_6_no_count += 1

                #------check msg - 7--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=42) > withdrawn_date):
                    l_apm_msg_7_withdrawn_count += 1
                #----scheduled msgs------
                elif (ap1_date - date_today).days > 42 and i.get("active_phase_message_7_complete") != "2":
                    l_apm_msg_7_scheduled_count += 1
                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 42 and i.get("active_phase_message_7_complete") == "2":
                    l_apm_msg_7_yes_count += 1
                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 42 and i.get("active_phase_message_7_complete") == "1":
                    l_apm_msg_7_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 42 and i.get("active_phase_message_7_complete") == "0":
                    l_apm_msg_7_no_count += 1

                #------check msg - 8--------------
                if withdrawn_date and (ap1_date + timedelta(days=49) > withdrawn_date):
                    l_apm_msg_8_withdrawn_count += 1
                #----scheduled msgs------
                elif (ap1_date - date_today).days > 49 and i.get("active_phase_message_8_complete") != "2":
                    l_apm_msg_8_scheduled_count += 1
                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 49 and i.get("active_phase_message_8_complete") == "2":
                    l_apm_msg_8_yes_count += 1
                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 49 and i.get("active_phase_message_8_complete") == "1":
                    l_apm_msg_8_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 49 and i.get("active_phase_message_8_complete") == "0":
                    l_apm_msg_8_no_count += 1

                #------check msg - 9--------------
                    #-----withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=56) > withdrawn_date):
                    l_apm_msg_9_withdrawn_count += 1
                #----scheduled msgs------
                elif (ap1_date - date_today).days > 56 and i.get("active_phase_message_9_complete") != "2":
                    l_apm_msg_9_scheduled_count += 1
                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 56 and i.get("active_phase_message_9_complete") == "2":
                    l_apm_msg_9_yes_count += 1
                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 56 and i.get("active_phase_message_9_complete") == "1":
                    l_apm_msg_9_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 56 and i.get("active_phase_message_9_complete") == "0":
                    l_apm_msg_9_no_count += 1

                #------check msg - 10--------------
                if withdrawn_date and (ap1_date + timedelta(days=63) > withdrawn_date):
                    l_apm_msg_10_withdrawn_count += 1
                #----scheduled msgs------
                elif (ap1_date - date_today).days > 63 and i.get("active_phase_message_10_complete") != "2":
                    l_apm_msg_10_scheduled_count += 1
                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 63 and i.get("active_phase_message_10_complete") == "2":
                    l_apm_msg_10_yes_count += 1
                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 63 and i.get("active_phase_message_10_complete") == "1":
                    l_apm_msg_10_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 63 and i.get("active_phase_message_10_complete") == "0":
                    l_apm_msg_10_no_count += 1

                #------check msg - 11--------------
                if withdrawn_date and (ap1_date + timedelta(days=70) > withdrawn_date):
                    l_apm_msg_11_withdrawn_count += 1
                #----scheduled msgs------
                elif (ap1_date - date_today).days > 70 and i.get("active_phase_message_11_complete") != "2":
                    l_apm_msg_11_scheduled_count += 1
                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 70 and i.get("active_phase_message_11_complete") == "2":
                    l_apm_msg_11_yes_count += 1
                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 70 and i.get("active_phase_message_11_complete") == "1":
                    l_apm_msg_11_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 70 and i.get("active_phase_message_11_complete") == "0":
                    l_apm_msg_11_no_count += 1


    e_mpm_msg_1_withdrawn_count = 0
    e_mpm_msg_2_withdrawn_count = 0
    e_mpm_msg_3_withdrawn_count = 0
    e_mpm_msg_4_withdrawn_count = 0
    e_mpm_msg_5_withdrawn_count = 0
    e_mpm_msg_6_withdrawn_count = 0
    e_mpm_msg_7_withdrawn_count = 0
    e_mpm_msg_8_withdrawn_count = 0
    e_mpm_msg_9_withdrawn_count = 0
    e_mpm_msg_10_withdrawn_count = 0
    e_mpm_msg_11_withdrawn_count = 0

    e_mpm_msg_1_no_count = 0
    e_mpm_msg_2_no_count = 0
    e_mpm_msg_3_no_count = 0
    e_mpm_msg_4_no_count = 0
    e_mpm_msg_5_no_count = 0
    e_mpm_msg_6_no_count = 0
    e_mpm_msg_7_no_count = 0
    e_mpm_msg_8_no_count = 0
    e_mpm_msg_9_no_count = 0
    e_mpm_msg_10_no_count = 0
    e_mpm_msg_11_no_count = 0

    e_mpm_msg_1_yes_count = 0
    e_mpm_msg_2_yes_count = 0
    e_mpm_msg_3_yes_count = 0
    e_mpm_msg_4_yes_count = 0
    e_mpm_msg_5_yes_count = 0
    e_mpm_msg_6_yes_count = 0
    e_mpm_msg_7_yes_count = 0
    e_mpm_msg_8_yes_count = 0
    e_mpm_msg_9_yes_count = 0
    e_mpm_msg_10_yes_count = 0
    e_mpm_msg_11_yes_count = 0

    e_mpm_msg_1_ip_count = 0
    e_mpm_msg_2_ip_count = 0
    e_mpm_msg_3_ip_count = 0
    e_mpm_msg_4_ip_count = 0
    e_mpm_msg_5_ip_count = 0
    e_mpm_msg_6_ip_count = 0
    e_mpm_msg_7_ip_count = 0
    e_mpm_msg_8_ip_count = 0
    e_mpm_msg_9_ip_count = 0
    e_mpm_msg_10_ip_count = 0
    e_mpm_msg_11_ip_count = 0

    e_mpm_msg_1_scheduled_count = 0
    e_mpm_msg_2_scheduled_count = 0
    e_mpm_msg_3_scheduled_count = 0
    e_mpm_msg_4_scheduled_count = 0
    e_mpm_msg_5_scheduled_count = 0
    e_mpm_msg_6_scheduled_count = 0
    e_mpm_msg_7_scheduled_count = 0
    e_mpm_msg_8_scheduled_count = 0
    e_mpm_msg_9_scheduled_count = 0
    e_mpm_msg_10_scheduled_count = 0
    e_mpm_msg_11_scheduled_count = 0

    #--------table 2------------
        #-------Early v care Message Completion Maintainence Phase message-----------
    for i in response_json:

        group = i.get('randomization_group', '').strip()
        status = i.get('participant_status', '').strip()
        withdrawn_date = i.get('date_of_withdrawal', '').strip()

        if group == '1':

            #-----checking msg-1--------------
            if 'ap1_date' in i and i['ap1_date'].strip():

                ap1_date = datetime.strptime(i['ap1_date'], '%Y-%m-%d').date()

                #----for withdrawn participants-----
                if withdrawn_date and ap1_date + 84 > withdrawn_date:
                    e_mpm_msg_1_withdrawn_count += 1

                #----scheduled msgs------
                elif (ap1_date - date_today).days > 84 and i.get("maintenance_phase_message_1_complete") != "2":
                    e_mpm_msg_1_scheduled_count += 1
                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 84 and i.get("maintenance_phase_message_1_complete") == "2":
                    e_mpm_msg_1_yes_count += 1

                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 84 and i.get("maintenance_phase_message_1_complete") == "1":
                    e_mpm_msg_1_ip_count += 1

                #----for no msgs-----
                elif (ap1_date - date_today).days <= 84 and i.get("maintenance_phase_message_1_complete") == "0":
                    e_mpm_msg_1_no_count += 1

                #------check msg - 2--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=98) > withdrawn_date):
                    e_mpm_msg_2_withdrawn_count += 1
                #----scheduled msgs------
                elif (ap1_date - date_today).days > 98 and i.get("maintenance_phase_message_2_complete") != "2":
                    e_mpm_msg_2_scheduled_count += 1

                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 98 and i.get("maintenance_phase_message_2_complete") == "2":
                    e_mpm_msg_2_yes_count += 1

                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 98 and i.get("maintenance_phase_message_2_complete") == "1":
                    e_mpm_msg_2_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 98 and i.get("maintenance_phase_message_2_complete") == "0":
                    e_mpm_msg_2_no_count += 1

                #------check msg - 3--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=112) > withdrawn_date):
                    e_mpm_msg_3_withdrawn_count += 1
                #----for scheduled msgs------
                elif (ap1_date - date_today).days > 112 and i.get("maintenance_phase_message_3_complete") != "2":
                    e_mpm_msg_3_scheduled_count += 1

                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 112 and i.get("maintenance_phase_message_3_complete") == "2":
                    e_mpm_msg_3_yes_count += 1

                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 112 and i.get("maintenance_phase_message_3_complete") == "1":
                    e_mpm_msg_3_ip_count += 1

                #----for no msgs-----
                elif (ap1_date - date_today).days <= 112 and i.get("maintenance_phase_message_3_complete") == "0":
                    e_mpm_msg_3_no_count += 1

                #------check msg - 4--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=140) > withdrawn_date):
                    e_mpm_msg_4_withdrawn_count += 1
                #----for scheduled msgs------
                elif (ap1_date - date_today).days > 140 and i.get("maintenance_phase_message_4_complete") != "2":
                    e_mpm_msg_4_scheduled_count += 1

                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 140 and i.get("maintenance_phase_message_4_complete") == "2":
                    e_mpm_msg_4_yes_count += 1
                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 140 and i.get("maintenance_phase_message_4_complete") == "1":
                    e_mpm_msg_4_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 140 and i.get("maintenance_phase_message_4_complete") == "0":
                    e_mpm_msg_4_no_count += 1

                #------check msg - 5--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=168) > withdrawn_date):
                    e_mpm_msg_5_withdrawn_count += 1
                #----for scheduled msgs------
                elif (ap1_date - date_today).days > 168 and i.get("maintenance_phase_message_5_complete") != "2":
                    e_mpm_msg_5_scheduled_count += 1

                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 168 and i.get("maintenance_phase_message_5_complete") == "2":
                    e_mpm_msg_5_yes_count += 1
                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 168 and i.get("maintenance_phase_message_5_complete") == "1":
                    e_mpm_msg_5_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 168 and i.get("maintenance_phase_message_5_complete") == "0":
                    e_mpm_msg_5_no_count += 1

                #------check msg - 6--------------
                if withdrawn_date and (ap1_date + timedelta(days=196) > withdrawn_date):
                    e_mpm_msg_6_withdrawn_count += 1
                #----for scheduled msgs------
                elif (ap1_date - date_today).days > 196 and i.get("maintenance_phase_message_6_complete") != "2":
                    e_mpm_msg_6_scheduled_count += 1
                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 196 and i.get("maintenance_phase_message_6_complete") == "2":
                    e_mpm_msg_6_yes_count += 1
                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 196 and i.get("maintenance_phase_message_6_complete") == "1":
                    e_mpm_msg_6_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 196 and i.get("maintenance_phase_message_6_complete") == "0":
                    e_mpm_msg_6_no_count += 1

                #------check msg - 7--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=224) > withdrawn_date):
                    e_mpm_msg_7_withdrawn_count += 1
                #----for scheduled msgs------
                elif (ap1_date - date_today).days > 224 and i.get("maintenance_phase_message_7_complete") != "2":
                    e_mpm_msg_7_scheduled_count += 1
                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 224 and i.get("maintenance_phase_message_7_complete") == "2":
                    e_mpm_msg_7_yes_count += 1
                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 224 and i.get("maintenance_phase_message_7_complete") == "1":
                    e_mpm_msg_7_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 224 and i.get("maintenance_phase_message_7_complete") == "0":
                    e_mpm_msg_7_no_count += 1

                #------check msg - 8--------------
                if withdrawn_date and (ap1_date + timedelta(days=252) > withdrawn_date):
                    e_mpm_msg_8_withdrawn_count += 1
                #----for scheduled msgs------
                elif (ap1_date - date_today).days > 252 and i.get("maintenance_phase_message_8_complete") != "2":
                    e_mpm_msg_8_scheduled_count += 1
                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 252 and i.get("maintenance_phase_message_8_complete") == "2":
                    e_mpm_msg_8_yes_count += 1
                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 252 and i.get("maintenance_phase_message_8_complete") == "1":
                    e_mpm_msg_8_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 252 and i.get("maintenance_phase_message_8_complete") == "0":
                    e_mpm_msg_8_no_count += 1

                #------check msg - 9--------------
                    #-----withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=280) > withdrawn_date):
                    e_mpm_msg_9_withdrawn_count += 1
                #----scheduled msgs------
                elif (ap1_date - date_today).days > 280 and i.get("maintenance_phase_message_9_complete") != "2":
                    e_mpm_msg_9_scheduled_count += 1
                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 280 and i.get("maintenance_phase_message_9_complete") == "2":
                    e_mpm_msg_9_yes_count += 1
                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 280 and i.get("maintenance_phase_message_9_complete") == "1":
                    e_mpm_msg_9_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 280 and i.get("maintenance_phase_message_9_complete") == "0":
                    e_mpm_msg_9_no_count += 1

                #------check msg - 10--------------
                if withdrawn_date and (ap1_date + timedelta(days=308) > withdrawn_date):
                    e_mpm_msg_10_withdrawn_count += 1
                #----for scheduled msgs------
                elif (ap1_date - date_today).days > 308 and i.get("maintenance_phase_message_10_complete") != "2":
                    e_mpm_msg_10_scheduled_count += 1
                #----for yes msgs-----
                elif (ap1_date - date_today).days <= 308 and i.get("maintenance_phase_message_11_complete") == "2":
                    e_mpm_msg_10_yes_count += 1
                #----for ip msgs-----
                elif (ap1_date - date_today).days <= 308 and i.get("maintenance_phase_message_11_complete") == "1":
                    e_mpm_msg_10_ip_count += 1
                #----for no msgs-----
                elif (ap1_date - date_today).days <= 308 and i.get("maintenance_phase_message_11_complete") == "0":
                    e_mpm_msg_10_no_count += 1



    e_session_1_pending_count = 0
    e_session_2_pending_count = 0
    e_session_3_pending_count = 0
    e_session_4_pending_count = 0
    e_session_5_pending_count = 0
    e_session_6_pending_count = 0
    e_session_7_pending_count = 0
    e_session_8_pending_count = 0
    e_session_9_pending_count = 0

    e_session_1_missed_count = 0
    e_session_2_missed_count = 0
    e_session_3_missed_count = 0
    e_session_4_missed_count = 0
    e_session_5_missed_count = 0
    e_session_6_missed_count = 0
    e_session_7_missed_count = 0
    e_session_8_missed_count = 0
    e_session_9_missed_count = 0

    e_session_1_completed_count = 0
    e_session_2_completed_count = 0
    e_session_3_completed_count = 0
    e_session_4_completed_count = 0
    e_session_5_completed_count = 0
    e_session_6_completed_count = 0
    e_session_7_completed_count = 0
    e_session_8_completed_count = 0
    e_session_9_completed_count = 0

    e_session_1_withdrawn_count = 0
    e_session_2_withdrawn_count = 0
    e_session_3_withdrawn_count = 0
    e_session_4_withdrawn_count = 0
    e_session_5_withdrawn_count = 0
    e_session_6_withdrawn_count = 0
    e_session_7_withdrawn_count = 0
    e_session_8_withdrawn_count = 0
    e_session_9_withdrawn_count = 0

    e_session_1_scheduled_count = 0
    e_session_2_scheduled_count = 0
    e_session_3_scheduled_count = 0
    e_session_4_scheduled_count = 0
    e_session_5_scheduled_count = 0
    e_session_6_scheduled_count = 0
    e_session_7_scheduled_count = 0
    e_session_8_scheduled_count = 0
    e_session_9_scheduled_count = 0

    l_session_1_scheduled_count = 0
    l_session_2_scheduled_count = 0
    l_session_3_scheduled_count = 0
    l_session_4_scheduled_count = 0
    l_session_5_scheduled_count = 0
    l_session_6_scheduled_count = 0
    l_session_7_scheduled_count = 0
    l_session_8_scheduled_count = 0
    l_session_9_scheduled_count = 0

    l_session_1_pending_count = 0
    l_session_2_pending_count = 0
    l_session_3_pending_count = 0
    l_session_4_pending_count = 0
    l_session_5_pending_count = 0
    l_session_6_pending_count = 0
    l_session_7_pending_count = 0
    l_session_8_pending_count = 0
    l_session_9_pending_count = 0

    l_session_1_missed_count = 0
    l_session_2_missed_count = 0
    l_session_3_missed_count = 0
    l_session_4_missed_count = 0
    l_session_5_missed_count = 0
    l_session_6_missed_count = 0
    l_session_7_missed_count = 0
    l_session_8_missed_count = 0
    l_session_9_missed_count = 0

    l_session_1_completed_count = 0
    l_session_2_completed_count = 0
    l_session_3_completed_count = 0
    l_session_4_completed_count = 0
    l_session_5_completed_count = 0
    l_session_6_completed_count = 0
    l_session_7_completed_count = 0
    l_session_8_completed_count = 0
    l_session_9_completed_count = 0

    l_session_1_withdrawn_count = 0
    l_session_2_withdrawn_count = 0
    l_session_3_withdrawn_count = 0
    l_session_4_withdrawn_count = 0
    l_session_5_withdrawn_count = 0
    l_session_6_withdrawn_count = 0
    l_session_7_withdrawn_count = 0
    l_session_8_withdrawn_count = 0
    l_session_9_withdrawn_count = 0


    #------table - 3---------
        #-------Early vCare Counseling Session-------
    for i in response_json:
        group = i.get('randomization_group', '').strip()
        status = i.get('participant_status', '').strip()
        withdrawn_date = i.get('date_of_withdrawal', '').strip()

        if group == '1':
            #-----checking session-1(human)--------------
            if 'zoom_appt_date' in i and i['zoom_appt_date'].strip():
                zoom_appt_date = datetime.strptime(i['zoom_appt_date'], '%Y-%m-%d').date()
                s1_date = datetime.strptime(i['s1_date'], '%Y-%m-%d').date() if i.get('s1_') else None

                #----for withdrawn participants-----
                if withdrawn_date and zoom_appt_date > withdrawn_date:
                    e_session_1_withdrawn_count += 1
                #----scheduled sessions------
                elif (zoom_appt_date - date_today).days > 0 and s1_date is None:
                    e_session_1_scheduled_count += 1

                elif s1_date:
                    e_session_1_completed_count += 1

                elif zoom_appt_date < date_today and s1_date is None:
                    e_session_1_missed_count += 1

                elif zoom_appt_date > date_today and s1_date is None:
                    e_session_1_pending_count += 1

            #-----checking session-2--------------
            if 's2_appoint' in i and i['s2_appoint'].strip():
                s2_appoint = datetime.strptime(i['s2_appoint'], '%Y-%m-%d').date()
                s2_date = datetime.strptime(i['s2_date'], '%Y-%m-%d').date() if i.get('s2_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and s2_appoint > withdrawn_date:
                    e_session_2_withdrawn_count += 1
                #----scheduled sessions------
                elif (s2_appoint - date_today).days > 0 and s2_date is None:
                    e_session_2_scheduled_count += 1
                elif s2_date:
                    e_session_2_completed_count += 1

                elif s2_appoint < date_today and s2_date is None:
                    e_session_2_missed_count += 1

                elif s2_appoint > date_today and s2_date is None:
                    e_session_2_pending_count += 1

            #------checking session-3--------------
            if 's3_appoint' in i and i['s3_appoint'].strip():
                s3_appoint = datetime.strptime(i['s3_appoint'], '%Y-%m-%d').date()
                s3_date = datetime.strptime(i['s3_date'], '%Y-%m-%d').date() if i.get('s3_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and s3_appoint > withdrawn_date:
                    e_session_3_withdrawn_count += 1
                #----scheduled sessions------
                elif (s3_appoint - date_today).days > 0 and s3_date is None:
                    e_session_3_scheduled_count += 1
                elif s3_date:
                    e_session_3_completed_count += 1

                elif s3_appoint < date_today and s3_date is None:
                    e_session_3_missed_count += 1

                elif s3_appoint > date_today and s3_date is None:
                    e_session_3_pending_count += 1

            #------checking session-4--------------
            if 's4_appoint' in i and i['s4_appoint'].strip():
                s4_appoint = datetime.strptime(i['s4_appoint'], '%Y-%m-%d').date()
                s4_date = datetime.strptime(i['s4_date'], '%Y-%m-%d').date() if i.get('s4_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and s4_appoint > withdrawn_date:
                    e_session_4_withdrawn_count += 1
                #----scheduled sessions------
                elif (s4_appoint - date_today).days > 0 and s4_date is None:
                    e_session_4_scheduled_count += 1
                elif s4_date:
                    e_session_4_completed_count += 1

                elif s4_appoint < date_today and s4_date is None:
                    e_session_4_missed_count += 1

                elif s4_appoint > date_today and s4_date is None:
                    e_session_4_pending_count += 1

            #------checking session-5--------------
            if 's5_appoint' in i and i['s5_appoint'].strip():
                s5_appoint = datetime.strptime(i['s5_appoint'], '%Y-%m-%d').date()
                s5_date = datetime.strptime(i['s5_date'], '%Y-%m-%d').date() if i.get('s5_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and s5_appoint > withdrawn_date:
                    e_session_5_withdrawn_count += 1
                #----scheduled sessions------
                elif (s5_appoint - date_today).days > 0 and s5_date is None:
                    e_session_5_scheduled_count += 1
                elif s5_date:
                    e_session_5_completed_count += 1

                elif s5_appoint < date_today and s5_date is None:
                    e_session_5_missed_count += 1

                elif s5_appoint > date_today and s5_date is None:
                    e_session_5_pending_count += 1

            #--------checking session-6-----------
            if 's6_appoint' in i and i['s6_appoint'].strip():
                s6_appoint = datetime.strptime(i['s6_appoint'], '%Y-%m-%d').date()
                s6_date = datetime.strptime(i['s6_date'], '%Y-%m-%d').date() if i.get('s6_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and s6_appoint > withdrawn_date:
                    e_session_6_withdrawn_count += 1
                #----scheduled sessions------
                elif (s6_appoint - date_today).days > 0 and s6_date is None:
                    e_session_6_scheduled_count += 1

                elif s6_date:
                    e_session_6_completed_count += 1

                elif s6_appoint < date_today and s6_date is None:
                    e_session_6_missed_count += 1

                elif s6_appoint > date_today and s6_date is None:
                    e_session_6_pending_count += 1

            #--------checking session-7-------
            if 's7_appoint' in i and i['s7_appoint'].strip():
                s7_appoint = datetime.strptime(i['s7_appoint'], '%Y-%m-%d').date()
                s7_date = datetime.strptime(i['s7_date'], '%Y-%m-%d').date() if i.get('s7_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and s7_appoint > withdrawn_date:
                    e_session_7_withdrawn_count += 1
                #----scheduled sessions------
                elif (s7_appoint - date_today).days > 0 and s7_date is None:
                    e_session_7_scheduled_count += 1
                elif s7_date:
                    e_session_7_completed_count += 1

                elif s7_appoint < date_today and s7_date is None:
                    e_session_7_missed_count += 1

                elif s7_appoint > date_today and s7_date is None:
                    e_session_7_pending_count += 1

            #--------checking session-8-------
            if 's_appoint' in i and i['s8_appoint'].strip():
                s8_appoint = datetime.strptime(i['s8_appoint'], '%Y-%m-%d').date()
                s8_date = datetime.strptime(i['s8_date'], '%Y-%m-%d').date() if i.get('s8_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and s8_appoint > withdrawn_date:
                    e_session_8_withdrawn_count += 1
                #----scheduled sessions------
                elif (s8_appoint - date_today).days > 0 and s8_date is None:
                    e_session_8_scheduled_count += 1

                elif s8_date:
                    e_session_8_completed_count += 1

                elif s8_appoint < date_today and s8_date is None:
                    e_session_8_missed_count += 1

                elif s8_appoint > date_today and s8_date is None:
                    e_session_8_pending_count += 1

            #--------checking session-9-------
            if 's9_appoint' in i and i['s9_appoint'].strip():
                s9_appoint = datetime.strptime(i['s9_appoint'], '%Y-%m-%d').date()
                s9_date = datetime.strptime(i['s9_date'], '%Y-%m-%d').date() if i.get('s9_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and s9_appoint > withdrawn_date:
                    e_session_9_withdrawn_count += 1
                #----scheduled sessions------
                elif (s9_appoint - date_today).days > 0 and s9_date is None:
                    e_session_9_scheduled_count += 1

                elif s9_date:
                    e_session_9_completed_count += 1

                elif s9_appoint < date_today and s9_date is None:
                    e_session_9_missed_count += 1

                elif s9_appoint > date_today and s9_date is None:
                    e_session_9_pending_count += 1

        #-------Later vCare Counseling Session-------

        elif group == '2':
            #-----checking session-1(human)--------------
            if 'zoom_appt_date' in i and i['zoom_appt_date'].strip():
                zoom_appt_date = datetime.strptime(i['zoom_appt_date'], '%Y-%m-%d').date()
                s1_date = datetime.strptime(i['s1_date'], '%Y-%m-%d').date() if i.get('s1_') else None

                #----for withdrawn participants-----
                if withdrawn_date and zoom_appt_date > withdrawn_date:
                    l_session_1_withdrawn_count += 1
                #----scheduled sessions------
                elif (zoom_appt_date - date_today).days > 0 and s1_date is None:
                    l_session_1_scheduled_count += 1

                elif s1_date:
                    l_session_1_completed_count += 1

                elif zoom_appt_date < date_today and s1_date is None:
                    l_session_1_missed_count += 1

                elif zoom_appt_date > date_today and s1_date is None:
                    l_session_1_pending_count += 1

            #-----checking session-2--------------
            if 's2_appoint' in i and i['s2_appoint'].strip():
                s2_appoint = datetime.strptime(i['s2_appoint'], '%Y-%m-%d').date()
                s2_date = datetime.strptime(i['s2_date'], '%Y-%m-%d').date() if i.get('s2_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and zoom_appt_date > withdrawn_date:
                    l_session_2_withdrawn_count += 1
                #----scheduled sessions------
                elif (s2_appoint - date_today).days > 0 and s2_date is None:
                    l_session_2_scheduled_count += 1

                elif s2_date:
                    l_session_2_completed_count += 1

                elif zoom_appt_date < date_today and s1_date is None:
                    l_session_2_missed_count += 1

                elif zoom_appt_date > date_today and s1_date is None:
                    l_session_2_pending_count += 1

            #------checking session-3--------------
            if 's3_appoint' in i and i['s3_appoint'].strip():
                s3_appoint = datetime.strptime(i['s3_appoint'], '%Y-%m-%d').date()
                s3_date = datetime.strptime(i['s3_date'], '%Y-%m-%d').date() if i.get('s3_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and zoom_appt_date > withdrawn_date:
                    l_session_3_withdrawn_count += 1
                #----scheduled sessions------
                elif (s3_appoint - date_today).days > 0 and s3_date is None:
                    l_session_3_scheduled_count += 1

                elif s3_date:
                    l_session_3_completed_count += 1

                elif zoom_appt_date < date_today and s1_date is None:
                    l_session_3_missed_count += 1

                elif zoom_appt_date > date_today and s1_date is None:
                    l_session_3_pending_count += 1

            #------checking session-4--------------
            if 's4_appoint' in i and i['s4_appoint'].strip():
                s4_appoint = datetime.strptime(i['s4_appoint'], '%Y-%m-%d').date()
                s4_date = datetime.strptime(i['s4_date'], '%Y-%m-%d').date() if i.get('s4_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and zoom_appt_date > withdrawn_date:
                    l_session_4_withdrawn_count += 1
                #----scheduled sessions------
                elif (s4_appoint - date_today).days > 0 and s4_date is None:
                    l_session_4_scheduled_count += 1
                elif s4_date:
                    l_session_4_completed_count += 1

                elif zoom_appt_date < date_today and s1_date is None:
                    l_session_4_missed_count += 1

                elif zoom_appt_date > date_today and s1_date is None:
                    l_session_4_pending_count += 1

            #------checking session-5--------------
            if 's5_appoint' in i and i['s5_appoint'].strip():
                s5_appoint = datetime.strptime(i['s5_appoint'], '%Y-%m-%d').date()
                s5_date = datetime.strptime(i['s5_date'], '%Y-%m-%d').date() if i.get('s5_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and zoom_appt_date > withdrawn_date:
                    l_session_5_withdrawn_count += 1
                #----scheduled sessions------
                elif (s5_appoint - date_today).days > 0 and s5_date is None:
                    l_session_5_scheduled_count += 1
                elif s5_date:
                    l_session_5_completed_count += 1

                elif zoom_appt_date < date_today and s1_date is None:
                    l_session_5_missed_count += 1

                elif zoom_appt_date > date_today and s1_date is None:
                    l_session_5_pending_count += 1

            #--------checking session-6
            if 's6_appoint' in i and i['s6_appoint'].strip():
                s6_appoint = datetime.strptime(i['s6_appoint'], '%Y-%m-%d').date()
                s6_date = datetime.strptime(i['s6_date'], '%Y-%m-%d').date() if i.get('s6_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and zoom_appt_date > withdrawn_date:
                    l_session_6_withdrawn_count += 1
                #----scheduled sessions------
                elif (s6_appoint - date_today).days > 0 and s6_date is None:
                    l_session_6_scheduled_count += 1

                elif s6_date:
                    l_session_6_completed_count += 1

                elif zoom_appt_date < date_today and s1_date is None:
                    l_session_6_missed_count += 1

                elif zoom_appt_date > date_today and s1_date is None:
                    l_session_6_pending_count += 1

            #--------checking session-7-------
            if 's7_appoint' in i and i['s7_appoint'].strip():
                s7_appoint = datetime.strptime(i['s7_appoint'], '%Y-%m-%d').date()
                s7_date = datetime.strptime(i['s7_date'], '%Y-%m-%d').date() if i.get('s7_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and zoom_appt_date > withdrawn_date:
                    l_session_7_withdrawn_count += 1
                #----scheduled sessions------
                elif (s7_appoint - date_today).days > 0 and s7_date is None:
                    l_session_7_scheduled_count += 1
                elif s7_date:
                    l_session_7_completed_count += 1

                elif zoom_appt_date < date_today and s1_date is None:
                    l_session_7_missed_count += 1

                elif zoom_appt_date > date_today and s1_date is None:
                    l_session_7_pending_count += 1

            #--------checking session-8-------
            if 's8_appoint' in i and i['s8_appoint'].strip():
                s8_appoint = datetime.strptime(i['s8_appoint'], '%Y-%m-%d').date()
                s8_date = datetime.strptime(i['s8_date'], '%Y-%m-%d').date() if i.get('s8_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and zoom_appt_date > withdrawn_date:
                    l_session_8_withdrawn_count += 1
                #----scheduled sessions------
                elif (s8_appoint - date_today).days > 0 and s8_date is None:
                    l_session_8_scheduled_count += 1

                elif s8_date:
                    l_session_8_completed_count += 1

                elif zoom_appt_date < date_today and s1_date is None:
                    l_session_8_missed_count += 1

                elif zoom_appt_date > date_today and s1_date is None:
                    l_session_8_pending_count += 1

            #--------checking session-9-------
            if 's9_appoint' in i and i['s9_appoint'].strip():
                s9_appoint = datetime.strptime(i['s9_appoint'], '%Y-%m-%d').date()
                s9_date = datetime.strptime(i['s9_date'], '%Y-%m-%d').date() if i.get('s9_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and zoom_appt_date > withdrawn_date:
                    l_session_9_withdrawn_count += 1
                #----scheduled sessions------
                elif (s9_appoint - date_today).days > 0 and s9_date is None:
                    l_session_9_scheduled_count += 1
                elif s9_date:
                    l_session_9_completed_count += 1

                elif zoom_appt_date < date_today and s1_date is None:
                    l_session_9_missed_count += 1

                elif zoom_appt_date > date_today and s1_date is None:
                    l_session_9_pending_count += 1



    # Additional Survey Variables
    tech_check_scheduled = 0
    tech_check_completed = 0
    tech_check_not_yet_due = 0
    tech_check_overdue = 0
    tech_check_withdrawals = 0
    eval_scheduled = 0
    eval_completed = 0
    eval_not_yet_due = 0
    eval_overdue = 0
    eval_withdrawals = 0
    on_demand_scheduled = 0
    on_demand_completed = 0
    on_demand_withdrawals = 0

    #--------Additional Surveys--------
    for i in response_json:
        # Get the date of withdrawal if it exists
        withdrawn_date = i.get('date_of_withdrawal', '').strip()
    #-----------tech check survey -----------
        #  Withdrawals (any record with participant_status == '3') // what if withdraw after session 2? this goes out after 3 days right?
        if i['participant_status'] == '3' and datetime.strptime(i["s2_date"], "%Y-%m-%d").date() > withdrawn_date and i['technical_check_survey_complete'] != '2':
            tech_check_withdrawals += 1

        #  Scheduled
        if (
            i.get("technical_check_survey_complete") != '2'
            and i.get("s2_date")  # makes sure key exists and is not empty/None
            and i["s2_date"].strip()  # makes sure it's not just whitespace
        ):
            s2_date_obj = datetime.strptime(i["s2_date"], "%Y-%m-%d").date()
            if (s2_date_obj - date_today).days == 3:
                tech_check_scheduled += 1

            tech_check_scheduled += 1

        #  Completed
        elif i['technical_check_survey_complete'] == '2':
            tech_check_completed += 1

        # Not yet due
        elif (
            i.get('technical_check_survey_complete') != '2'
            and i.get("s2_date", "").strip() != ""
            and (datetime.strptime(i["s2_date"], "%Y-%m-%d").date() - date_today).days > 3
        ):

            tech_check_not_yet_due += 1

        # Overdue
        elif (
            i.get('technical_check_survey_complete') != '2'
            and i.get("s2_date", "").strip() != ""
            and (datetime.strptime(i["s2_date"], "%Y-%m-%d").date() - date_today).days <= 0
        ):
            tech_check_overdue += 1

        #--------valuation survey-------------
        if i['participant_status'] == '3' and datetime.strptime(i["s9_date"], "%Y-%m-%d").date() > withdrawn_date and i['evaluation_survey_complete'] != '2':
            eval_withdrawals += 1

        #  Scheduled
        if i['technical_check_survey_complete'] != '2' and i.get("s2_date") and i["s2_date"].strip():
            s2_date_obj = datetime.strptime(i["s2_date"], "%Y-%m-%d").date()
            if (s2_date_obj - date.today()).days == 3:
                eval_scheduled += 1

        #  Completed
        elif i['evaluation_survey_complete'] == '2':
            eval_completed += 1

        # Not yet due
        elif (
            i.get('technical_check_survey_complete') != '2'
            and i.get("s2_date", "").strip() != ""
            and (datetime.strptime(i["s2_date"], "%Y-%m-%d").date() - date_today).days > 3
        ):
            eval_not_yet_due += 1

        # Overdue
        elif (
            i.get('technical_check_survey_complete') != '2'
            and i.get("s2_date", "").strip() != ""
            and (datetime.strptime(i["s2_date"], "%Y-%m-%d").date() - date_today).days <= 0
        ):
            eval_overdue += 1

        #--------on demand session-------------
        if i['participant_status'] == '3':
            on_demand_withdrawals += 1

        elif i.get('adhoc_date') and i.get('ad_hoc_completed_session'):
            on_demand_completed += 1

    #----------new data call for phq-9 values for including event data----------
    datacall1 = {
        'token': '065B39DB545BAA2DB65B224A6279E10A',
        'content': 'record',
        'action': 'export',
        'format': 'json',
        'type': 'flat',
        'csvDelimiter': '',
        # 'records[0]': '1',
        # 'records[1]': '2',
        'fields[0]': 'record_id',
        'fields[1]': 'randomization_group',
        'fields[2]': 'r1_date',
        'fields[3]': 'zoom_appt_date',
        'fields[4]': 's2_appoint',
        'fields[5]': 's3_appoint',
        'fields[6]': 's4_appoint',
        'fields[7]': 's5_appoint',
        'fields[8]': 's6_appoint',
        'fields[9]': 's7_appoint',
        'fields[10]': 's8_appoint',
        'fields[11]': 's9_appoint',
        'fields[12]': 'lumen_administered_phq9_complete',
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

    e_phq9_completed_s1_count = 0
    e_phq9_completed_s2_count = 0
    e_phq9_completed_s3_count = 0
    e_phq9_completed_s4_count = 0
    e_phq9_completed_s5_count = 0
    e_phq9_completed_s6_count = 0
    e_phq9_completed_s7_count = 0
    e_phq9_completed_s8_count = 0
    e_phq9_completed_s9_count = 0

    e_phq9_expected_s1_count = 0
    e_phq9_expected_s2_count = 0
    e_phq9_expected_s3_count = 0
    e_phq9_expected_s4_count = 0
    e_phq9_expected_s5_count = 0
    e_phq9_expected_s6_count = 0
    e_phq9_expected_s7_count = 0
    e_phq9_expected_s8_count = 0
    e_phq9_expected_s9_count = 0

    e_phq9_overdue_s1_count = 0
    e_phq9_overdue_s2_count = 0
    e_phq9_overdue_s3_count = 0
    e_phq9_overdue_s4_count = 0
    e_phq9_overdue_s5_count = 0
    e_phq9_overdue_s6_count = 0
    e_phq9_overdue_s7_count = 0
    e_phq9_overdue_s8_count = 0
    e_phq9_overdue_s9_count = 0

    l_phq9_completed_s1_count = 0
    l_phq9_completed_s2_count = 0
    l_phq9_completed_s3_count = 0
    l_phq9_completed_s4_count = 0
    l_phq9_completed_s5_count = 0
    l_phq9_completed_s6_count = 0
    l_phq9_completed_s7_count = 0
    l_phq9_completed_s8_count = 0
    l_phq9_completed_s9_count = 0

    l_phq9_expected_s1_count = 0
    l_phq9_expected_s2_count = 0
    l_phq9_expected_s3_count = 0
    l_phq9_expected_s4_count = 0
    l_phq9_expected_s5_count = 0
    l_phq9_expected_s6_count = 0
    l_phq9_expected_s7_count = 0
    l_phq9_expected_s8_count = 0
    l_phq9_expected_s9_count = 0

    l_phq9_overdue_s1_count = 0
    l_phq9_overdue_s2_count = 0
    l_phq9_overdue_s3_count = 0
    l_phq9_overdue_s4_count = 0
    l_phq9_overdue_s5_count = 0
    l_phq9_overdue_s6_count = 0
    l_phq9_overdue_s7_count = 0
    l_phq9_overdue_s8_count = 0
    l_phq9_overdue_s9_count = 0

    phq_9_session_dates = {}

    #--------pre processing--------
    for record in response_json1:
        record_id = record.get("record_id")

        # Initialize the record entry
        if record_id not in phq_9_session_dates:
            phq_9_session_dates[record_id] = {}

        # Store the appointments
        if record.get("zoom_appt_date", "").strip():
            phq_9_session_dates[record_id]["session_1"] = record["zoom_appt_date"]

        if record.get("s2_appoint", "").strip():
            phq_9_session_dates[record_id]["session_2"] = record["s2_appoint"]

        if record.get("s3_appoint", "").strip():
            phq_9_session_dates[record_id]["session_3"] = record["s3_appoint"]

        if record.get("s4_appoint", "").strip():
            phq_9_session_dates[record_id]["session_4"] = record["s4_appoint"]

        if record.get("s5_appoint", "").strip():
            phq_9_session_dates[record_id]["session_5"] = record["s5_appoint"]

        if record.get("s6_appoint", "").strip():
            phq_9_session_dates[record_id]["session_6"] = record["s6_appoint"]

        if record.get("s7_appoint", "").strip():
            phq_9_session_dates[record_id]["session_7"] = record["s7_appoint"]

        if record.get("s8_appoint", "").strip():
            phq_9_session_dates[record_id]["session_8"] = record["s8_appoint"]

        if record.get("s9_appoint", "").strip():
            phq_9_session_dates[record_id]["session_9"] = record["s9_appoint"]


    # #--------table 4------------
        #-------Early vCare PHQ-9 Status-------
    for i in response_json1:
        group = i.get('randomization_group', '').strip()

        s1_appoint = phq_9_session_dates.get(i['record_id'], {}).get('session_1', None)
        s2_appoint = phq_9_session_dates.get(i['record_id'], {}).get('session_2', None)
        s3_appoint = phq_9_session_dates.get(i['record_id'], {}).get('session_3', None)
        s4_appoint = phq_9_session_dates.get(i['record_id'], {}).get('session_4', None)
        s5_appoint = phq_9_session_dates.get(i['record_id'], {}).get('session_5', None)
        s6_appoint = phq_9_session_dates.get(i['record_id'], {}).get('session_6', None)
        s7_appoint = phq_9_session_dates.get(i['record_id'], {}).get('session_7', None)
        s8_appoint = phq_9_session_dates.get(i['record_id'], {}).get('session_8', None)
        s9_appoint = phq_9_session_dates.get(i['record_id'], {}).get('session_9', None)

        if group == '1':

            #-----checking phq-9 score--------------

                # Session 1 (Human)
            if 'zoom_appt_date' in i and i['zoom_appt_date'].strip() and i['redcap_event_name'] == 'baseline_arm_1':
                zoom_appt_date = datetime.strptime(i['zoom_appt_date'], '%Y-%m-%d').date()

                if i.get('lumen_administered_phq9_complete') == '2' and zoom_appt_date <= date_today:
                    e_phq9_completed_s1_count += 1

                elif i.get('lumen_administered_phq9_complete') != '2' and zoom_appt_date > date_today:
                    e_phq9_expected_s1_count += 1
                else:
                    e_phq9_overdue_s1_count += 1

            # Session 2
            if i['redcap_event_name'] == 'session_2_arm_1' and s2_appoint:
                if i.get('lumen_administered_phq9_complete') == '2' and s2_appoint <= date_today:
                    e_phq9_completed_s2_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s2_appoint > date_today:
                    e_phq9_expected_s2_count += 1
                else:
                    e_phq9_overdue_s2_count += 1

            # Session 3
            if i['redcap_event_name'] == 'session_3_arm_1' and s3_appoint:
                if i.get('lumen_administered_phq9_complete') == '2' and s3_appoint <= date_today:
                    e_phq9_completed_s3_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s3_appoint > date_today:
                    e_phq9_expected_s3_count += 1
                else:
                    e_phq9_overdue_s3_count += 1

            # Session 4
            if i['redcap_event_name'] == 'session_4_arm_1' and s4_appoint:
                if i.get('lumen_administered_phq9_complete') == '2' and s4_appoint <= date_today:
                    e_phq9_completed_s4_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s4_appoint > date_today:
                    e_phq9_expected_s4_count += 1
                else:
                    e_phq9_overdue_s4_count += 1

            # Session 5
            if i['redcap_event_name'] == 'session_5_arm_1' and s5_appoint:
                if i.get('lumen_administered_phq9_complete') == '2' and s5_appoint <= date_today:
                    e_phq9_completed_s5_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s5_appoint > date_today:
                    e_phq9_expected_s5_count += 1
                else:
                    e_phq9_overdue_s5_count += 1

            # Session 6
            if i['redcap_event_name'] == 'session_6_arm_1' and s6_appoint:
                if i.get('lumen_administered_phq9_complete') == '2' and s6_appoint <= date_today:
                    e_phq9_completed_s6_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s6_appoint > date_today:
                    e_phq9_expected_s6_count += 1
                else:
                    e_phq9_overdue_s6_count += 1

            # Session 7
            if i['redcap_event_name'] == 'session_7_arm_1' and s7_appoint:
                if i.get('lumen_administered_phq9_complete') == '2' and s7_appoint <= date_today:
                    e_phq9_completed_s7_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s7_appoint > date_today:
                    e_phq9_expected_s7_count += 1
                else:
                    e_phq9_overdue_s7_count += 1

            # Session 8
            if i['redcap_event_name'] == 'session_8_arm_1' and s8_appoint:
                if i.get('lumen_administered_phq9_complete') == '2' and s8_appoint <= date_today:
                    e_phq9_completed_s8_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s8_appoint > date_today:
                    e_phq9_expected_s8_count += 1
                else:
                    e_phq9_overdue_s8_count += 1

            # Session 9
            if i['redcap_event_name'] == 'session_9_arm_1' and s9_appoint:
                if i.get('lumen_administered_phq9_complete') == '2' and s9_appoint <= date_today:
                    e_phq9_completed_s9_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s9_appoint > date_today:
                    e_phq9_expected_s9_count += 1
                else:
                    e_phq9_overdue_s9_count += 1

        #-------Later vCare PHQ-9 Status-------
        if group == '2':

            #-----checking phq-9 score--------------

                # Session 1 (Human)
            if 'zoom_appt_date' in i and i['zoom_appt_date'].strip() and i['redcap_event_name'] == 'baseline_arm_1':
                zoom_appt_date = datetime.strptime(i['zoom_appt_date'], '%Y-%m-%d').date()

                if i.get('lumen_administered_phq9_complete') == '2' and zoom_appt_date <= date_today:
                    l_phq9_completed_s1_count += 1

                elif i.get('lumen_administered_phq9_complete') != '2' and zoom_appt_date > date_today:
                    l_phq9_expected_s1_count += 1
                else:
                    l_phq9_overdue_s1_count += 1

            # Session 2
            if i['redcap_event_name'] == 'session_2_arm_1' and s2_appoint:
                if i.get('lumen_administered_phq9_complete') == '2' and s2_appoint <= date_today:
                    l_phq9_completed_s2_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s2_appoint > date_today:
                    l_phq9_expected_s2_count += 1
                else:
                    l_phq9_overdue_s2_count += 1

            # Session 3
            if i['redcap_event_name'] == 'session_3_arm_1' and s3_appoint:
                if i.get('lumen_administered_phq9_complete') == '2' and s3_appoint <= date_today:
                    l_phq9_completed_s3_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s3_appoint > date_today:
                    l_phq9_expected_s3_count += 1
                else:
                    l_phq9_overdue_s3_count += 1

            # Session 4
            if i['redcap_event_name'] == 'session_4_arm_1' and s4_appoint:
                if i.get('lumen_administered_phq9_complete') == '2' and s4_appoint <= date_today:
                    l_phq9_completed_s4_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s4_appoint > date_today:
                    l_phq9_expected_s4_count += 1
                else:
                    l_phq9_overdue_s4_count += 1

            # Session 5
            if i['redcap_event_name'] == 'session_5_arm_1' and s5_appoint:
                if i.get('lumen_administered_phq9_complete') == '2' and s5_appoint <= date_today:
                    l_phq9_completed_s5_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s5_appoint > date_today:
                    l_phq9_expected_s5_count += 1
                else:
                    l_phq9_overdue_s5_count += 1

            # Session 6
            if i['redcap_event_name'] == 'session_6_arm_1' and s6_appoint:
                if i.get('lumen_administered_phq9_complete') == '2' and s6_appoint <= date_today:
                    l_phq9_completed_s6_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s6_appoint > date_today:
                    l_phq9_expected_s6_count += 1
                else:
                    l_phq9_overdue_s6_count += 1

            # Session 7
            if i['redcap_event_name'] == 'session_7_arm_1' and s7_appoint:
                if i.get('lumen_administered_phq9_complete') == '2' and s7_appoint <= date_today:
                    l_phq9_completed_s7_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s7_appoint > date_today:
                    l_phq9_expected_s7_count += 1
                else:
                    l_phq9_overdue_s7_count += 1

            # Session 8
            if i['redcap_event_name'] == 'session_8_arm_1' and s8_appoint:
                if i.get('lumen_administered_phq9_complete') == '2' and s8_appoint <= date_today:
                    l_phq9_completed_s8_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s8_appoint > date_today:
                    l_phq9_expected_s8_count += 1
                else:
                    l_phq9_overdue_s8_count += 1

            # Session 9
            if i['redcap_event_name'] == 'session_9_arm_1' and s9_appoint:
                if i.get('lumen_administered_phq9_complete') == '2' and s9_appoint <= date_today:
                    l_phq9_completed_s9_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s9_appoint > date_today:
                    l_phq9_expected_s9_count += 1
                else:
                    l_phq9_overdue_s9_count += 1


    results_json = {
        "Table_1": {
            "Early": {
                "Total": e_total_table_1,
                "Early Rand-1 Notified by phone": e_rand_notified_by_phn_count,
                "Early Rand-2 Notified by phone": 0,
                "Early Intervention Withdrawal": e_intervention_withdrawal,
                "Early Study Withdrawal": e_study_withdrawal,
                "Early Post Rand Exclusion": e_post_rand_excl
            },
            "Later": {
                "Total": l_total_table_1,
                "Later Rand-1 Notified by phone": l_rand_notified_by_phn_count,
                "Later Rand-2 Notified by phone": l_rand_2_notified_by_phn_count,
                "Later Intervention Withdrawal": l_intervention_withdrawal,
                "Later Study Withdrawal": l_study_withdrawal,
                "Later Post Rand Exclusion": l_post_rand_excl
            }
        },
        "Early v_care message completion": {
            "Active Phase Message Completion": {
                "Scheduled": {
                    "Message - 1": e_apm_msg_1_scheduled_count,
                    "Message - 2": e_apm_msg_2_scheduled_count,
                    "Message - 3": e_apm_msg_3_scheduled_count,
                    "Message - 4": e_apm_msg_4_scheduled_count,
                    "Message - 5": e_apm_msg_5_scheduled_count,
                    "Message - 6": e_apm_msg_6_scheduled_count,
                    "Message - 7": e_apm_msg_7_scheduled_count,
                    "Message - 8": e_apm_msg_8_scheduled_count,
                    "Message - 9": e_apm_msg_9_scheduled_count,
                    "Message - 10": e_apm_msg_10_scheduled_count,
                    "Message - 11": e_apm_msg_11_scheduled_count
                },
                "Yes": {
                    "Message - 1": e_apm_msg_1_yes_count,
                    "Message - 2": e_apm_msg_2_yes_count,
                    "Message - 3": e_apm_msg_3_yes_count,
                    "Message - 4": e_apm_msg_4_yes_count,
                    "Message - 5": e_apm_msg_5_yes_count,
                    "Message - 6": e_apm_msg_6_yes_count,
                    "Message - 7": e_apm_msg_7_yes_count,
                    "Message - 8": e_apm_msg_8_yes_count,
                    "Message - 9": e_apm_msg_9_yes_count,
                    "Message - 10": e_apm_msg_10_yes_count,
                    "Message - 11": e_apm_msg_11_yes_count
                },
                "In Progress": {
                    "Message - 1": e_apm_msg_1_ip_count,
                    "Message - 2": e_apm_msg_2_ip_count,
                    "Message - 3": e_apm_msg_3_ip_count,
                    "Message - 4": e_apm_msg_4_ip_count,
                    "Message - 5": e_apm_msg_5_ip_count,
                    "Message - 6": e_apm_msg_6_ip_count,
                    "Message - 7": e_apm_msg_7_ip_count,
                    "Message - 8": e_apm_msg_8_ip_count,
                    "Message - 9": e_apm_msg_9_ip_count,
                    "Message - 10": e_apm_msg_10_ip_count,
                    "Message - 11": e_apm_msg_11_ip_count
                },
                "No": {
                    "Message - 1": e_apm_msg_1_no_count,
                    "Message - 2": e_apm_msg_2_no_count,
                    "Message - 3": e_apm_msg_3_no_count,
                    "Message - 4": e_apm_msg_4_no_count,
                    "Message - 5": e_apm_msg_5_no_count,
                    "Message - 6": e_apm_msg_6_no_count,
                    "Message - 7": e_apm_msg_7_no_count,
                    "Message - 8": e_apm_msg_8_no_count,
                    "Message - 9": e_apm_msg_9_no_count,
                    "Message - 10": e_apm_msg_10_no_count,
                    "Message - 11": e_apm_msg_11_no_count
                },
                "Withdrawn": {
                    "Message - 1": e_apm_msg_1_withdrawn_count,
                    "Message - 2": e_apm_msg_2_withdrawn_count,
                    "Message - 3": e_apm_msg_3_withdrawn_count,
                    "Message - 4": e_apm_msg_4_withdrawn_count,
                    "Message - 5": e_apm_msg_5_withdrawn_count,
                    "Message - 6": e_apm_msg_6_withdrawn_count,
                    "Message - 7": e_apm_msg_7_withdrawn_count,
                    "Message - 8": e_apm_msg_8_withdrawn_count,
                    "Message - 9": e_apm_msg_9_withdrawn_count,
                    "Message - 10": e_apm_msg_10_withdrawn_count,
                    "Message - 11": e_apm_msg_11_withdrawn_count
                }
            }
        },
        "Later v_care message completion": {
            "Active Phase Message Completion": {
                "Scheduled": {
                    "Message - 1": l_apm_msg_1_scheduled_count,
                    "Message - 2": l_apm_msg_2_scheduled_count,
                    "Message - 3": l_apm_msg_3_scheduled_count,
                    "Message - 4": l_apm_msg_4_scheduled_count,
                    "Message - 5": l_apm_msg_5_scheduled_count,
                    "Message - 6": l_apm_msg_6_scheduled_count,
                    "Message - 7": l_apm_msg_7_scheduled_count,
                    "Message - 8": l_apm_msg_8_scheduled_count,
                    "Message - 9": l_apm_msg_9_scheduled_count,
                    "Message - 10": l_apm_msg_10_scheduled_count,
                    "Message - 11": l_apm_msg_11_scheduled_count
                },
                "Yes": {
                    "Message - 1": l_apm_msg_1_yes_count,
                    "Message - 2": l_apm_msg_2_yes_count,
                    "Message - 3": l_apm_msg_3_yes_count,
                    "Message - 4": l_apm_msg_4_yes_count,
                    "Message - 5": l_apm_msg_5_yes_count,
                    "Message - 6": l_apm_msg_6_yes_count,
                    "Message - 7": l_apm_msg_7_yes_count,
                    "Message - 8": l_apm_msg_8_yes_count,
                    "Message - 9": l_apm_msg_9_yes_count,
                    "Message - 10": l_apm_msg_10_yes_count,
                    "Message - 11": l_apm_msg_11_yes_count
                },
                "In Progress": {
                    "Message - 1": l_apm_msg_1_ip_count,
                    "Message - 2": l_apm_msg_2_ip_count,
                    "Message - 3": l_apm_msg_3_ip_count,
                    "Message - 4": l_apm_msg_4_ip_count,
                    "Message - 5": l_apm_msg_5_ip_count,
                    "Message - 6": l_apm_msg_6_ip_count,
                    "Message - 7": l_apm_msg_7_ip_count,
                    "Message - 8": l_apm_msg_8_ip_count,
                    "Message - 9": l_apm_msg_9_ip_count,
                    "Message - 10": l_apm_msg_10_ip_count,
                    "Message - 11": l_apm_msg_11_ip_count
                },
                "No": {
                    "Message - 1": l_apm_msg_1_no_count,
                    "Message - 2": l_apm_msg_2_no_count,
                    "Message - 3": l_apm_msg_3_no_count,
                    "Message - 4": l_apm_msg_4_no_count,
                    "Message - 5": l_apm_msg_5_no_count,
                    "Message - 6": l_apm_msg_6_no_count,
                    "Message - 7": l_apm_msg_7_no_count,
                    "Message - 8": l_apm_msg_8_no_count,
                    "Message - 9": l_apm_msg_9_no_count,
                    "Message - 10": l_apm_msg_10_no_count,
                    "Message - 11": l_apm_msg_11_no_count
                },
                "Withdrawn": {
                    "Message - 1": l_apm_msg_1_withdrawn_count,
                    "Message - 2": l_apm_msg_2_withdrawn_count,
                    "Message - 3": l_apm_msg_3_withdrawn_count,
                    "Message - 4": l_apm_msg_4_withdrawn_count,
                    "Message - 5": l_apm_msg_5_withdrawn_count,
                    "Message - 6": l_apm_msg_6_withdrawn_count,
                    "Message - 7": l_apm_msg_7_withdrawn_count,
                    "Message - 8": l_apm_msg_8_withdrawn_count,
                    "Message - 9": l_apm_msg_9_withdrawn_count,
                    "Message - 10": l_apm_msg_10_withdrawn_count,
                    "Message - 11": l_apm_msg_11_withdrawn_count
                }
            }
        },
        "Early v_care maintenance completion": {
            "Maintenance Phase Message Completion": {
                "Scheduled": {
                    "Message - 1": e_mpm_msg_1_scheduled_count,
                    "Message - 2": e_mpm_msg_2_scheduled_count,
                    "Message - 3": e_mpm_msg_3_scheduled_count,
                    "Message - 4": e_mpm_msg_4_scheduled_count,
                    "Message - 5": e_mpm_msg_5_scheduled_count,
                    "Message - 6": e_mpm_msg_6_scheduled_count,
                    "Message - 7": e_mpm_msg_7_scheduled_count,
                    "Message - 8": e_mpm_msg_8_scheduled_count,
                    "Message - 9": e_mpm_msg_9_scheduled_count,
                    "Message - 10": e_mpm_msg_10_scheduled_count
                },
                "Yes": {
                    "Message - 1": e_mpm_msg_1_yes_count,
                    "Message - 2": e_mpm_msg_2_yes_count,
                    "Message - 3": e_mpm_msg_3_yes_count,
                    "Message - 4": e_mpm_msg_4_yes_count,
                    "Message - 5": e_mpm_msg_5_yes_count,
                    "Message - 6": e_mpm_msg_6_yes_count,
                    "Message - 7": e_mpm_msg_7_yes_count,
                    "Message - 8": e_mpm_msg_8_yes_count,
                    "Message - 9": e_mpm_msg_9_yes_count,
                    "Message - 10": e_mpm_msg_10_yes_count
                },
                "In Progress": {
                    "Message - 1": e_mpm_msg_1_ip_count,
                    "Message - 2": e_mpm_msg_2_ip_count,
                    "Message - 3": e_mpm_msg_3_ip_count,
                    "Message - 4": e_mpm_msg_4_ip_count,
                    "Message - 5": e_mpm_msg_5_ip_count,
                    "Message - 6": e_mpm_msg_6_ip_count,
                    "Message - 7": e_mpm_msg_7_ip_count,
                    "Message - 8": e_mpm_msg_8_ip_count,
                    "Message - 9": e_mpm_msg_9_ip_count,
                    "Message - 10": e_mpm_msg_10_ip_count
                },
                "No": {
                    "Message - 1": e_mpm_msg_1_no_count,
                    "Message - 2": e_mpm_msg_2_no_count,
                    "Message - 3": e_mpm_msg_3_no_count,
                    "Message - 4": e_mpm_msg_4_no_count,
                    "Message - 5": e_mpm_msg_5_no_count,
                    "Message - 6": e_mpm_msg_6_no_count,
                    "Message - 7": e_mpm_msg_7_no_count,
                    "Message - 8": e_mpm_msg_8_no_count,
                    "Message - 9": e_mpm_msg_9_no_count,
                    "Message - 10": e_mpm_msg_10_no_count
                },
                "Withdrawn": {
                    "Message - 1": e_mpm_msg_1_withdrawn_count,
                    "Message - 2": e_mpm_msg_2_withdrawn_count,
                    "Message - 3": e_mpm_msg_3_withdrawn_count,
                    "Message - 4": e_mpm_msg_4_withdrawn_count,
                    "Message - 5": e_mpm_msg_5_withdrawn_count,
                    "Message - 6": e_mpm_msg_6_withdrawn_count,
                    "Message - 7": e_mpm_msg_7_withdrawn_count,
                    "Message - 8": e_mpm_msg_8_withdrawn_count,
                    "Message - 9": e_mpm_msg_9_withdrawn_count,
                    "Message - 10": e_mpm_msg_10_withdrawn_count
                }
            }
        },
        "Counseling Session Status": {
            "Early": {
                "Session 1": {
                    "Scheduled": e_session_1_scheduled_count,
                    "Completed": e_session_1_completed_count,
                    "Missed": e_session_1_missed_count,
                    "Pending": e_session_1_pending_count,
                    "Withdrawn": e_session_1_withdrawn_count
                },
                "Session 2": {
                    "Scheduled": e_session_2_scheduled_count,
                    "Completed": e_session_2_completed_count,
                    "Missed": e_session_2_missed_count,
                    "Pending": e_session_2_pending_count,
                    "Withdrawn": e_session_2_withdrawn_count
                },
                "Session 3": {
                    "Scheduled": e_session_3_scheduled_count,
                    "Completed": e_session_3_completed_count,
                    "Missed": e_session_3_missed_count,
                    "Pending": e_session_3_pending_count,
                    "Withdrawn": e_session_3_withdrawn_count
                },
                "Session 4": {
                    "Scheduled": e_session_4_scheduled_count,
                    "Completed": e_session_4_completed_count,
                    "Missed": e_session_4_missed_count,
                    "Pending": e_session_4_pending_count,
                    "Withdrawn": e_session_4_withdrawn_count
                },
                "Session 5": {
                    "Scheduled": e_session_5_scheduled_count,
                    "Completed": e_session_5_completed_count,
                    "Missed": e_session_5_missed_count,
                    "Pending": e_session_5_pending_count,
                    "Withdrawn": e_session_5_withdrawn_count
                },
                "Session 6": {
                    "Scheduled": e_session_6_scheduled_count,
                    "Completed": e_session_6_completed_count,
                    "Missed": e_session_6_missed_count,
                    "Pending": e_session_6_pending_count,
                    "Withdrawn": e_session_6_withdrawn_count
                },
                "Session 7": {
                    "Scheduled": e_session_7_scheduled_count,
                    "Completed": e_session_7_completed_count,
                    "Missed": e_session_7_missed_count,
                    "Pending": e_session_7_pending_count,
                    "Withdrawn": e_session_7_withdrawn_count
                },
                "Session 8": {
                    "Scheduled": e_session_8_scheduled_count,
                    "Completed": e_session_8_completed_count,
                    "Missed": e_session_8_missed_count,
                    "Pending": e_session_8_pending_count,
                    "Withdrawn": e_session_8_withdrawn_count
                },
                "Session 9": {
                    "Scheduled": e_session_9_scheduled_count,
                    "Completed": e_session_9_completed_count,
                    "Missed": e_session_9_missed_count,
                    "Pending": e_session_9_pending_count,
                    "Withdrawn": e_session_9_withdrawn_count
                }
            },
            "Later": {
                "Session 1": {
                    "Scheduled": l_session_1_scheduled_count,
                    "Completed": l_session_1_completed_count,
                    "Missed": l_session_1_missed_count,
                    "Pending": l_session_1_pending_count,
                    "Withdrawn": l_session_1_withdrawn_count
                },
                "Session 2": {
                    "Scheduled": l_session_2_scheduled_count,
                    "Completed": l_session_2_completed_count,
                    "Missed": l_session_2_missed_count,
                    "Pending": l_session_2_pending_count,
                    "Withdrawn": l_session_2_withdrawn_count
                },
                "Session 3": {
                    "Scheduled": l_session_3_scheduled_count,
                    "Completed": l_session_3_completed_count,
                    "Missed": l_session_3_missed_count,
                    "Pending": l_session_3_pending_count,
                    "Withdrawn": l_session_3_withdrawn_count
                },
                "Session 4": {
                    "Scheduled": l_session_4_scheduled_count,
                    "Completed": l_session_4_completed_count,
                    "Missed": l_session_4_missed_count,
                    "Pending": l_session_4_pending_count,
                    "Withdrawn": l_session_4_withdrawn_count
                },
                "Session 5": {
                    "Scheduled": l_session_5_scheduled_count,
                    "Completed": l_session_5_completed_count,
                    "Missed": l_session_5_missed_count,
                    "Pending": l_session_5_pending_count,
                    "Withdrawn": l_session_5_withdrawn_count
                },
                "Session 6": {
                    "Scheduled": l_session_6_scheduled_count,
                    "Completed": l_session_6_completed_count,
                    "Missed": l_session_6_missed_count,
                    "Pending": l_session_6_pending_count,
                    "Withdrawn": l_session_6_withdrawn_count
                },
                "Session 7": {
                    "Scheduled": l_session_7_scheduled_count,
                    "Completed": l_session_7_completed_count,
                    "Missed": l_session_7_missed_count,
                    "Pending": l_session_7_pending_count,
                    "Withdrawn": l_session_7_withdrawn_count
                },
                "Session 8": {
                    "Scheduled": l_session_8_scheduled_count,
                    "Completed": l_session_8_completed_count,
                    "Missed": l_session_8_missed_count,
                    "Pending": l_session_8_pending_count,
                    "Withdrawn": l_session_8_withdrawn_count
                },
                "Session 9": {
                    "Scheduled": l_session_9_scheduled_count,
                    "Completed": l_session_9_completed_count,
                    "Missed": l_session_9_missed_count,
                    "Pending": l_session_9_pending_count,
                    "Withdrawn": l_session_9_withdrawn_count
                }
            }
        },
        "PHQ-9 Status by Session": {
            "Early": {
                "Session 1": {"Completed": e_phq9_completed_s1_count, "Expected": e_phq9_expected_s1_count, "Overdue": e_phq9_overdue_s1_count},
                "Session 2": {"Completed": e_phq9_completed_s2_count, "Expected": e_phq9_expected_s2_count, "Overdue": e_phq9_overdue_s2_count},
                "Session 3": {"Completed": e_phq9_completed_s3_count, "Expected": e_phq9_expected_s3_count, "Overdue": e_phq9_overdue_s3_count},
                "Session 4": {"Completed": e_phq9_completed_s4_count, "Expected": e_phq9_expected_s4_count, "Overdue": e_phq9_overdue_s4_count},
                "Session 5": {"Completed": e_phq9_completed_s5_count, "Expected": e_phq9_expected_s5_count, "Overdue": e_phq9_overdue_s5_count},
                "Session 6": {"Completed": e_phq9_completed_s6_count, "Expected": e_phq9_expected_s6_count, "Overdue": e_phq9_overdue_s6_count},
                "Session 7": {"Completed": e_phq9_completed_s7_count, "Expected": e_phq9_expected_s7_count, "Overdue": e_phq9_overdue_s7_count},
                "Session 8": {"Completed": e_phq9_completed_s8_count, "Expected": e_phq9_expected_s8_count, "Overdue": e_phq9_overdue_s8_count},
                "Session 9": {"Completed": e_phq9_completed_s9_count, "Expected": e_phq9_expected_s9_count, "Overdue": e_phq9_overdue_s9_count}
            },
            "Later": {
                "Session 1": {"Completed": l_phq9_completed_s1_count, "Expected": l_phq9_expected_s1_count, "Overdue": l_phq9_overdue_s1_count},
                "Session 2": {"Completed": l_phq9_completed_s2_count, "Expected": l_phq9_expected_s2_count, "Overdue": l_phq9_overdue_s2_count},
                "Session 3": {"Completed": l_phq9_completed_s3_count, "Expected": l_phq9_expected_s3_count, "Overdue": l_phq9_overdue_s3_count},
                "Session 4": {"Completed": l_phq9_completed_s4_count, "Expected": l_phq9_expected_s4_count, "Overdue": l_phq9_overdue_s4_count},
                "Session 5": {"Completed": l_phq9_completed_s5_count, "Expected": l_phq9_expected_s5_count, "Overdue": l_phq9_overdue_s5_count},
                "Session 6": {"Completed": l_phq9_completed_s6_count, "Expected": l_phq9_expected_s6_count, "Overdue": l_phq9_overdue_s6_count},
                "Session 7": {"Completed": l_phq9_completed_s7_count, "Expected": l_phq9_expected_s7_count, "Overdue": l_phq9_overdue_s7_count},
                "Session 8": {"Completed": l_phq9_completed_s8_count, "Expected": l_phq9_expected_s8_count, "Overdue": l_phq9_overdue_s8_count},
                "Session 9": {"Completed": l_phq9_completed_s9_count, "Expected": l_phq9_expected_s9_count, "Overdue": l_phq9_overdue_s9_count}
            }
        },
        "Additional Surveys": {
            "Tech Check": {
                "Scheduled": tech_check_scheduled,
                "Withdrawals": tech_check_withdrawals,
                "Completed": tech_check_completed,
                "Not yet due": tech_check_not_yet_due,
                "Overdue": tech_check_overdue
            },
            "Evaluation": {
                "Scheduled": eval_scheduled,
                "Withdrawals": eval_withdrawals,
                "Completed": eval_completed,
                "Not yet due": eval_not_yet_due,
                "Overdue": eval_overdue
            },
            "On demand Session": {
                "Withdrawals": on_demand_withdrawals,
                "Completed": on_demand_completed,
            }
        }

    }

    return results_json
