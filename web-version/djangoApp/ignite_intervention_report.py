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
                if withdrawn_date and (s5_date + timedelta(days=-3)) >= withdrawn_date:
                    e_apm_msg_1_withdrawn_count += 1

                #----scheduled msgs------
                if (date_today - s5_date).days >= -3 :
                    # print(f"Scheduled date: {s5_date}, Record is: {i['record_id']} and active_phase_message_1_complete: {i.get('active_phase_message_1_complete')}")
                    e_apm_msg_1_scheduled_count += 1

                #----for yes msgs-----
                if (date_today - s5_date).days >= -3 and i.get("active_phase_message_1_complete") == "2":
                    e_apm_msg_1_yes_count += 1

                #----for ip msgs-----
                elif s5_date - timedelta(days=3) <= date_today < s5_date + timedelta(days=10) and i.get("active_phase_message_1_complete") != "2":  ## betn session 1 and 2 dates and not done 
                    # print(f"IP, Record is: {i['record_id']} and active_phase_message_1_complete: {i.get('active_phase_message_1_complete')}")
                    e_apm_msg_1_ip_count += 1

                #----for no msgs-----
                elif (date_today - s5_date).days >= -3 and (i.get("active_phase_message_1_complete") == "0"):
                    # print(f"No, Record is: {i['record_id']} and active_phase_message_1_complete: {i.get('active_phase_message_1_complete')}")
                    e_apm_msg_1_no_count += 1

            if i['ap1_date'].strip() and 'ap1_date' in i:
                ap1_date = datetime.strptime(i['ap1_date'], '%Y-%m-%d').date()

                #------check msg - 2--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=7) > withdrawn_date):
                    e_apm_msg_2_withdrawn_count += 1
            
                #----scheduled msgs------
                if (date_today - ap1_date).days >= 7:
                    e_apm_msg_2_scheduled_count += 1

                #----for yes msgs-----
                if (date_today - ap1_date).days >= 7 and i.get("active_phase_message_2_complete") == "2":
                    e_apm_msg_2_yes_count += 1

                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=7)  and i.get("active_phase_message_2_complete") != "2":
                    e_apm_msg_2_ip_count += 1

                #----for no msgs-----
                elif (date_today - ap1_date).days >= 7 and i.get("active_phase_message_2_complete") == "0":
                    e_apm_msg_2_no_count += 1

                #------check msg - 3--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=14) > withdrawn_date):
                    e_apm_msg_3_withdrawn_count += 1

                #----scheduled msgs------
                if (date_today - ap1_date).days >= 14:
                    e_apm_msg_3_scheduled_count += 1

                #----for yes msgs-----
                if (date_today - ap1_date).days >= 14 and i.get("active_phase_message_3_complete") == "2":
                    e_apm_msg_3_yes_count += 1

                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=21) and i.get("active_phase_message_3_complete") != "2":
                    e_apm_msg_3_ip_count += 1

                #----for no msgs-----
                elif (date_today - ap1_date).days >= 14 and i.get("active_phase_message_3_complete") == "0":
                    e_apm_msg_3_no_count += 1

                #------check msg - 4--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=21) > withdrawn_date):
                    e_apm_msg_4_withdrawn_count += 1
                #----scheduled msgs------
                if (date_today - ap1_date).days >= 21:
                    e_apm_msg_4_scheduled_count += 1

                #----for yes msgs-----
                if (date_today - ap1_date).days >= 21 and i.get("active_phase_message_4_complete") == "2":
                    e_apm_msg_4_yes_count += 1  
                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=28)  and i.get("active_phase_message_4_complete") != "2":
                    e_apm_msg_4_ip_count += 1 

                #----for no msgs-----
                elif (date_today - ap1_date).days >= 21 and i.get("active_phase_message_4_complete") == "0":
                    e_apm_msg_4_no_count += 1

                #------check msg - 5--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=28) > withdrawn_date):
                    e_apm_msg_5_withdrawn_count += 1   
                #----scheduled msgs------
                if (date_today - ap1_date).days >= 28 :
                    e_apm_msg_5_scheduled_count += 1

                #----for yes msgs-----
                if (date_today - ap1_date).days >= 28 and i.get("active_phase_message_5_complete") == "2":
                    e_apm_msg_5_yes_count += 1
                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=35)   and i.get("active_phase_message_5_complete") != "2":
                    e_apm_msg_5_ip_count += 1
                #----for no msgs-----
                elif (date_today - ap1_date).days >= 28 and i.get("active_phase_message_5_complete") == "0":
                    e_apm_msg_5_no_count += 1


                #------check msg - 6--------------
                if withdrawn_date and (ap1_date + timedelta(days=35) > withdrawn_date):
                    e_apm_msg_6_withdrawn_count += 1
                #----scheduled msgs------
                if (date_today - ap1_date).days >= 35:
                    e_apm_msg_6_scheduled_count += 1

                #----for yes msgs-----
                if (date_today - ap1_date).days >= 35 and i.get("active_phase_message_5_complete") == "2":
                    e_apm_msg_6_yes_count += 1
                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=42)  and i.get("active_phase_message_5_complete") != "2":
                    e_apm_msg_6_ip_count += 1
                #----for no msgs-----
                elif (date_today - ap1_date).days >= 35 and i.get("active_phase_message_5_complete") == "0":
                    e_apm_msg_6_no_count += 1

                #------check msg - 7--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=42) > withdrawn_date):
                    e_apm_msg_7_withdrawn_count += 1
                #----scheduled msgs------
                if (date_today - ap1_date).days >= 42:
                    e_apm_msg_7_scheduled_count += 1
                #----for yes msgs-----
                if (date_today - ap1_date).days >= 42 and i.get("active_phase_message_7_complete") == "2":
                    e_apm_msg_7_yes_count += 1
                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=49)  and i.get("active_phase_message_7_complete") != "2":
                    e_apm_msg_7_ip_count += 1
                #----for no msgs-----
                elif (date_today - ap1_date).days >= 42 and i.get("active_phase_message_7_complete") == "0":
                    e_apm_msg_7_no_count += 1

                #------check msg - 8--------------  
                if withdrawn_date and (ap1_date + timedelta(days=49) > withdrawn_date):
                    e_apm_msg_8_withdrawn_count += 1
                #----scheduled msgs------
                if (date_today - ap1_date).days >= 49 :
                    e_apm_msg_8_scheduled_count += 1
                #----for yes msgs-----
                if (date_today - ap1_date).days >= 49 and i.get("active_phase_message_8_complete") == "2":
                    e_apm_msg_8_yes_count += 1
                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=56)  and i.get("active_phase_message_8_complete") != "2":
                    e_apm_msg_8_ip_count += 1

                #----for no msgs-----
                elif (date_today - ap1_date).days >= 49 and i.get("active_phase_message_8_complete") == "0":
                    e_apm_msg_8_no_count += 1

                #------check msg - 9--------------
                    #-----withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=56) > withdrawn_date):
                    e_apm_msg_9_withdrawn_count += 1
                #----scheduled msgs------
                if (date_today - ap1_date).days >= 56 :
                    e_apm_msg_9_scheduled_count += 1
                #----for yes msgs-----
                if (date_today - ap1_date).days >= 56 :
                    e_apm_msg_9_yes_count += 1
                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=63)  and i.get("active_phase_message_9_complete") != "2":
                    e_apm_msg_9_ip_count += 1
                #----for no msgs-----
                elif (date_today - ap1_date).days >= 56 and i.get("active_phase_message_9_complete") == "0":
                    e_apm_msg_9_no_count += 1

                #------check msg - 10--------------
                if withdrawn_date and (ap1_date + timedelta(days=63) > withdrawn_date):
                    e_apm_msg_10_withdrawn_count += 1   
                #----scheduled msgs------
                if (date_today - ap1_date).days >= 63:
                    e_apm_msg_10_scheduled_count += 1
                #----for yes msgs-----
                if (date_today - ap1_date).days >= 63 and i.get("active_phase_message_10_complete") == "2":
                    e_apm_msg_10_yes_count += 1
                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=70)  and i.get("active_phase_message_10_complete") != "2":
                    e_apm_msg_10_ip_count += 1
                #----for no msgs-----
                elif (date_today - ap1_date).days >= 63 and i.get("active_phase_message_10_complete") == "0":
                    e_apm_msg_10_no_count += 1

                #------check msg - 11--------------
                if withdrawn_date and (ap1_date + timedelta(days=70) > withdrawn_date):
                    e_apm_msg_11_withdrawn_count += 1
                #----scheduled msgs------
                if (date_today - ap1_date).days >= 70 :
                    e_apm_msg_11_scheduled_count += 1
                #----for yes msgs-----
                if (date_today - ap1_date).days >= 70 and i.get("active_phase_message_11_complete") == "2":
                    e_apm_msg_11_yes_count += 1
                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=77)  and i.get("active_phase_message_11_complete") != "2":
                    e_apm_msg_11_ip_count += 1
                #----for no msgs-----
                elif (date_today - ap1_date).days >= 70 and i.get("active_phase_message_11_complete") == "0":
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
                if (s5_date - date_today).days > -3 :
                    l_apm_msg_1_scheduled_count += 1
                #----for yes msgs-----
                if (s5_date - date_today).days >= -3 and i.get("active_phase_message_1_complete") == "2":
                    l_apm_msg_1_yes_count += 1

                #----for ip msgs-----
                elif s5_date - timedelta(days=3) <= date_today < s5_date + timedelta(days=10) and i.get("active_phase_message_1_complete") != "2":
                    l_apm_msg_1_ip_count += 1

                #----for no msgs-----
                elif (s5_date - date_today).days >= -3 and i.get("active_phase_message_1_complete") == "0":
                    l_apm_msg_1_no_count += 1

            if i['ap1_date'].strip() and 'ap1_date' in i:
                ap1_date = datetime.strptime(i['ap1_date'], '%Y-%m-%d').date()

                #------check msg - 2--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=7) > withdrawn_date):
                    l_apm_msg_2_withdrawn_count += 1
                #----scheduled msgs------
                if (date_today - ap1_date).days >= 7 and i.get("active_phase_message_2_complete") != "2":
                    l_apm_msg_2_scheduled_count += 1
                #----for yes msgs-----
                if (date_today - ap1_date).days >= 7 and i.get("active_phase_message_2_complete") == "2":
                    l_apm_msg_2_yes_count += 1

                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=7)  and i.get("active_phase_message_2_complete") != "2":
                    l_apm_msg_2_ip_count += 1
                #----for no msgs-----
                elif (date_today - ap1_date).days >= 7 and i.get("active_phase_message_2_complete") == "0":
                    l_apm_msg_2_no_count += 1

                #------check msg - 3--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=14) > withdrawn_date):
                    l_apm_msg_3_withdrawn_count += 1
                #----scheduled msgs------
                if (date_today - ap1_date).days >= 14 and i.get("active_phase_message_3_complete") != "2":
                    l_apm_msg_3_scheduled_count += 1
                #----for yes msgs-----
                if (date_today - ap1_date).days >= 14 and i.get("active_phase_message_3_complete") == "2":
                    l_apm_msg_3_yes_count += 1

                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=21)and i.get("active_phase_message_3_complete") != "2":
                    l_apm_msg_3_ip_count += 1

                #----for no msgs-----
                elif (date_today - ap1_date).days >= 14 and i.get("active_phase_message_3_complete") == "0":
                    l_apm_msg_3_no_count += 1

                #------check msg - 4--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=21) > withdrawn_date):
                    l_apm_msg_4_withdrawn_count += 1
                #----scheduled msgs------
                if (date_today - ap1_date).days >= 21 and i.get("active_phase_message_4_complete") != "2":
                    l_apm_msg_4_scheduled_count += 1
                #----for yes msgs-----
                if (date_today - ap1_date).days >= 21 and i.get("active_phase_message_4_complete") == "2":
                    l_apm_msg_4_yes_count += 1  
                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=28) and i.get("active_phase_message_4_complete") != "2":
                    l_apm_msg_4_ip_count += 1   
                #----for no msgs-----
                elif (date_today - ap1_date).days >= 21 and i.get("active_phase_message_4_complete") == "0":
                    l_apm_msg_4_no_count += 1

                #------check msg - 5--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=28) > withdrawn_date):
                    l_apm_msg_5_withdrawn_count += 1   
                #----scheduled msgs------
                if (date_today - ap1_date).days >= 28 and i.get("active_phase_message_5_complete") != "2":
                    l_apm_msg_5_scheduled_count += 1 
                #----for yes msgs-----
                if (date_today - ap1_date).days >= 28 and i.get("active_phase_message_5_complete") == "2":
                    l_apm_msg_5_yes_count += 1
                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=35)  and i.get("active_phase_message_5_complete") != "2":
                    l_apm_msg_5_ip_count += 1
                #----for no msgs-----
                elif (date_today - ap1_date).days >= 28 and i.get("active_phase_message_5_complete") == "0":
                    l_apm_msg_5_no_count += 1

                #------check msg - 6--------------
                if withdrawn_date and (ap1_date + timedelta(days=35) > withdrawn_date):
                    l_apm_msg_6_withdrawn_count += 1
                #----scheduled msgs------
                if (date_today - ap1_date).days >= 35 and i.get("active_phase_message_5_complete") != "2":
                    l_apm_msg_6_scheduled_count += 1
                #----for yes msgs-----
                if (date_today - ap1_date).days >= 35 and i.get("active_phase_message_5_complete") == "2":
                    l_apm_msg_6_yes_count += 1
                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=42) and i.get("active_phase_message_5_complete") != "2":
                    l_apm_msg_6_ip_count += 1
                #----for no msgs-----
                elif (date_today - ap1_date).days >= 35 and i.get("active_phase_message_5_complete") == "0":
                    l_apm_msg_6_no_count += 1

                #------check msg - 7--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=42) > withdrawn_date):
                    l_apm_msg_7_withdrawn_count += 1
                #----scheduled msgs------
                if (date_today - ap1_date).days >= 42 and i.get("active_phase_message_7_complete") != "2":
                    l_apm_msg_7_scheduled_count += 1
                #----for yes msgs-----
                if (date_today - ap1_date).days >= 42 and i.get("active_phase_message_7_complete") == "2":
                    l_apm_msg_7_yes_count += 1
                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=49) and i.get("active_phase_message_7_complete") != "2":
                    l_apm_msg_7_ip_count += 1
                #----for no msgs-----
                elif (date_today - ap1_date).days >= 42 and i.get("active_phase_message_7_complete") == "0":
                    l_apm_msg_7_no_count += 1

                #------check msg - 8--------------  
                if withdrawn_date and (ap1_date + timedelta(days=49) > withdrawn_date):
                    l_apm_msg_8_withdrawn_count += 1
                #----scheduled msgs------
                if (date_today - ap1_date).days >= 49 and i.get("active_phase_message_8_complete") != "2":
                    l_apm_msg_8_scheduled_count += 1
                #----for yes msgs-----
                if (date_today - ap1_date).days >= 49 and i.get("active_phase_message_8_complete") == "2":
                    l_apm_msg_8_yes_count += 1
                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=56) and i.get("active_phase_message_8_complete") != "2":
                    l_apm_msg_8_ip_count += 1
                #----for no msgs-----
                elif (date_today - ap1_date).days >= 49 and i.get("active_phase_message_8_complete") == "0":
                    l_apm_msg_8_no_count += 1

                #------check msg - 9--------------
                    #-----withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=56) > withdrawn_date):
                    l_apm_msg_9_withdrawn_count += 1
                #----scheduled msgs------
                if (date_today - ap1_date).days >= 56 and i.get("active_phase_message_9_complete") != "2":
                    l_apm_msg_9_scheduled_count += 1
                #----for yes msgs-----
                if (date_today - ap1_date).days >= 56 and i.get("active_phase_message_9_complete") == "2":
                    l_apm_msg_9_yes_count += 1
                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=63)   and i.get("active_phase_message_9_complete") != "2":
                    l_apm_msg_9_ip_count += 1
                #----for no msgs-----
                elif (date_today - ap1_date).days >= 56 and i.get("active_phase_message_9_complete") == "0":
                    l_apm_msg_9_no_count += 1

                #------check msg - 10--------------
                if withdrawn_date and (ap1_date + timedelta(days=63) > withdrawn_date):
                    l_apm_msg_10_withdrawn_count += 1
                #----scheduled msgs------
                if (date_today - ap1_date).days >= 63 and i.get("active_phase_message_10_complete") != "2":
                    l_apm_msg_10_scheduled_count += 1   
                #----for yes msgs-----
                if (date_today - ap1_date).days >= 63 and i.get("active_phase_message_10_complete") == "2":
                    l_apm_msg_10_yes_count += 1
                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=70) and i.get("active_phase_message_10_complete") != "2":
                    l_apm_msg_10_ip_count += 1
                #----for no msgs-----
                elif (date_today - ap1_date).days >= 63 and i.get("active_phase_message_10_complete") == "0":
                    l_apm_msg_10_no_count += 1

                #------check msg - 11--------------
                if withdrawn_date and (ap1_date + timedelta(days=70) > withdrawn_date):
                    l_apm_msg_11_withdrawn_count += 1
                #----scheduled msgs------
                if (date_today - ap1_date).days >= 70 and i.get("active_phase_message_11_complete") != "2":
                    l_apm_msg_11_scheduled_count += 1
                #----for yes msgs-----
                if (date_today - ap1_date).days >= 70 and i.get("active_phase_message_11_complete") == "2":
                    l_apm_msg_11_yes_count += 1
                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=77)  and i.get("active_phase_message_11_complete") != "2":
                    l_apm_msg_11_ip_count += 1
                #----for no msgs-----
                elif (date_today - ap1_date).days >= 70 and i.get("active_phase_message_11_complete") == "0":
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
                if (date_today - ap1_date).days >= 84 and i.get("maintenance_phase_message_1_complete") != "2":
                    e_mpm_msg_1_scheduled_count += 1

                #----for yes msgs-----
                if (date_today - ap1_date).days >= 84 and i.get("maintenance_phase_message_1_complete") == "2":
                    e_mpm_msg_1_yes_count += 1

                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=98)   and i.get("maintenance_phase_message_1_complete") != "2":
                    e_mpm_msg_1_ip_count += 1

                #----for no msgs-----
                elif (date_today - ap1_date).days >= 84 and i.get("maintenance_phase_message_1_complete") == "0":
                    e_mpm_msg_1_no_count += 1

                #------check msg - 2--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=98) > withdrawn_date):
                    e_mpm_msg_2_withdrawn_count += 1
                #----scheduled msgs------
                elif (date_today - ap1_date).days >= 98 and i.get("maintenance_phase_message_2_complete") != "2":
                    e_mpm_msg_2_scheduled_count += 1

                #----for yes msgs-----
                elif (date_today - ap1_date).days >= 98 and i.get("maintenance_phase_message_2_complete") == "2":
                    e_mpm_msg_2_yes_count += 1

                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=112) and i.get("maintenance_phase_message_2_complete") != "2":
                    e_mpm_msg_2_ip_count += 1

                #----for no msgs-----
                elif (date_today - ap1_date).days >= 98 and i.get("maintenance_phase_message_2_complete") == "0":
                    e_mpm_msg_2_no_count += 1

                #------check msg - 3--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=112) > withdrawn_date):
                    e_mpm_msg_3_withdrawn_count += 1
                #----for scheduled msgs------
                if (date_today - ap1_date).days >= 112 and i.get("maintenance_phase_message_3_complete") != "2":
                    e_mpm_msg_3_scheduled_count += 1

                #----for yes msgs-----
                if (date_today - ap1_date).days >= 112 and i.get("maintenance_phase_message_3_complete") == "2":
                    e_mpm_msg_3_yes_count += 1

                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=140)  and i.get("maintenance_phase_message_3_complete") != "2":
                    e_mpm_msg_3_ip_count += 1

                #----for no msgs-----
                elif (date_today - ap1_date).days >= 112 and i.get("maintenance_phase_message_3_complete") == "0":
                    e_mpm_msg_3_no_count += 1

                #------check msg - 4--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=140) > withdrawn_date):
                    e_mpm_msg_4_withdrawn_count += 1
                #----for scheduled msgs------
                if (date_today - ap1_date).days >= 140 and i.get("maintenance_phase_message_4_complete") != "2":
                    e_mpm_msg_4_scheduled_count += 1

                #----for yes msgs-----
                if (date_today - ap1_date).days >= 140 and i.get("maintenance_phase_message_4_complete") == "2":
                    e_mpm_msg_4_yes_count += 1  
                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=168)  and i.get("maintenance_phase_message_4_complete") != "2":
                    e_mpm_msg_4_ip_count += 1   
                #----for no msgs-----
                elif (date_today - ap1_date).days >= 140 and i.get("maintenance_phase_message_4_complete") == "0":
                    e_mpm_msg_4_no_count += 1

                #------check msg - 5--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=168) > withdrawn_date):
                    e_mpm_msg_5_withdrawn_count += 1  
                #----for scheduled msgs------
                if (date_today - ap1_date).days >= 168 and i.get("maintenance_phase_message_5_complete") != "2":
                    e_mpm_msg_5_scheduled_count += 1

                #----for yes msgs-----
                if (date_today - ap1_date).days >= 168 and i.get("maintenance_phase_message_5_complete") == "2":
                    e_mpm_msg_5_yes_count += 1
                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=196) and i.get("maintenance_phase_message_5_complete") != "2":
                    e_mpm_msg_5_ip_count += 1

                #----for no msgs-----
                elif (date_today - ap1_date).days >= 168 and i.get("maintenance_phase_message_5_complete") == "0":
                    e_mpm_msg_5_no_count += 1

                #------check msg - 6--------------
                if withdrawn_date and (ap1_date + timedelta(days=196) > withdrawn_date):
                    e_mpm_msg_6_withdrawn_count += 1
                #----for scheduled msgs------
                if (date_today - ap1_date).days >= 196 and i.get("maintenance_phase_message_6_complete") != "2":
                    e_mpm_msg_6_scheduled_count += 1
                #----for yes msgs-----
                if (date_today - ap1_date).days >= 196 and i.get("maintenance_phase_message_6_complete") == "2":
                    e_mpm_msg_6_yes_count += 1
                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=224)  and i.get("maintenance_phase_message_6_complete") != "2":
                    e_mpm_msg_6_ip_count += 1
                #----for no msgs-----
                elif (date_today - ap1_date).days >= 196 and i.get("maintenance_phase_message_6_complete") == "0":
                    e_mpm_msg_6_no_count += 1

                #------check msg - 7--------------
                    #----for withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=224) > withdrawn_date):
                    e_mpm_msg_7_withdrawn_count += 1
                #----for scheduled msgs------
                if (date_today - ap1_date).days >= 224 and i.get("maintenance_phase_message_7_complete") != "2":
                    e_mpm_msg_7_scheduled_count += 1
                #----for yes msgs-----
                if (date_today - ap1_date).days >= 224 and i.get("maintenance_phase_message_7_complete") == "2":
                    e_mpm_msg_7_yes_count += 1
                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=252)  and i.get("maintenance_phase_message_7_complete") != "2":
                    e_mpm_msg_7_ip_count += 1
                #----for no msgs-----
                elif (date_today - ap1_date).days >= 224 and i.get("maintenance_phase_message_7_complete") == "0":
                    e_mpm_msg_7_no_count += 1

                #------check msg - 8--------------  
                if withdrawn_date and (ap1_date + timedelta(days=252) > withdrawn_date):
                    e_mpm_msg_8_withdrawn_count += 1
                #----for scheduled msgs------
                if (date_today - ap1_date).days >= 252 and i.get("maintenance_phase_message_8_complete") != "2":
                    e_mpm_msg_8_scheduled_count += 1
                #----for yes msgs-----
                if (date_today - ap1_date).days >= 252 and i.get("maintenance_phase_message_8_complete") == "2":
                    e_mpm_msg_8_yes_count += 1
                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=280)  and i.get("maintenance_phase_message_8_complete") != "2":
                    e_mpm_msg_8_ip_count += 1
                #----for no msgs-----
                elif (date_today - ap1_date).days >= 252 and i.get("maintenance_phase_message_8_complete") == "0":
                    e_mpm_msg_8_no_count += 1

                #------check msg - 9--------------
                    #-----withdrawn participants-----
                if withdrawn_date and (ap1_date + timedelta(days=280) > withdrawn_date):
                    e_mpm_msg_9_withdrawn_count += 1
                #----scheduled msgs------
                if (date_today - ap1_date).days >= 280 and i.get("maintenance_phase_message_9_complete") != "2":
                    e_mpm_msg_9_scheduled_count += 1
                #----for yes msgs-----
                if (date_today - ap1_date).days >= 280 and i.get("maintenance_phase_message_9_complete") == "2":
                    e_mpm_msg_9_yes_count += 1
                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=308)  and i.get("maintenance_phase_message_9_complete") != "2":
                    e_mpm_msg_9_ip_count += 1
                #----for no msgs-----
                elif (date_today - ap1_date).days >= 280 and i.get("maintenance_phase_message_9_complete") == "0":
                    e_mpm_msg_9_no_count += 1

                #------check msg - 10--------------
                if withdrawn_date and (ap1_date + timedelta(days=308) > withdrawn_date):
                    e_mpm_msg_10_withdrawn_count += 1 
                #----for scheduled msgs------
                if (date_today - ap1_date).days >= 308 and i.get("maintenance_phase_message_10_complete") != "2":
                    e_mpm_msg_10_scheduled_count += 1  
                #----for yes msgs-----
                if (date_today - ap1_date).days >= 308 and i.get("maintenance_phase_message_11_complete") == "2":
                    e_mpm_msg_10_yes_count += 1
                #----for ip msgs-----
                elif ap1_date <= date_today < ap1_date + timedelta(days=336)  and i.get("maintenance_phase_message_11_complete") != "2":
                    e_mpm_msg_10_ip_count += 1
                #----for no msgs-----
                elif (date_today - ap1_date).days >= 308 and i.get("maintenance_phase_message_11_complete") == "0":
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

    e_pending_sessions = {s: [] for s in range(1, 10)}
    e_missed_sessions = {s: [] for s in range(1, 10)}

    l_pending_sessions = {s: [] for s in range(1, 10)}
    l_missed_sessions = {s: [] for s in range(1, 10)}

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
                s1_date = datetime.strptime(i['s1_date'], '%Y-%m-%d').date() if i.get('s1_date') else None  #Fixedd!!
                # print(f"S1 date: {s1_date}, Zoom appointment date: {zoom_appt_date} and rescord ID: {i.get('record_id')}")

                #----for withdrawn participants-----
                if withdrawn_date and zoom_appt_date >= withdrawn_date:
                    e_session_1_withdrawn_count += 1
                #----scheduled sessions------
                if (zoom_appt_date <= date_today):
                    e_session_1_scheduled_count += 1

                if s1_date:
                    e_session_1_completed_count += 1

                elif (zoom_appt_date + timedelta(days=7)) < date_today and s1_date is None:
                    e_missed_sessions[1].append(i.get("record_id"))
                    e_session_1_missed_count += 1

                elif zoom_appt_date <= date_today <= zoom_appt_date + timedelta(days=7) and s1_date is None:
                    # print(f"Pending session 1 for record ID: {i.get('record_id')} and zoom_appt_date {zoom_appt_date}" )
                    e_pending_sessions[1].append(i.get("record_id"))
                    e_session_1_pending_count += 1

            #-----checking session-2--------------
            if 's2_appoint' in i and i['s2_appoint'].strip():
                s2_appoint = datetime.strptime(i['s2_appoint'], '%Y-%m-%d').date()
                s2_date = datetime.strptime(i['s2_date'], '%Y-%m-%d').date() if i.get('s2_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and s2_appoint >= withdrawn_date:
                    e_session_2_withdrawn_count += 1
                #----scheduled sessions------
                if (s2_appoint <= date_today):
                    e_session_2_scheduled_count += 1
                if s2_date:
                    e_session_2_completed_count += 1

                elif (s2_appoint + timedelta(days=7) ) < date_today and s2_date is None:
                    e_missed_sessions[2].append(i.get("record_id"))
                    e_session_2_missed_count += 1

                elif s2_appoint <= date_today <= s2_appoint + timedelta(days=7) and s2_date is None:
                    e_pending_sessions[2].append(i.get("record_id"))
                    e_session_2_pending_count += 1

            #------checking session-3-------------- 
            if 's3_appoint' in i and i['s3_appoint'].strip():
                s3_appoint = datetime.strptime(i['s3_appoint'], '%Y-%m-%d').date()
                s3_date = datetime.strptime(i['s3_date'], '%Y-%m-%d').date() if i.get('s3_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and s3_appoint >= withdrawn_date:
                    e_session_3_withdrawn_count += 1

                #----scheduled sessions------
                if (s3_appoint <= date_today):
                    e_session_3_scheduled_count += 1

                if s3_date:
                    e_session_3_completed_count += 1

                elif (s3_appoint + timedelta(days=7) ) < date_today and s3_date is None:
                    e_missed_sessions[3].append(i.get("record_id"))
                    e_session_3_missed_count += 1

                elif s3_appoint <= date_today <= s3_appoint + timedelta(days=7) and s3_date is None:
                    e_pending_sessions[3].append(i.get("record_id"))
                    e_session_3_pending_count += 1

            #------checking session-4--------------
            if 's4_appoint' in i and i['s4_appoint'].strip():
                s4_appoint = datetime.strptime(i['s4_appoint'], '%Y-%m-%d').date()
                s4_date = datetime.strptime(i['s4_date'], '%Y-%m-%d').date() if i.get('s4_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and s4_appoint >= withdrawn_date:
                    e_session_4_withdrawn_count += 1
                #----scheduled sessions------
                if (s4_appoint <= date_today):
                    e_session_4_scheduled_count += 1

                if s4_date:
                    e_session_4_completed_count += 1

                elif (s4_appoint + timedelta(days=14) ) < date_today and s4_date is None:
                    e_missed_sessions[4].append(i.get("record_id"))
                    e_session_4_missed_count += 1

                elif s4_appoint <= date_today <= s4_appoint + timedelta(days=14) and s4_date is None:
                    e_pending_sessions[4].append(i.get("record_id"))
                    e_session_4_pending_count += 1

            #------checking session-5--------------
            if 's5_appoint' in i and i['s5_appoint'].strip():
                s5_appoint = datetime.strptime(i['s5_appoint'], '%Y-%m-%d').date()
                s5_date = datetime.strptime(i['s5_date'], '%Y-%m-%d').date() if i.get('s5_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and s5_appoint >= withdrawn_date:
                    e_session_5_withdrawn_count += 1
                #----scheduled sessions------
                if (s5_appoint <= date_today):
                    e_session_5_scheduled_count += 1
                if s5_date:
                    e_session_5_completed_count += 1

                elif (s5_appoint + timedelta(days=14) ) < date_today and s5_date is None:
                    e_missed_sessions[5].append(i.get("record_id"))
                    e_session_5_missed_count += 1

                elif s5_appoint <= date_today <= s5_appoint + timedelta(days=14) and s5_date is None:
                    e_pending_sessions[5].append(i.get("record_id"))
                e_session_5_pending_count += 1
        
            #--------checking session-6-----------
            if 's6_appoint' in i and i['s6_appoint'].strip():
                s6_appoint = datetime.strptime(i['s6_appoint'], '%Y-%m-%d').date()
                s6_date = datetime.strptime(i['s6_date'], '%Y-%m-%d').date() if i.get('s6_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and s6_appoint >= withdrawn_date:
                    e_session_6_withdrawn_count += 1
                #----scheduled sessions------
                if (s6_appoint <= date_today) and s6_date is None:
                    e_session_6_scheduled_count += 1

                if s6_date:
                    e_session_6_completed_count += 1

                elif (s6_appoint + timedelta(days=14) ) < date_today and s6_date is None:
                    e_missed_sessions[6].append(i.get("record_id"))
                    e_session_6_missed_count += 1

                elif s6_appoint <= date_today <= s6_appoint + timedelta(days=28) and s6_date is None:
                    e_pending_sessions[6].append(i.get("record_id"))
                    e_session_6_pending_count += 1

            #--------checking session-7-------
            if 's7_appoint' in i and i['s7_appoint'].strip():
                s7_appoint = datetime.strptime(i['s7_appoint'], '%Y-%m-%d').date()
                s7_date = datetime.strptime(i['s7_date'], '%Y-%m-%d').date() if i.get('s7_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and s7_appoint > withdrawn_date:
                    e_session_7_withdrawn_count += 1
                #----scheduled sessions------
                if (s7_appoint <= date_today):
                    # print(f"Scheduled session 7 for participant {i.get('record_id')} s7saved date: {s7_date} and s7 appointment date: {s7_appoint}")
                    e_session_7_scheduled_count += 1
                if s7_date:
                    # print(f"Completed session 7 for participant {i.get('record_id')} s7saved date: {s7_date} and s7 appointment date: {s7_appoint}")
                    e_session_7_completed_count += 1

                elif (s7_appoint + timedelta(days= 28)) < date_today and s7_date is None:
                    e_missed_sessions[7].append(i.get("record_id"))
                    e_session_7_missed_count += 1

                elif s7_appoint <= date_today <= s7_appoint + timedelta(days=28) and s7_date is None:
                    e_pending_sessions[7].append(i.get("record_id"))
                    e_session_7_pending_count += 1

            #--------checking session-8-------
            if 's8_appoint' in i and i['s8_appoint'].strip():
                s8_appoint = datetime.strptime(i['s8_appoint'], '%Y-%m-%d').date()
                s8_date = datetime.strptime(i['s8_date'], '%Y-%m-%d').date() if i.get('s8_date') else None
                # print(f"S8 date: {s8_date}, S8 appointment date: {s8_appoint} and rescord ID: {i.get('record_id')}")
                #----for withdrawn participants-----
                if withdrawn_date and s8_appoint >= withdrawn_date:
                    e_session_8_withdrawn_count += 1
                #----scheduled sessions------
                if (s8_appoint <= date_today):
                    # print(f"Scheduled session 8 for participant {i.get('record_id')} s8saved date: {s8_date} and s8 appointment date: {s8_appoint}")
                    e_session_8_scheduled_count += 1

                if s8_date:
                    # print(f"Completed session 8 for participant {i.get('record_id')} s8saved date: {s8_date} and s8 appointment date: {s8_appoint}")
                    e_session_8_completed_count += 1

                elif (s8_appoint + timedelta(days=28))< date_today and s8_date is None:
                    e_missed_sessions[8].append(i.get("record_id"))
                    e_session_8_missed_count += 1

                elif s8_appoint <= date_today <= s8_appoint + timedelta(days=28) and s8_date is None:
                    e_pending_sessions[8].append(i.get("record_id"))
                    e_session_8_pending_count += 1

            #--------checking session-9-------
            if 's9_appoint' in i and i['s9_appoint'].strip():
                s9_appoint = datetime.strptime(i['s9_appoint'], '%Y-%m-%d').date()
                s9_date = datetime.strptime(i['s9_date'], '%Y-%m-%d').date() if i.get('s9_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and s9_appoint >= withdrawn_date:
                    e_session_9_withdrawn_count += 1
                #----scheduled sessions------
                if (s9_appoint <= date_today):
                    # print(f"Scheduled session 9 for participant {i.get('record_id')} s9saved date: {s9_date} and s9 appointment date: {s9_appoint}")
                    e_session_9_scheduled_count += 1

                if s9_date:
                    # print(f"Completed session 9 for participant {i.get('record_id')} s9saved date: {s9_date} and s9 appointment date: {s9_appoint}")
                    e_session_9_completed_count += 1

                elif (s9_appoint + timedelta(days=28)) < date_today and s9_date is None:
                    e_missed_sessions[9].append(i.get("record_id"))
                    e_session_9_missed_count += 1

                elif s9_appoint <= date_today <= s9_appoint + timedelta(days=28) and s9_date is None:
                    e_pending_sessions[9].append(i.get("record_id"))
                    e_session_9_pending_count += 1

        #-------Later vCare Counseling Session-------

        elif group == '2':
            #-----checking session-1(human)--------------
            if 'zoom_appt_date' in i and i['zoom_appt_date'].strip():
                zoom_appt_date = datetime.strptime(i['zoom_appt_date'], '%Y-%m-%d').date()
                s1_date = datetime.strptime(i['s1_date'], '%Y-%m-%d').date() if i.get('s1_') else None

                #----for withdrawn participants-----
                if withdrawn_date and zoom_appt_date >= withdrawn_date:
                    l_session_1_withdrawn_count += 1
                #----scheduled sessions------
                if (zoom_appt_date <= date_today):
                    l_session_1_scheduled_count += 1

                if s1_date:
                    l_session_1_completed_count += 1

                elif (zoom_appt_date + timedelta(days=7)) < date_today and s1_date is None:
                    l_missed_sessions[1].append(i.get("record_id"))
                    l_session_1_missed_count += 1

                elif zoom_appt_date <= date_today <= zoom_appt_date + timedelta(days=7) and s1_date is None:
                    l_pending_sessions[1].append(i.get("record_id"))
                    l_session_1_pending_count += 1

            #-----checking session-2--------------
            if 's2_appoint' in i and i['s2_appoint'].strip():
                s2_appoint = datetime.strptime(i['s2_appoint'], '%Y-%m-%d').date()
                s2_date = datetime.strptime(i['s2_date'], '%Y-%m-%d').date() if i.get('s2_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and zoom_appt_date >= withdrawn_date:
                    l_session_2_withdrawn_count += 1
                #----scheduled sessions------
                elif (s2_appoint - date_today).days > 0 and s2_date is None:
                    l_session_2_scheduled_count += 1

                elif s2_date:
                    l_session_2_completed_count += 1

                elif (s2_appoint + timedelta(days=7) ) < date_today and s2_date is None:
                    l_missed_sessions[2].append(i.get("record_id"))
                    l_session_2_missed_count += 1

                elif s2_appoint <= date_today <= s2_appoint + timedelta(days=7) and s2_date is None:
                    l_pending_sessions[2].append(i.get("record_id"))
                    l_session_2_pending_count += 1

            #------checking session-3-------------- 
            if 's3_appoint' in i and i['s3_appoint'].strip():
                s3_appoint = datetime.strptime(i['s3_appoint'], '%Y-%m-%d').date()
                s3_date = datetime.strptime(i['s3_date'], '%Y-%m-%d').date() if i.get('s3_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and zoom_appt_date >= withdrawn_date:
                    l_session_3_withdrawn_count += 1
                #----scheduled sessions------
                elif (s3_appoint - date_today).days > 0 and s3_date is None:
                    l_session_3_scheduled_count += 1

                elif s3_date:
                    l_session_3_completed_count += 1

                elif (s3_appoint + timedelta(days=7) ) < date_today and s3_date is None:
                    l_missed_sessions[3].append(i.get("record_id"))
                    l_session_3_missed_count += 1

                elif s3_appoint <= date_today <= s3_appoint + timedelta(days=7) and s3_date is None:
                    l_pending_sessions[3].append(i.get("record_id"))
                    l_session_3_pending_count += 1

            #------checking session-4--------------
            if 's4_appoint' in i and i['s4_appoint'].strip():
                s4_appoint = datetime.strptime(i['s4_appoint'], '%Y-%m-%d').date()
                s4_date = datetime.strptime(i['s4_date'], '%Y-%m-%d').date() if i.get('s4_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and zoom_appt_date >= withdrawn_date:
                    l_session_4_withdrawn_count += 1
                #----scheduled sessions------
                elif (s4_appoint - date_today).days > 0 and s4_date is None:
                    l_session_4_scheduled_count += 1
                elif s4_date:
                    l_session_4_completed_count += 1

                elif (s4_appoint + timedelta(days=14) ) < date_today and s4_date is None:
                    l_missed_sessions[4].append(i.get("record_id"))
                    l_session_4_missed_count += 1

                elif s4_appoint <= date_today <= s4_appoint + timedelta(days=14) and s4_date is None:
                    l_pending_sessions[4].append(i.get("record_id"))
                    l_session_4_pending_count += 1

            #------checking session-5--------------
            if 's5_appoint' in i and i['s5_appoint'].strip():
                s5_appoint = datetime.strptime(i['s5_appoint'], '%Y-%m-%d').date()
                s5_date = datetime.strptime(i['s5_date'], '%Y-%m-%d').date() if i.get('s5_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and zoom_appt_date >= withdrawn_date:
                    l_session_5_withdrawn_count += 1
                #----scheduled sessions------
                elif (s5_appoint - date_today).days > 0 and s5_date is None:
                    l_session_5_scheduled_count += 1
                elif s5_date:
                    l_session_5_completed_count += 1

                elif (s5_appoint + timedelta(days=14) ) < date_today and s5_date is None:
                    l_missed_sessions[5].append(i.get("record_id"))
                    l_session_5_missed_count += 1

                elif s5_appoint <= date_today <= s5_appoint + timedelta(days=14) and s5_date is None:
                    l_pending_sessions[5].append(i.get("record_id"))
                    l_session_5_pending_count += 1

            #--------checking session-6------------
            if 's6_appoint' in i and i['s6_appoint'].strip():
                s6_appoint = datetime.strptime(i['s6_appoint'], '%Y-%m-%d').date()
                s6_date = datetime.strptime(i['s6_date'], '%Y-%m-%d').date() if i.get('s6_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and zoom_appt_date >= withdrawn_date:
                    l_session_6_withdrawn_count += 1
                #----scheduled sessions------
                elif (s6_appoint - date_today).days > 0 and s6_date is None:
                    l_session_6_scheduled_count += 1

                elif s6_date:
                    l_session_6_completed_count += 1

                elif (s6_appoint + timedelta(days=14) ) < date_today and s6_date is None:
                    l_missed_sessions[6].append(i.get("record_id"))
                    l_session_6_missed_count += 1

                elif s6_appoint <= date_today <= s6_appoint + timedelta(days=28) and s6_date is None:
                    l_pending_sessions[6].append(i.get("record_id"))
                    l_session_6_pending_count += 1

            #--------checking session-7-------
            if 's7_appoint' in i and i['s7_appoint'].strip():
                s7_appoint = datetime.strptime(i['s7_appoint'], '%Y-%m-%d').date()
                s7_date = datetime.strptime(i['s7_date'], '%Y-%m-%d').date() if i.get('s7_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and zoom_appt_date >= withdrawn_date:
                    l_session_7_withdrawn_count += 1
                #----scheduled sessions------
                elif (s7_appoint - date_today).days > 0 and s7_date is None:
                    l_session_7_scheduled_count += 1
                elif s7_date:
                    l_session_7_completed_count += 1

                elif (s7_appoint + timedelta(days= 28)) < date_today and s7_date is None:
                    l_missed_sessions[7].append(i.get("record_id"))
                    l_session_7_missed_count += 1

                elif s7_appoint <= date_today <= s7_appoint + timedelta(days=28) and s7_date is None:
                    l_pending_sessions[7].append(i.get("record_id"))
                    l_session_7_pending_count += 1

            #--------checking session-8-------
            if 's8_appoint' in i and i['s8_appoint'].strip():
                s8_appoint = datetime.strptime(i['s8_appoint'], '%Y-%m-%d').date()
                s8_date = datetime.strptime(i['s8_date'], '%Y-%m-%d').date() if i.get('s8_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and zoom_appt_date >= withdrawn_date:
                    l_session_8_withdrawn_count += 1
                #----scheduled sessions------
                elif (s8_appoint - date_today).days > 0 and s8_date is None:
                    l_session_8_scheduled_count += 1

                elif s8_date:
                    l_session_8_completed_count += 1

                elif (s8_appoint + timedelta(days=28))< date_today and s8_date is None:
                    l_missed_sessions[8].append(i.get("record_id"))
                    l_session_8_missed_count += 1

                elif s8_appoint <= date_today <= s8_appoint + timedelta(days=28) and s8_date is None:
                    l_pending_sessions[8].append(i.get("record_id"))
                    l_session_8_pending_count += 1

            #--------checking session-9-------
            if 's9_appoint' in i and i['s9_appoint'].strip():
                s9_appoint = datetime.strptime(i['s9_appoint'], '%Y-%m-%d').date()
                s9_date = datetime.strptime(i['s9_date'], '%Y-%m-%d').date() if i.get('s9_date') else None

                #----for withdrawn participants-----
                if withdrawn_date and zoom_appt_date >= withdrawn_date:
                    l_session_9_withdrawn_count += 1
                #----scheduled sessions------
                elif (s9_appoint - date_today).days > 0 and s9_date is None:
                    l_session_9_scheduled_count += 1
                elif s9_date:
                    l_session_9_completed_count += 1

                elif (s9_appoint + timedelta(days=28)) < date_today and s9_date is None:
                    l_missed_sessions[9].append(i.get("record_id"))
                    l_session_9_missed_count += 1

                elif s9_appoint <= date_today <= s9_appoint + timedelta(days=28) and s9_date is None:
                    l_pending_sessions[9].append(i.get("record_id"))
                    l_session_9_pending_count += 1

# print(f"Early vCare Counseling Session - Pending: {e_pending_sessions}")
# print(f"Early vCare Counseling Session - Missed: {e_missed_sessions}")

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

    tech_check_overdue_list =[]
    eval_survet_overdue_list = []
    #--------Additional Surveys-------- 
    for i in response_json:
        # Get the date of withdrawal if it exists
        withdrawn_date = i.get('date_of_withdrawal', '').strip()
    #-----------tech check survey -----------
        if i['s2_date'].strip():

            s2_date = datetime.strptime(i['s2_date'], "%Y-%m-%d").date()
            if i['participant_status'] == '3' and s2_date >= withdrawn_date and i['technical_check_survey_complete'] != '2':
                tech_check_withdrawals += 1

            # Scheduled 
            if s2_date <= date_today:
                tech_check_scheduled += 1

        # Completed
            if i['technical_check_survey_complete'] == '2':
                tech_check_completed += 1

        # Not yet due
            elif i['technical_check_survey_complete'] != '2' and s2_date > date_today:
                tech_check_not_yet_due += 1

        # Overdue
            elif i['technical_check_survey_complete'] != '2' and (s2_date - date_today).days < 0:
                tech_check_overdue_list.append(i.get("record_id"))
                tech_check_overdue += 1

        #--------valuation survey-------------
        if i['s9_date'].strip()  :
            s9_appoint = datetime.strptime(i["s9_date"], "%Y-%m-%d").date()
            if i['participant_status'] == '3' and i['evaluation_survey_complete'] != '2' and s9_appoint > withdrawn_date:
                eval_withdrawals += 1

            #  Scheduled
            if s9_date <= date_today:
                eval_scheduled += 1

                #  Completed
            if i['evaluation_survey_complete'] == '2':
                eval_completed += 1

            # Not yet due
            elif i['evaluation_survey_complete'] != '2' and s9_date > date_today:
                eval_not_yet_due += 1

            # Overdue
            elif i['evaluation_survey_complete'] != '2' and (s9_date - date_today).days < 0:
                eval_survet_overdue_list.append(i.get("record_id"))
                eval_overdue += 1

        #--------on demand session-------------
        if i['participant_status'] == '3':
            on_demand_withdrawals += 1

        elif i.get('adhoc_date') and i.get('ad_hoc_completed_session'):
            on_demand_completed += 1

    print(tech_check_overdue_list)
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
        # 'fields[13]': 'ad_hoc_completed_session',
        # 'fields[14]': 'adhoc_date',
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

    e_overdue_phq9 = {s: [] for s in range(1, 10)}
    e_expected_phq9 = {s: [] for s in range(1, 10)}

    l_overdue_phq9 = {s: [] for s in range(1, 10)}
    l_expected_phq9 = {s: [] for s in range(1, 10)}


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

        if record.get("randomization_group"):
            phq_9_session_dates[record_id]["randomization_group"] = record["randomization_group"]

        if record.get("adhoc_date"):
            phq_9_session_dates[record_id]["adhoc_date"] = record["adhoc_date"]

        if record.get("adhoc_completed_session"):
            phq_9_session_dates[record_id]["adhoc_completed_session"] = record["adhoc_completed_session"]

    # print(phq_9_session_dates)

    # #--------table 4------------
        #-------Early vCare PHQ-9 Status-------
    for i in response_json1:
        group = phq_9_session_dates.get(i['record_id'], {}).get('randomization_group')
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
            # print(f"Processing record {i['record_id']} ans s1appoint {s1_appoint} and today's date {date_today} lumen_administered_phq9_complete: {i.get('lumen_administered_phq9_complete')} redcap_event_name: {i['redcap_event_name']}")
            #-----checking phq-9 score--------------
            # print(f"PHQ-9 checking for record {i['record_id']} on {s1_appoint} and redcap event {i['redcap_event_name']} lumen_administered_phq9_complete: {i.get('lumen_administered_phq9_complete')}")
            # Session 1 (Human)
            if s1_appoint and s1_appoint.strip() and i['redcap_event_name'] == 'session_1_arm_1':
                s1_appoint = datetime.strptime(s1_appoint, '%Y-%m-%d').date()
                # print(f"PHQ-9 checking for record {i['record_id']} on {s1_appoint}")
                if i.get('lumen_administered_phq9_complete') == '2' and s1_appoint <= date_today:
                    # print(f"PHQ-9 completed for record {i['record_id']} on {s1_appoint}")
                    e_phq9_completed_s1_count += 1

                elif i.get('lumen_administered_phq9_complete') != '2' and s1_appoint <= date_today < s1_appoint + timedelta(days=7):
                    e_expected_phq9[1].append(i.get("record_id"))
                    e_phq9_expected_s1_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and date_today >= s1_appoint + timedelta(days=7):
                    e_overdue_phq9[1].append(i.get("record_id"))
                    e_phq9_overdue_s1_count += 1
                else:
                    pass

            # Session 2
            if i['redcap_event_name'] == 'session_2_arm_1' and s2_appoint and s2_appoint.strip():
                s2_appoint = datetime.strptime(s2_appoint, '%Y-%m-%d').date()
                if i.get('lumen_administered_phq9_complete') == '2' and s2_appoint <= date_today:
                    e_phq9_completed_s2_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s2_appoint <= date_today < s2_appoint + timedelta(days=7):
                    e_expected_phq9[2].append(i.get("record_id"))
                    e_phq9_expected_s2_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and date_today >= s2_appoint + timedelta(days=14):
                    e_overdue_phq9[2].append(i.get("record_id"))
                    e_phq9_overdue_s2_count += 1
                else:
                    pass
            # Session 3
            if i['redcap_event_name'] == 'session_3_arm_1' and s3_appoint and s3_appoint.strip():
                s3_appoint = datetime.strptime(s3_appoint, '%Y-%m-%d').date()
                if i.get('lumen_administered_phq9_complete') == '2' and s3_appoint <= date_today:
                    e_phq9_completed_s3_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s3_appoint <= date_today < s3_appoint + timedelta(days=7):
                    e_expected_phq9[3].append(i.get("record_id"))
                    e_phq9_expected_s3_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and date_today >= s3_appoint + timedelta(days=14):
                    e_overdue_phq9[3].append(i.get("record_id"))
                    e_phq9_overdue_s3_count += 1
                else:
                    pass

            # Session 4
            if i['redcap_event_name'] == 'session_4_arm_1' and s4_appoint and s4_appoint.strip():
                s4_appoint = datetime.strptime(s4_appoint, '%Y-%m-%d').date()
                if i.get('lumen_administered_phq9_complete') == '2' and s4_appoint <= date_today:
                    e_phq9_completed_s4_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s4_appoint <= date_today < s4_appoint + timedelta(days=14):
                    e_expected_phq9[4].append(i.get("record_id"))
                    print(f"Expected PHQ-9 for record {i['record_id']} on {s4_appoint}")
                    e_phq9_expected_s4_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and date_today >= s4_appoint + timedelta(days=14):
                    e_overdue_phq9[4].append(i.get("record_id"))
                    e_phq9_overdue_s4_count += 1
                else:
                    pass
                
            # Session 5
            if i['redcap_event_name'] == 'session_5_arm_1' and s5_appoint and s5_appoint.strip():
                s5_appoint = datetime.strptime(s5_appoint, '%Y-%m-%d').date()
                if i.get('lumen_administered_phq9_complete') == '2' and s5_appoint <= date_today:
                    e_phq9_completed_s5_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s5_appoint <= date_today < s5_appoint + timedelta(days=14):
                    e_expected_phq9[5].append(i.get("record_id"))
                    e_phq9_expected_s5_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and date_today >= s5_appoint + timedelta(days=14):
                    e_overdue_phq9[5].append(i.get("record_id"))
                    e_phq9_overdue_s5_count += 1
                else:
                    pass

            # Session 6
            if i['redcap_event_name'] == 'session_6_arm_1' and s6_appoint and s6_appoint.strip():
                s6_appoint = datetime.strptime(s6_appoint, '%Y-%m-%d').date()
                if i.get('lumen_administered_phq9_complete') == '2' and s6_appoint <= date_today:
                    e_phq9_completed_s6_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s6_appoint <= date_today < s6_appoint + timedelta(days=28):
                    e_expected_phq9[6].append(i.get("record_id"))
                    e_phq9_expected_s6_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and date_today >= s6_appoint + timedelta(days=14):
                    e_overdue_phq9[6].append(i.get("record_id"))
                    e_phq9_overdue_s6_count += 1
                else:
                    pass

            # Session 7
            if i['redcap_event_name'] == 'session_7_arm_1' and s7_appoint and s7_appoint.strip():
                s7_appoint = datetime.strptime(s7_appoint, '%Y-%m-%d').date()
                if i.get('lumen_administered_phq9_complete') == '2' and s7_appoint <= date_today:
                    e_phq9_completed_s7_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s7_appoint <= date_today < s7_appoint + timedelta(days=28):
                    e_expected_phq9[7].append(i.get("record_id"))
                    e_phq9_expected_s7_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and date_today >= s7_appoint + timedelta(days=14):
                    e_overdue_phq9[7].append(i.get("record_id"))
                    e_phq9_overdue_s7_count += 1
                else:
                    pass

            # Session 8
            if i['redcap_event_name'] == 'session_8_arm_1' and s8_appoint and s8_appoint.strip():
                s8_appoint = datetime.strptime(s8_appoint, '%Y-%m-%d').date()
                if i.get('lumen_administered_phq9_complete') == '2' and s8_appoint <= date_today:
                    e_phq9_completed_s8_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s8_appoint <= date_today < s8_appoint + timedelta(days=28):
                    e_expected_phq9[8].append(i.get("record_id"))
                    e_phq9_expected_s8_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and date_today >= s8_appoint + timedelta(days=14):
                    e_overdue_phq9[8].append(i.get("record_id"))
                    e_phq9_overdue_s8_count += 1
                else:
                    pass

            # Session 9
            if i['redcap_event_name'] == 'session_9_arm_1' and s9_appoint and s9_appoint.strip():
                s9_appoint = datetime.strptime(s9_appoint, '%Y-%m-%d').date()
                if i.get('lumen_administered_phq9_complete') == '2' and s9_appoint <= date_today:
                    e_phq9_completed_s9_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s9_appoint <= date_today < s9_appoint + timedelta(days=28):
                    e_expected_phq9[9].append(i.get("record_id"))
                    e_phq9_expected_s9_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and date_today >= s5_appoint + timedelta(days=14):
                    e_overdue_phq9[9].append(i.get("record_id"))
                    e_phq9_overdue_s9_count += 1
                else:
                    pass
        #-------Later vCare PHQ-9 Status-------
        if group == '2':

            #-----checking phq-9 score--------------

                # Session 1 (Human)
            if s1_appoint in i and s1_appoint.strip() and i['redcap_event_name'] == 'session_1_arm_1':
                s1_appoint = datetime.strptime(s1_appoint, '%Y-%m-%d').date()

                if i.get('lumen_administered_phq9_complete') == '2' and s1_appoint <= date_today:
                    l_phq9_completed_s1_count += 1

                elif i.get('lumen_administered_phq9_complete') != '2' and s1_appoint <= date_today < s1_appoint + timedelta(days=7):
                    l_expected_phq9[1].append(i.get("record_id"))
                    l_phq9_expected_s1_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and date_today >= s1_appoint + timedelta(days=14):
                    l_overdue_phq9[1].append(i.get("record_id"))
                    l_phq9_overdue_s1_count += 1
                else:
                    pass

            # Session 2
            if i['redcap_event_name'] == 'session_2_arm_1' and s2_appoint:
                if i.get('lumen_administered_phq9_complete') == '2' and s2_appoint <= date_today:
                    l_phq9_completed_s2_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s2_appoint <= date_today < s2_appoint + timedelta(days=7):
                    l_expected_phq9[2].append(i.get("record_id"))
                    l_phq9_expected_s2_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and date_today >= s2_appoint + timedelta(days=14):
                    l_overdue_phq9[2].append(i.get("record_id"))
                    l_phq9_overdue_s2_count += 1
                else:
                    pass
            # Session 3
            if i['redcap_event_name'] == 'session_3_arm_1' and s3_appoint:
                if i.get('lumen_administered_phq9_complete') == '2' and s3_appoint <= date_today:
                    l_phq9_completed_s3_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s3_appoint < date_today < s3_appoint + timedelta(days=7):
                    l_expected_phq9[3].append(i.get("record_id"))
                    l_phq9_expected_s3_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and date_today >= s3_appoint + timedelta(days=14):
                    l_overdue_phq9[3].append(i.get("record_id"))
                    l_phq9_overdue_s3_count += 1
                else:
                    pass

            # Session 4
            if i['redcap_event_name'] == 'session_4_arm_1' and s4_appoint:
                if i.get('lumen_administered_phq9_complete') == '2' and s4_appoint <= date_today:
                    l_phq9_completed_s4_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s4_appoint <= date_today < date_today + timedelta(days=14):
                    l_expected_phq9[4].append(i.get("record_id"))
                    l_phq9_expected_s4_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and date_today >= s4_appoint + timedelta(days=14):
                    l_overdue_phq9[4].append(i.get("record_id"))
                    l_phq9_overdue_s4_count += 1
                else:
                    pass

            # Session 5
            if i['redcap_event_name'] == 'session_5_arm_1' and s5_appoint:
                if i.get('lumen_administered_phq9_complete') == '2' and s5_appoint <= date_today:
                    l_phq9_completed_s5_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s5_appoint <= date_today < date_today + timedelta(days=14):
                    l_expected_phq9[5].append(i.get("record_id"))
                    l_phq9_expected_s5_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and date_today >= s5_appoint + timedelta(days=14):
                    l_overdue_phq9[5].append(i.get("record_id"))
                    l_phq9_overdue_s5_count += 1
                else:
                    pass

            # Session 6
            if i['redcap_event_name'] == 'session_6_arm_1' and s6_appoint:
                if i.get('lumen_administered_phq9_complete') == '2' and s6_appoint <= date_today:
                    l_phq9_completed_s6_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s6_appoint <= date_today < date_today + timedelta(days=28):   
                    l_expected_phq9[6].append(i.get("record_id"))
                    l_phq9_expected_s6_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and date_today >= s6_appoint + timedelta(days=14):
                    l_overdue_phq9[6].append(i.get("record_id"))
                    l_phq9_overdue_s6_count += 1
                else:
                    pass

                # Session 7
            if i['redcap_event_name'] == 'session_7_arm_1' and s7_appoint:
                if i.get('lumen_administered_phq9_complete') == '2' and s7_appoint <= date_today:
                    l_phq9_completed_s7_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s7_appoint <= date_today < date_today + timedelta(days=28):
                    l_expected_phq9[7].append(i.get("record_id"))
                    l_phq9_expected_s7_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and date_today >= s7_appoint + timedelta(days=14):
                    l_overdue_phq9[7].append(i.get("record_id"))
                    l_phq9_overdue_s7_count += 1
                else:
                    pass

            # Session 8
            if i['redcap_event_name'] == 'session_8_arm_1' and s8_appoint:
                if i.get('lumen_administered_phq9_complete') == '2' and s8_appoint <= date_today:
                    l_phq9_completed_s8_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s8_appoint <= date_today < date_today + timedelta(days=28):
                    l_expected_phq9[8].append(i.get("record_id"))
                    l_phq9_expected_s8_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and date_today >= s8_appoint + timedelta(days=14):
                    l_overdue_phq9[8].append(i.get("record_id"))
                    l_phq9_overdue_s8_count += 1
                else:
                    pass

            # Session 9
            if i['redcap_event_name'] == 'session_9_arm_1' and s9_appoint:
                if i.get('lumen_administered_phq9_complete') == '2' and s9_appoint <= date_today:
                    l_phq9_completed_s9_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and s9_appoint <= date_today < date_today + timedelta(days=28):
                    l_expected_phq9[9].append(i.get("record_id"))
                    l_phq9_expected_s9_count += 1
                elif i.get('lumen_administered_phq9_complete') != '2' and date_today >= s9_appoint + timedelta(days=14):
                    l_overdue_phq9[9].append(i.get("record_id"))
                    l_phq9_overdue_s9_count += 1
                else:
                    pass

    # print(e_overdue_phq9)
    # print(e_expected_phq9)

        results_json = {
        "Table_1": {
        "Early": {
            "Total": e_total_table_1,
            "Early Rand-1 Notified by phone": e_rand_notified_by_phn_count,
            "Early Rand-2 Notified by phone": 0,
            "Early Intervention Withdrawal": e_intervention_withdrawal,
            "Early Post Rand Exclusion": e_post_rand_excl
        },
        "Later": {
            "Total": l_total_table_1,
            "Later Rand-1 Notified by phone": l_rand_notified_by_phn_count,
            "Later Rand-2 Notified by phone": l_rand_2_notified_by_phn_count,
            "Later Intervention Withdrawal": l_intervention_withdrawal,
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
            },
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
        },
        
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
        },
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
    },
        "Missed Session": {
                "Early Pending Session" : e_pending_sessions,
                "Early Missed Session": e_pending_sessions,
                "Later Pending Session": l_pending_sessions,
                "Later Missed Session": l_pending_sessions
            },
    
        "Missed PHQ-9": {
            "Early expected PHQ-9": e_expected_phq9,
            "Early Overdue PHQ-9": e_overdue_phq9,
            "Later Expected PHQ-9": l_expected_phq9,
            "Later Overdue PHQ-9": l_overdue_phq9
        },
        "Missed Teck-check": {
        "Tech check overdue": tech_check_overdue_list,
        "Eval check overdue": eval_survet_overdue_list
        }
    }

    return results_json
