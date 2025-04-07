import urllib.request
import urllib.parse
import json

def fetch_redcap_staff_report():
    """
    Fetches REDCap data and counts number of records per staff per category.

    Returns:
        dict: A nested dictionary with categories as keys, and staff ID-name/count pairs.
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
        'events[0]': 'enroll_arm_1',
        'rawOrLabel': 'raw',
        'rawOrLabelHeaders': 'raw',
        'exportCheckboxLabel': 'false',
        'exportSurveyFields': 'false',
        'exportDataAccessGroups': 'false',
        'returnFormat': 'json'
    }

    # Encode and send request
    data = urllib.parse.urlencode(datacall).encode('utf-8')
    req = urllib.request.Request('https://www.redcap.ihrp.uic.edu/api/', data)
    resp = urllib.request.urlopen(req)
    response_json = json.loads(resp.read())

    # Mapping of staff IDs to names
    staff_names = {
        '1': "Amruta B",
        '2': "Leslie S",
        '3': "Claudia G",
        '4': "Shannon G",
        '5': "Nancy W",
        '6': "Corina R",
        '7': "Nan L",
        '8': "Jenny J",
        '9': "Gbenga A",
        '10': "Abby M",
        '11': "Richa S",
        '12': "Rahul V"
    }

    # Categories and corresponding REDCap fields
    categories = {
        'Teleorientation': 'to_staff',
        'In-person Visit': 'ip_staff',
        'Eligibility screener': 'es_ra',
        'In-person tech staff': 'tz_staff_2',
        'Tech zoom setup staff': 'tz_staff'
    }

    # Initialize result counters
    results = {category: {staff_id: 0 for staff_id in staff_names} for category in categories}

    # Tally staff counts per category
    for record in response_json:
        for category, field in categories.items():
            staff_id = record.get(field)
            if staff_id in results[category]:
                results[category][staff_id] += 1

    # Format results to include names with counts
    formatted_results = {}
    for category, staff_counts in results.items():
        formatted_results[category] = {
            staff_names[staff_id]: count for staff_id, count in staff_counts.items()
        }

    return formatted_results
