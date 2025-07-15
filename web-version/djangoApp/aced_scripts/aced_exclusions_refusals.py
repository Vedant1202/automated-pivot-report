import requests
import urllib.request, urllib.parse
import json

# import pandas as pd
from datetime import datetime, timedelta

def getExclusionsRefusalsData():
    datacall = {
        # 'token': '5D8E1721D73344CAA8B62EDE0ADE8ED9',
        'token': '47F4F8FA1815CC6DEF2C77FAE213ABB3',
        'content': 'record',
        'action': 'export',
        'format': 'json',
        'type': 'flat',
        'csvDelimiter': '',
        'fields[0]': 'record_id',
        'fields[1]': 'vol_excl2',
        # 'fields[2]': 'date_invite_1',
        'fields[3]': 'vol_excl',
        'fields[4]': 'es_english',
        'fields[5]': 'age_under',
        'fields[6]': 'age_over',
        'fields[7]': 'es_computer',
        'fields[8]': 'phq9_score_ra',
        'fields[9]': 'phq9_suicide_plan',
        'fields[10]': 'mh_exclusions_ed',
        'fields[11]': 'mh_exclusions_ed_2',
        'fields[12]': 'mh_exclusions_bpd',
        'fields[13]': 'mh_exclusions_ocd',
        'fields[14]': 'mh_exclusions_ptsd',
        'fields[15]': 'mh_exclusions_ptsd_2',
        'fields[16]': 'mh_exclusions_psych',
        'fields[17]': 'mh_exclusions_aud_sud',
        'fields[18]': 'mh_exclusions_aud_sud_2',
        'fields[19]': 'mh_exclusions_adhd',
        'fields[20]': 'mh_exclusions_neuro',
        'fields[21]': 'mh_exclusions_color',
        'fields[22]': 'mh_exclusions_vision',
        'fields[23]': 'mh_exclusions_move',
        'fields[24]': 'to_inelig_why',
        'fields[25]': 'mini_suicide_plan',
        'fields[26]': 'mdec_oc',
        'fields[27]': 'pdd_oc',
        'fields[28]': 'mini_x_oc',
        'fields[29]': 'invite_yn',
        'fields[30]': 'screen_icf_oc',
        'fields[31]': 'decline_ies',
        'fields[32]': 'why_decline_to',
        'fields[33]': 'to_appt_decline',
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

    # print("Received Data")
    today = datetime.today().date()

    # Initialize counters for exclusion reasons
    pts_not_fluent_in_english = 0
    pts_age_years = 0
    pts_no_internet_access = 0
    pts_impediment = 0
    pts_deceased = 0
    pts_other_exclusion = 0
    screening_not_fluent_in_english = 0
    screening_age_years = 0
    screening_no_internet_access = 0
    screening_phq9_score = 0
    screening_suicidality_plan = 0
    screening_eating_disorder = 0
    screening_bipolar_disorder = 0
    screening_ocd_disorder = 0
    screening_ptsd_disorder = 0
    screening_psychosis = 0
    screening_alcohol_substance_abuse = 0
    screening_adhd_disorder = 0
    screening_neuro_disorder = 0
    screening_impediment = 0
    to_not_fluent_in_english = 0
    to_age_years = 0
    to_no_internet_access = 0
    to_suicidality_plan = 0
    to_impediment = 0
    to_deceased = 0
    to_no_major_depression_disorder = 0
    to_other_exclusion = 0
    screening_not_interested = 0
    screening_too_busy = 0
    screening_dislike_tech = 0
    screening_privacy_concern = 0
    screening_other_concern = 0
    screening_decline_to_state = 0
    to_not_interested = 0
    to_too_busy = 0
    to_dislike_tech = 0
    to_privacy_concern = 0
    to_other_concern = 0
    to_decline_to_state = 0


    #Exclusions
    for i in response_json:
        if i['vol_excl2'] != '':
            if i['vol_excl'] == '1':
                pts_not_fluent_in_english += 1
            if i['vol_excl'] == '2':
                pts_age_years += 1

            if i['vol_excl'] == '3':
                pts_no_internet_access += 1 

            if i['vol_excl'] == '5':
                pts_impediment += 1 

            if i['vol_excl'] == '6':
                pts_deceased += 1

            if i['vol_excl'] == '4' or i['vol_excl'] == '7':
                pts_other_exclusion += 1
        

    for i in response_json:
        if i['es_english'] == '2':
            screening_not_fluent_in_english += 1 
        
        if i['age_under'] == '0' or i['age_over'] == '0':
            screening_age_years += 1

        if i['es_computer'] == '2':
            screening_no_internet_access += 1
        
        if i['phq9_score_ra'] < '10' and (i['phq9_suicide_plan'] != '1'):
            screening_phq9_score += 1
        
        if i['phq9_score_ra'] in ['1' , '99']:
            screening_suicidality_plan += 1
        
        if i['mh_exclusions_ed'] == '1' and i['mh_exclusions_ed_2'] == '1':
            screening_eating_disorder += 1
        
        if i['mh_exclusions_bpd'] == '1':
            screening_bipolar_disorder += 1

        if i['mh_exclusions_ocd'] == '1':
            screening_ocd_disorder += 1
            
        if i['mh_exclusions_ptsd'] == '1' or i['mh_exclusions_ptsd_2'] == '1':
            screening_ptsd_disorder += 1

        if i['mh_exclusions_psych'] == '1':
            screening_psychosis += 1

        if i['mh_exclusions_aud_sud'] == '1' or i['mh_exclusions_aud_sud_2'] == '1':
            screening_alcohol_substance_abuse += 1
        
        if i['mh_exclusions_adhd'] == '1':
            screening_adhd_disorder += 1

        if i['mh_exclusions_neuro'] == '1':
            screening_neuro_disorder += 1

        if i['mh_exclusions_color'] == '1' or i['mh_exclusions_vision'] == '2' or i['mh_exclusions_move'] == '1':
            screening_impediment += 1


    for i in response_json:
        if i['to_inelig_why'] == '1':
            to_not_fluent_in_english += 1

        if i['to_inelig_why'] == '2':
            to_age_years += 1

        if i['to_inelig_why'] == '3':
            to_no_internet_access += 1

        if i['mini_suicide_plan'] in ['1','99']:
            to_suicidality_plan += 1

        if i['to_inelig_why'] == '5':
            to_impediment += 1

        if (i['mdec_oc'] == '0' and i['pdd_oc'] == '0' and i['mini_x_oc'] == '0' and  (i['mini_suicide_plan']  not in[ '1' ,'99'] )) or i['to_inelig_why'] == '8':
            to_no_major_depression_disorder += 1

        if i['to_inelig_why'] == '6':
            to_deceased += 1

        if i['to_inelig_why'] in ['4', '7']:
            to_other_exclusion += 1

    #Refusals
    for i in response_json:
        if i['invite_yn']== '2' or  i['screen_icf_oc'] == '2' or i['decline_ies'] == '1':
            screening_not_interested += 1

        if i['decline_ies'] == '4':
            screening_too_busy += 1

        if i['decline_ies'] == '2':
            screening_dislike_tech += 1 
        
        if i['decline_ies'] == '3':
            screening_privacy_concern += 1

        if i['decline_ies'] == '6':
            screening_other_concern += 1

        if i['decline_ies'] == '7':
            screening_decline_to_state += 1

    for i in response_json:
        if i['why_decline_to'] == '1' or i['to_appt_decline'] == '1':
            to_not_interested += 1

        if i['why_decline_to'] == '2' or i['to_appt_decline'] == '3':
            to_too_busy += 1

        if i['why_decline_to'] == '3' or i['to_appt_decline'] == '4':
            to_dislike_tech += 1

        if i['why_decline_to'] == '4' or i['to_appt_decline'] == '5':
            to_privacy_concern += 1

        if i['why_decline_to'] == '5' or i['to_appt_decline'] == '8':
            to_other_concern += 1

        if i['why_decline_to'] == '6' or i['to_appt_decline'] == '9':
            to_decline_to_state += 1

    result_json = {
        "Exclusions": {
            "Prior To Screening": {
                "Not Fluent in English": pts_not_fluent_in_english,
                "Age <18 or >65": pts_age_years,
                "No Computer/Internet Access": pts_no_internet_access,
                "Impediment to Vision Hearing or hand movement": pts_impediment,
                "Deceased": pts_deceased,
                "Other Exclusion": pts_other_exclusion,
                "Exclusion Total": pts_not_fluent_in_english + pts_age_years + pts_no_internet_access + pts_impediment + pts_deceased + pts_other_exclusion
            },
            "Screening": {
                "Not Fluent in Englishh": screening_not_fluent_in_english,
                "Age <18 or > 65": screening_age_years,
                "No Computer/Internet Access": screening_no_internet_access,
                "PHQ9 < 10": screening_phq9_score,
                "Suicidality with active plan": screening_suicidality_plan,
                "Eating Disorder": screening_eating_disorder,
                "Bipolar Disorder": screening_bipolar_disorder,
                "OCD": screening_ocd_disorder,
                "PTSD": screening_ptsd_disorder,
                "Psychosis": screening_psychosis,
                "Alcohol or substance abuse disorder": screening_alcohol_substance_abuse,
                "ADHD Disorder": screening_adhd_disorder,
                "Neurological condition or brain injury": screening_neuro_disorder, 
                "Impediment to Vision Hearing or hand movement": screening_impediment,
                "Exclusion Total": screening_not_fluent_in_english + screening_age_years + screening_no_internet_access + screening_phq9_score + screening_suicidality_plan + screening_eating_disorder + screening_bipolar_disorder + screening_ocd_disorder + screening_ptsd_disorder + screening_psychosis + screening_alcohol_substance_abuse + screening_adhd_disorder + screening_neuro_disorder + screening_impediment
            },
            "Tele-Orientation":{
            "Not Fluent in English": to_not_fluent_in_english,
                "Age <18 or >65": to_age_years,
                "No Computer/Internet Access": to_no_internet_access,
                "Suciadility with activce plan": to_suicidality_plan,
                "Impediment to Vision Hearing or hand movement": to_impediment,
                "No major depressive disorder": to_no_major_depression_disorder,
                "Deceased": to_deceased,
                "Other Exclusion": to_other_exclusion,
                "Exclusion Total": to_not_fluent_in_english + to_age_years + to_no_internet_access + to_suicidality_plan + to_impediment + to_no_major_depression_disorder + to_deceased + to_other_exclusion
            }
        },
        "Refusals" : {
            "Screening": {
                "Not Interested": screening_not_interested,
                "Too busy": screening_too_busy,
                "Dislike Technology Applications" : screening_dislike_tech,
                "Concerned_about_privacy": screening_privacy_concern,
                "Other" : screening_other_concern,
                "Decline to State": screening_decline_to_state,
                "Refusal Total": screening_not_interested + screening_too_busy + screening_privacy_concern + screening_other_concern + screening_decline_to_state + screening_dislike_tech
            },
            "Teleorientation":{
                "Not Interested": to_not_interested,
                "Too busy": to_too_busy,
                "Dislike Technology Applications" : to_dislike_tech,
                "Concerned_about_privacy": to_privacy_concern,
                "Other" : to_other_concern,
                "Decline to State": to_decline_to_state,
                "Refusal Total": to_not_interested + to_too_busy + to_privacy_concern + to_other_concern + to_decline_to_state + to_dislike_tech
            },
            } 
        }

    return result_json