// Function to trigger API call to Flask server
async function fetchSummaries(startDate, endDate) {
    // Define the API URL
    const url = 'http://127.0.0.1:5000/fetch-summary';

    // Create the payload with startDate and endDate
    const payload = {
        startDate: startDate,
        endDate: endDate
    };

    try {
        // Make the POST request using fetch
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload)
        });

        // Check if the response is successful
        if (!response.ok) {
            const errorData = await response.json();
            console.error('Error:', errorData);
            return;
        }

        // Parse the JSON response
        const data = await response.json();
        console.log('Success:', data);
        // populateTable(data);
        return data;
    } catch (error) {
        // Handle any network or server errors
        console.error('Error fetching summaries:', error);
    }
}

// Example function to fetch data and populate the table
async function populateTable(startDateDoc, endDateDoc) {
    // Replace with the actual API endpoint
    // const startDateDoc = await fetch('API_ENDPOINT_START').then(response => response.json());
    // const endDateDoc = await fetch('API_ENDPOINT_END').then(response => response.json());

    // Invitations sent
    document.getElementById('cumulative-invitations-sent').innerText = endDateDoc.totals.invite_sent_count;
    document.getElementById('cumulative-invitations-sent-percent').innerText = ((endDateDoc.totals.invite_sent_count - startDateDoc.totals.invite_sent_count) / endDateDoc.totals.invite_sent_count) * 100;
    document.getElementById('weekly-change-invitations-sent').innerText = endDateDoc.totals.invite_sent_count - startDateDoc.totals.invite_sent_count;
    document.getElementById('uic-invitations-sent').innerText = endDateDoc.sitesDict["1"].invite_sent_count;
    document.getElementById('uic-change-invitations-sent').innerText = endDateDoc.sitesDict["1"].invite_sent_count - startDateDoc.sitesDict["1"].invite_sent_count;
    document.getElementById('stl-invitations-sent').innerText = endDateDoc.sitesDict["2"].invite_sent_count;
    document.getElementById('stl-change-invitations-sent').innerText = endDateDoc.sitesDict["2"].invite_sent_count - startDateDoc.sitesDict["2"].invite_sent_count;
    document.getElementById('pit-invitations-sent').innerText = endDateDoc.sitesDict["3"].invite_sent_count;
    document.getElementById('pit-change-invitations-sent').innerText = endDateDoc.sitesDict["3"].invite_sent_count - startDateDoc.sitesDict["3"].invite_sent_count;

    // Within 2-week wait
    document.getElementById('cumulative-2week-wait').innerText = endDateDoc.totals.two_week_wait_count;
    document.getElementById('cumulative-2week-wait-percent').innerText = ((endDateDoc.totals.two_week_wait_count - startDateDoc.totals.two_week_wait_count) / endDateDoc.totals.two_week_wait_count) * 100;
    document.getElementById('weekly-change-2week-wait').innerText = endDateDoc.totals.two_week_wait_count - startDateDoc.totals.two_week_wait_count;
    document.getElementById('uic-2week-wait').innerText = endDateDoc.sitesDict["1"].two_week_wait_count;
    document.getElementById('uic-change-2week-wait').innerText = endDateDoc.sitesDict["1"].two_week_wait_count - startDateDoc.sitesDict["1"].two_week_wait_count;
    document.getElementById('stl-2week-wait').innerText = endDateDoc.sitesDict["2"].two_week_wait_count;
    document.getElementById('stl-change-2week-wait').innerText = endDateDoc.sitesDict["2"].two_week_wait_count - startDateDoc.sitesDict["2"].two_week_wait_count;
    document.getElementById('pit-2week-wait').innerText = endDateDoc.sitesDict["3"].two_week_wait_count;
    document.getElementById('pit-change-2week-wait').innerText = endDateDoc.sitesDict["3"].two_week_wait_count - startDateDoc.sitesDict["3"].two_week_wait_count;

    // Calling in-progress
    document.getElementById('cumulative-calling').innerText = endDateDoc.totals.calling_in_progress_count;
    document.getElementById('cumulative-calling-percent').innerText = ((endDateDoc.totals.calling_in_progress_count - startDateDoc.totals.calling_in_progress_count) / endDateDoc.totals.calling_in_progress_count) * 100 || 0;
    document.getElementById('weekly-change-calling').innerText = endDateDoc.totals.calling_in_progress_count - startDateDoc.totals.calling_in_progress_count;
    document.getElementById('uic-calling').innerText = endDateDoc.sitesDict["1"].calling_in_progress_count;
    document.getElementById('uic-change-calling').innerText = endDateDoc.sitesDict["1"].calling_in_progress_count - startDateDoc.sitesDict["1"].calling_in_progress_count;
    document.getElementById('stl-calling').innerText = endDateDoc.sitesDict["2"].calling_in_progress_count;
    document.getElementById('stl-change-calling').innerText = endDateDoc.sitesDict["2"].calling_in_progress_count - startDateDoc.sitesDict["2"].calling_in_progress_count;
    document.getElementById('pit-calling').innerText = endDateDoc.sitesDict["3"].calling_in_progress_count;
    document.getElementById('pit-change-calling').innerText = endDateDoc.sitesDict["3"].calling_in_progress_count - startDateDoc.sitesDict["3"].calling_in_progress_count;

    // Ceased outreach
    document.getElementById('cumulative-ceased').innerText = endDateDoc.totals.recruit_oc_var;
    document.getElementById('cumulative-ceased-percent').innerText = ((endDateDoc.totals.recruit_oc_var - startDateDoc.totals.recruit_oc_var) / endDateDoc.totals.recruit_oc_var) * 100 || 0;
    document.getElementById('weekly-change-ceased').innerText = endDateDoc.totals.recruit_oc_var - startDateDoc.totals.recruit_oc_var;
    document.getElementById('uic-ceased').innerText = endDateDoc.sitesDict["1"].recruit_oc_var;
    document.getElementById('uic-change-ceased').innerText = endDateDoc.sitesDict["1"].recruit_oc_var - startDateDoc.sitesDict["1"].recruit_oc_var;
    document.getElementById('stl-ceased').innerText = endDateDoc.sitesDict["2"].recruit_oc_var;
    document.getElementById('stl-change-ceased').innerText = endDateDoc.sitesDict["2"].recruit_oc_var - startDateDoc.sitesDict["2"].recruit_oc_var;
    document.getElementById('pit-ceased').innerText = endDateDoc.sitesDict["3"].recruit_oc_var;
    document.getElementById('pit-change-ceased').innerText = endDateDoc.sitesDict["3"].recruit_oc_var - startDateDoc.sitesDict["3"].recruit_oc_var;

    // Requested call (via Website or Twilio)
    document.getElementById('cumulative-requested-call').innerText = endDateDoc.totals.requested_call_count;
    document.getElementById('cumulative-requested-call-percent').innerText = ((endDateDoc.totals.requested_call_count - startDateDoc.totals.requested_call_count) / endDateDoc.totals.requested_call_count) * 100 || 0;
    document.getElementById('weekly-change-requested-call').innerText = endDateDoc.totals.requested_call_count - startDateDoc.totals.requested_call_count;
    document.getElementById('uic-requested-call').innerText = endDateDoc.sitesDict["1"].requested_call_count;
    document.getElementById('uic-change-requested-call').innerText = endDateDoc.sitesDict["1"].requested_call_count - startDateDoc.sitesDict["1"].requested_call_count;
    document.getElementById('stl-requested-call').innerText = endDateDoc.sitesDict["2"].requested_call_count;
    document.getElementById('stl-change-requested-call').innerText = endDateDoc.sitesDict["2"].requested_call_count - startDateDoc.sitesDict["2"].requested_call_count;
    document.getElementById('pit-requested-call').innerText = endDateDoc.sitesDict["3"].requested_call_count;
    document.getElementById('pit-change-requested-call').innerText = endDateDoc.sitesDict["3"].requested_call_count - startDateDoc.sitesDict["3"].requested_call_count;

    // Partial Screen
    document.getElementById('cumulative-partial-screen').innerText = endDateDoc.totals.partial_screen_count;
    document.getElementById('cumulative-partial-screen-percent').innerText = ((endDateDoc.totals.partial_screen_count - startDateDoc.totals.partial_screen_count) / endDateDoc.totals.partial_screen_count) * 100;
    document.getElementById('weekly-change-partial-screen').innerText = endDateDoc.totals.partial_screen_count - startDateDoc.totals.partial_screen_count;
    document.getElementById('uic-partial-screen').innerText = endDateDoc.sitesDict["1"].partial_screen_count;
    document.getElementById('uic-change-partial-screen').innerText = endDateDoc.sitesDict["1"].partial_screen_count - startDateDoc.sitesDict["1"].partial_screen_count;
    document.getElementById('stl-partial-screen').innerText = endDateDoc.sitesDict["2"].partial_screen_count;
    document.getElementById('stl-change-partial-screen').innerText = endDateDoc.sitesDict["2"].partial_screen_count - startDateDoc.sitesDict["2"].partial_screen_count;
    document.getElementById('pit-partial-screen').innerText = endDateDoc.sitesDict["3"].partial_screen_count;
    document.getElementById('pit-change-partial-screen').innerText = endDateDoc.sitesDict["3"].partial_screen_count - startDateDoc.sitesDict["3"].partial_screen_count;

    // Not Screened
    document.getElementById('cumulative-not-screened').innerText = endDateDoc.totals.not_screened_count;
    document.getElementById('cumulative-not-screened-percent').innerText = ((endDateDoc.totals.not_screened_count - startDateDoc.totals.not_screened_count) / endDateDoc.totals.not_screened_count) * 100 || 0;
    document.getElementById('weekly-change-not-screened').innerText = endDateDoc.totals.not_screened_count - startDateDoc.totals.not_screened_count;
    document.getElementById('uic-not-screened').innerText = endDateDoc.sitesDict["1"].not_screened_count;
    document.getElementById('uic-change-not-screened').innerText = endDateDoc.sitesDict["1"].not_screened_count - startDateDoc.sitesDict["1"].not_screened_count;
    document.getElementById('stl-not-screened').innerText = endDateDoc.sitesDict["2"].not_screened_count;
    document.getElementById('stl-change-not-screened').innerText = endDateDoc.sitesDict["2"].not_screened_count - startDateDoc.sitesDict["2"].not_screened_count;
    document.getElementById('pit-not-screened').innerText = endDateDoc.sitesDict["3"].not_screened_count;
    document.getElementById('pit-change-not-screened').innerText = endDateDoc.sitesDict["3"].not_screened_count - startDateDoc.sitesDict["3"].not_screened_count;
}

// Call the function to populate the table
// populateTable();

// Example usage of the function
// Pass in the startDate and endDate in the 'YYYY-MM-DD' format
function getSummariesAndDisplay() {
    const startDate = document.getElementById('startDateSelect').value;
    const endDate = document.getElementById('endDateSelect').value;

    console.log('vars', startDate, endDate);
    
    fetchSummaries(startDate, endDate).then(data => {
        console.log(data.startDateDoc, data.endDateDoc)
        populateTable(data.startDateDoc, data.endDateDoc);
    });
}

function exportToExcel() {
    var wb = XLSX.utils.table_to_book(document.getElementById('recruitment-table'), {sheet: "Sheet1"});
    XLSX.writeFile(wb, 'table.xlsx');
}
