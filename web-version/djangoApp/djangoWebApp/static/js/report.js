$(document).ready(function() {
    // Fetch available dates
    fetchAvailableDates().then((availableDates) => {
        console.log('Fetched Dates:', availableDates);

        // Get today's date in yyyy-MM-dd format
        const today = new Date().toISOString().split('T')[0];

        // Initialize Flatpickr for startDateInput
        flatpickr("#startDateInput", {
            enable: availableDates, // Only allow these dates
            dateFormat: "Y-m-d", // Set the format to yyyy-MM-dd
            defaultDate: availableDates.includes(today) ? today : availableDates[0], // Default to today if available
        });

        // Initialize Flatpickr for endDateInput
        flatpickr("#endDateInput", {
            enable: availableDates, // Only allow these dates
            dateFormat: "Y-m-d", // Set the format to yyyy-MM-dd
            defaultDate: availableDates.includes(today) ? today : availableDates[0], // Default to today if available
        });
    });
})

async function fetchAvailableDates() {
    const apiUrl = '/api/dates/'; // Replace with the full API URL if hosted on a different domain

    try {
        const response = await fetch(apiUrl, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json(); // Parse JSON response

        return data.dates; // Return the array of dates
    } catch (error) {
        console.error('Error fetching dates:', error);
        return []; // Return an empty array on error
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Check if this cookie string begins with the name we want
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function encodeFormData(data) {
    return Object.keys(data)
        .map(key => encodeURIComponent(key) + '=' + encodeURIComponent(data[key]))
        .join('&');
}

// Function to trigger API call to server
async function fetchRecruitmentSummaries(startDate, endDate) {
    // Define the API URL
    const url = 'http://127.0.0.1:8000/api/data/recruitment/';

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
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': getCookie('csrftoken')  // Function to get the CSRF token
            },
            body: encodeFormData(payload)
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

// Function to trigger API call to server
async function fetchMdReviewSummaries(startDate, endDate) {
    // Define the API URL
    const url = 'http://127.0.0.1:8000/api/data/mdreview/';

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
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': getCookie('csrftoken')  // Function to get the CSRF token
            },
            body: encodeFormData(payload)
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
// async function populateRecruitmentTable(startDateDoc, endDateDoc) {
//     // Replace with the actual API endpoint
//     // const startDateDoc = await fetch('API_ENDPOINT_START').then(response => response.json());
//     // const endDateDoc = await fetch('API_ENDPOINT_END').then(response => response.json());

//     // Invitations sent
//     document.getElementById('cumulative-invitations-sent').innerText = endDateDoc.totals.invite_sent_count;
//     document.getElementById('cumulative-invitations-sent-percent').innerText = ((endDateDoc.totals.invite_sent_count - startDateDoc.totals.invite_sent_count) / endDateDoc.totals.invite_sent_count) * 100;
//     document.getElementById('weekly-change-invitations-sent').innerText = endDateDoc.totals.invite_sent_count - startDateDoc.totals.invite_sent_count;
//     document.getElementById('uic-invitations-sent').innerText = endDateDoc.sitesDict["1"].invite_sent_count;
//     document.getElementById('uic-change-invitations-sent').innerText = endDateDoc.sitesDict["1"].invite_sent_count - startDateDoc.sitesDict["1"].invite_sent_count;
//     document.getElementById('stl-invitations-sent').innerText = endDateDoc.sitesDict["2"].invite_sent_count;
//     document.getElementById('stl-change-invitations-sent').innerText = endDateDoc.sitesDict["2"].invite_sent_count - startDateDoc.sitesDict["2"].invite_sent_count;
//     document.getElementById('pit-invitations-sent').innerText = endDateDoc.sitesDict["3"].invite_sent_count;
//     document.getElementById('pit-change-invitations-sent').innerText = endDateDoc.sitesDict["3"].invite_sent_count - startDateDoc.sitesDict["3"].invite_sent_count;

//     // Within 2-week wait
//     document.getElementById('cumulative-2week-wait').innerText = endDateDoc.totals.two_week_wait_count;
//     document.getElementById('cumulative-2week-wait-percent').innerText = ((endDateDoc.totals.two_week_wait_count - startDateDoc.totals.two_week_wait_count) / endDateDoc.totals.two_week_wait_count) * 100;
//     document.getElementById('weekly-change-2week-wait').innerText = endDateDoc.totals.two_week_wait_count - startDateDoc.totals.two_week_wait_count;
//     document.getElementById('uic-2week-wait').innerText = endDateDoc.sitesDict["1"].two_week_wait_count;
//     document.getElementById('uic-change-2week-wait').innerText = endDateDoc.sitesDict["1"].two_week_wait_count - startDateDoc.sitesDict["1"].two_week_wait_count;
//     document.getElementById('stl-2week-wait').innerText = endDateDoc.sitesDict["2"].two_week_wait_count;
//     document.getElementById('stl-change-2week-wait').innerText = endDateDoc.sitesDict["2"].two_week_wait_count - startDateDoc.sitesDict["2"].two_week_wait_count;
//     document.getElementById('pit-2week-wait').innerText = endDateDoc.sitesDict["3"].two_week_wait_count;
//     document.getElementById('pit-change-2week-wait').innerText = endDateDoc.sitesDict["3"].two_week_wait_count - startDateDoc.sitesDict["3"].two_week_wait_count;

//     // Calling in-progress
//     document.getElementById('cumulative-calling').innerText = endDateDoc.totals.calling_in_progress_count;
//     document.getElementById('cumulative-calling-percent').innerText = ((endDateDoc.totals.calling_in_progress_count - startDateDoc.totals.calling_in_progress_count) / endDateDoc.totals.calling_in_progress_count) * 100 || 0;
//     document.getElementById('weekly-change-calling').innerText = endDateDoc.totals.calling_in_progress_count - startDateDoc.totals.calling_in_progress_count;
//     document.getElementById('uic-calling').innerText = endDateDoc.sitesDict["1"].calling_in_progress_count;
//     document.getElementById('uic-change-calling').innerText = endDateDoc.sitesDict["1"].calling_in_progress_count - startDateDoc.sitesDict["1"].calling_in_progress_count;
//     document.getElementById('stl-calling').innerText = endDateDoc.sitesDict["2"].calling_in_progress_count;
//     document.getElementById('stl-change-calling').innerText = endDateDoc.sitesDict["2"].calling_in_progress_count - startDateDoc.sitesDict["2"].calling_in_progress_count;
//     document.getElementById('pit-calling').innerText = endDateDoc.sitesDict["3"].calling_in_progress_count;
//     document.getElementById('pit-change-calling').innerText = endDateDoc.sitesDict["3"].calling_in_progress_count - startDateDoc.sitesDict["3"].calling_in_progress_count;

//     // Ceased outreach
//     document.getElementById('cumulative-ceased').innerText = endDateDoc.totals.recruit_oc_var;
//     document.getElementById('cumulative-ceased-percent').innerText = ((endDateDoc.totals.recruit_oc_var - startDateDoc.totals.recruit_oc_var) / endDateDoc.totals.recruit_oc_var) * 100 || 0;
//     document.getElementById('weekly-change-ceased').innerText = endDateDoc.totals.recruit_oc_var - startDateDoc.totals.recruit_oc_var;
//     document.getElementById('uic-ceased').innerText = endDateDoc.sitesDict["1"].recruit_oc_var;
//     document.getElementById('uic-change-ceased').innerText = endDateDoc.sitesDict["1"].recruit_oc_var - startDateDoc.sitesDict["1"].recruit_oc_var;
//     document.getElementById('stl-ceased').innerText = endDateDoc.sitesDict["2"].recruit_oc_var;
//     document.getElementById('stl-change-ceased').innerText = endDateDoc.sitesDict["2"].recruit_oc_var - startDateDoc.sitesDict["2"].recruit_oc_var;
//     document.getElementById('pit-ceased').innerText = endDateDoc.sitesDict["3"].recruit_oc_var;
//     document.getElementById('pit-change-ceased').innerText = endDateDoc.sitesDict["3"].recruit_oc_var - startDateDoc.sitesDict["3"].recruit_oc_var;

//     // Requested call (via Website or Twilio)
//     document.getElementById('cumulative-requested-call').innerText = endDateDoc.totals.requested_call_count;
//     document.getElementById('cumulative-requested-call-percent').innerText = ((endDateDoc.totals.requested_call_count - startDateDoc.totals.requested_call_count) / endDateDoc.totals.requested_call_count) * 100 || 0;
//     document.getElementById('weekly-change-requested-call').innerText = endDateDoc.totals.requested_call_count - startDateDoc.totals.requested_call_count;
//     document.getElementById('uic-requested-call').innerText = endDateDoc.sitesDict["1"].requested_call_count;
//     document.getElementById('uic-change-requested-call').innerText = endDateDoc.sitesDict["1"].requested_call_count - startDateDoc.sitesDict["1"].requested_call_count;
//     document.getElementById('stl-requested-call').innerText = endDateDoc.sitesDict["2"].requested_call_count;
//     document.getElementById('stl-change-requested-call').innerText = endDateDoc.sitesDict["2"].requested_call_count - startDateDoc.sitesDict["2"].requested_call_count;
//     document.getElementById('pit-requested-call').innerText = endDateDoc.sitesDict["3"].requested_call_count;
//     document.getElementById('pit-change-requested-call').innerText = endDateDoc.sitesDict["3"].requested_call_count - startDateDoc.sitesDict["3"].requested_call_count;

//     // Partial Screen
//     document.getElementById('cumulative-partial-screen').innerText = endDateDoc.totals.partial_screen_count;
//     document.getElementById('cumulative-partial-screen-percent').innerText = ((endDateDoc.totals.partial_screen_count - startDateDoc.totals.partial_screen_count) / endDateDoc.totals.partial_screen_count) * 100;
//     document.getElementById('weekly-change-partial-screen').innerText = endDateDoc.totals.partial_screen_count - startDateDoc.totals.partial_screen_count;
//     document.getElementById('uic-partial-screen').innerText = endDateDoc.sitesDict["1"].partial_screen_count;
//     document.getElementById('uic-change-partial-screen').innerText = endDateDoc.sitesDict["1"].partial_screen_count - startDateDoc.sitesDict["1"].partial_screen_count;
//     document.getElementById('stl-partial-screen').innerText = endDateDoc.sitesDict["2"].partial_screen_count;
//     document.getElementById('stl-change-partial-screen').innerText = endDateDoc.sitesDict["2"].partial_screen_count - startDateDoc.sitesDict["2"].partial_screen_count;
//     document.getElementById('pit-partial-screen').innerText = endDateDoc.sitesDict["3"].partial_screen_count;
//     document.getElementById('pit-change-partial-screen').innerText = endDateDoc.sitesDict["3"].partial_screen_count - startDateDoc.sitesDict["3"].partial_screen_count;

//     // Not Screened
//     document.getElementById('cumulative-not-screened').innerText = endDateDoc.totals.not_screened_count;
//     document.getElementById('cumulative-not-screened-percent').innerText = ((endDateDoc.totals.not_screened_count - startDateDoc.totals.not_screened_count) / endDateDoc.totals.not_screened_count) * 100 || 0;
//     document.getElementById('weekly-change-not-screened').innerText = endDateDoc.totals.not_screened_count - startDateDoc.totals.not_screened_count;
//     document.getElementById('uic-not-screened').innerText = endDateDoc.sitesDict["1"].not_screened_count;
//     document.getElementById('uic-change-not-screened').innerText = endDateDoc.sitesDict["1"].not_screened_count - startDateDoc.sitesDict["1"].not_screened_count;
//     document.getElementById('stl-not-screened').innerText = endDateDoc.sitesDict["2"].not_screened_count;
//     document.getElementById('stl-change-not-screened').innerText = endDateDoc.sitesDict["2"].not_screened_count - startDateDoc.sitesDict["2"].not_screened_count;
//     document.getElementById('pit-not-screened').innerText = endDateDoc.sitesDict["3"].not_screened_count;
//     document.getElementById('pit-change-not-screened').innerText = endDateDoc.sitesDict["3"].not_screened_count - startDateDoc.sitesDict["3"].not_screened_count;
// }

async function populateRecruitmentTable(startDateDoc, endDateDoc) {
    console.log("new func 2")
    const calculatePercent = (current, previous) => current ? (((current - previous) / current) * 100).toFixed(2) : 0;

    // Array to store any errors or missing fields
    const errors = [];

    const metrics = [
        // Recruitment Invitations
        { id: 'invitations-sent', key: 'invite_sent_count' },
        { id: '2week-wait', key: 'two_week_wait_count' },
        { id: 'calling', key: 'calling_in_progress_count' },
        { id: 'ceased', key: 'ceased_outreach_count' },
        { id: 'requested-call', key: 'requested_call_count' },
        { id: 'partial-screen', key: 'partial_screen_count' },
        { id: 'not-screened', key: 'not_screened_count' },
        { id: 'ineligible', key: 'ineligible_prior_to_screen_count' },
        { id: 'declined', key: 'declined_to_screen_count' },
        { id: 'screened', key: 'screened_count' },
        { id: 'ineligible-after-screened', key: 'ineligible_count' },

        // Eligibility
        { id: 'eligible-declined-to', key: 'eligible_but_declined_to_count' },
        { id: 'eligible-undecided', key: 'eligible_undecided_count' },
        { id: 'eligible-maybe', key: 'maybe_eligible_count' },
        { id: 'eligible-ies', key: 'ies_eligible_count' },

        // Tele-Orientation Appointment
        { id: 'to-appoint', key: 'to_schedule_count' },
        { id: 'to-attended', key: 'to_attend_count' },
        { id: 'declined-icf', key: 'declined_icf_count' },
        { id: 'eligible-pending-md-clear', key: 'eligible_pending_clearance_count' },
        { id: 'eligible-at-to', key: 'eligible_at_to_count' },
        { id: 'appoint-declined', key: 'appt_declined_count' },
        { id: 'appoint-within-1-wk', key: 'appt_needed_within_week_since_ies_count' },
        { id: 'appoint-over-1-wk', key: 'appt_needed_over_week_since_ies_count' },
        { id: 're-no-show', key: 'reschedule_no_show_count' },
        { id: 'to-scheduled', key: 'to_schedule_count' },
        { id: 'inelig-to', key: 'ineligible_at_to_count' },
        { id: 'eligible-undecided-to', key: 'eligible_undecided_count' },
        // { id: '', key: '' },
        // { id: '', key: '' },
        
        // Device Distribution
        { id: 'device-dist', key: 'dist_complete' },
        { id: 'need-baseline', key: 'needs_baseline_survey_count' },
        { id: 'declined-proceed', key: 'declined_to_proceed_count_2' },
        { id: 'dist-plan-tbd', key: 'dist_plan_tbd_count' },
        { id: 'dist-plan-in-place', key: 'dist_plan_in_place_count' },
        { id: 'distrib-delay-pickup', key: 'dist_delay_problem' },
        { id: 'distrib-delay-ship', key: 'dist_delay_shipping' },
        { id: 'dec-to-proceed-dev-dist', key: 'declined_to_proceed_count_2' },
        { id: 'distrib-complete', key: 'dist_complete' },
        { id: 'dec-proceed-devices-home', key: 'declined_to_proceed_with_device_count' },
        
        // Home-Tech Setup Appointment
        { id: 'home-setup', key: 'home_tech_needed_count' },
        { id: 'decline-devices', key: 'declined_to_proceed_with_device_count' },
        { id: 'appoint-need-within-1-wk-delivery', key: 'appt_needed_within_week_since_ies_count' },
        { id: 'appoint-need-over-1-wk-delivery', key: 'appt_needed_over_week_since_ies_count' },
        { id: 'resch-no-show-device', key: 'reschedule_no_show_count' },
        { id: 'tech-setup-sch', key: 'tech_schedule_setup_count' },

        // Home-Tech Attended
        { id: 'home-tech-attend', key: 'tech_issue_with_device_count' },
        { id: 'decline-proceed-devices-home', key: 'declined_to_proceed_with_device_count' },
        { id: 'ineligible-home-tech', key: 'ineligible_to_proceed_with_device_count' },
        { id: 'tech-pending-resolution', key: 'tech_issue_with_device_count' },

        // Self-Measurements
        { id: 'self-measures-ready', key: 'self_measure_ready_count' },
        { id: 'baseline-self-measure-progress', key: 'self_measure_ready_count' },
        { id: 'pending-day-8-check', key: 'pending_day_8_count' },
        { id: 'pending-day-15-check', key: 'pending_day_15_check' },
        { id: 'inelig-bmi', key: 'ineligible_bmi_count' },
        { id: 'inelig-insuff-day-15', key: 'insufficient_data_count' },

        // Randomization
        { id: 'elig-pending-random', key: 'elig_pending_randamization_count' },
        { id: 'r1-random', key: 'randamization_count' }
    ];

    metrics.forEach(metric => {
        try {
            const cumulative = parseFloat(endDateDoc.totals[metric.key]) || 0;
            const previous = parseFloat(startDateDoc.totals[metric.key]) || 0;
            const uicCurrent = parseFloat(endDateDoc.sitesDict["1"][metric.key]) || 0;
            const uicPrevious = parseFloat(startDateDoc.sitesDict["1"][metric.key]) || 0;
            const stlCurrent = parseFloat(endDateDoc.sitesDict["2"][metric.key]) || 0;
            const stlPrevious = parseFloat(startDateDoc.sitesDict["2"][metric.key]) || 0;
            const pitCurrent = parseFloat(endDateDoc.sitesDict["3"][metric.key]) || 0;
            const pitPrevious = parseFloat(startDateDoc.sitesDict["3"][metric.key]) || 0;

            // Fill cumulative, percent, and weekly change
            document.getElementById(`cumulative-${metric.id}`).innerText = cumulative;
            document.getElementById(`cumulative-${metric.id}-percent`).innerText = calculatePercent(cumulative, previous) + '%';
            document.getElementById(`weekly-change-${metric.id}`).innerText = cumulative - previous;

            // Fill site-specific data
            document.getElementById(`uic-${metric.id}`).innerText = uicCurrent;
            document.getElementById(`uic-change-${metric.id}`).innerText = uicCurrent - uicPrevious;
            document.getElementById(`stl-${metric.id}`).innerText = stlCurrent;
            document.getElementById(`stl-change-${metric.id}`).innerText = stlCurrent - stlPrevious;
            document.getElementById(`pit-${metric.id}`).innerText = pitCurrent;
            document.getElementById(`pit-change-${metric.id}`).innerText = pitCurrent - pitPrevious;
        } catch (error) {
            // Log missing fields or errors
            errors.push(`Error processing metric: ${metric.key}. ${error.message}`);
        }
    });

    // Log any errors
    if (errors.length > 0) {
        console.error("The following errors occurred while populating the table:");
        errors.forEach(err => console.error(err));
    }
}


// const tableRows = [
//     { id: "invitations-sent", label: "Invitations sent", metric: "invite_sent_count" },
//     { id: "within-2week-wait", label: "Within 2-week wait", metric: "two_week_wait_count" },
//     { id: "calling-in-progress", label: "Calling in-progress", metric: "calling_in_progress_count" },
//     { id: "ceased-outreach", label: "Ceased outreach", metric: "ceased_outreach_count" },
//     { id: "requested-call", label: "Requested call (via Website or Twilio)", metric: "requested_call_count" },
//     { id: "partial-screen", label: "Partial Screen", metric: "partial_screen_count" },
//     { id: "not-screened", label: "Not Screened", metric: "not_screened_count" },
//     { id: "ineligible-prior", label: "Ineligible prior to screen", metric: "ineligible_prior_to_screen_count" },
//     { id: "declined-screen", label: "Declined to screen", metric: "declined_to_screen_count" },
//     { id: "screened", label: "Screened", metric: "screened_count" },
//     { id: "ineligible", label: "Ineligible", metric: "ineligible_count" },
//     { id: "eligible-declined", label: "Eligible - Declined TO", metric: "eligible_but_declined_to_count" },
//     { id: "eligible-undecided", label: "Eligible - Undecided", metric: "eligible_undecided_count" },
//     { id: "maybe-eligible", label: "Maybe Eligible", metric: "maybe_eligible_count" },
//     { id: "ies-eligible", label: "IES Eligible", metric: "ies_eligible_count" },
//     { id: "appointment-declined", label: "Appointment declined/ceased", metric: "appointment_declined_count" },
//     { id: "appointment-needed-wk", label: "Appointment needed within wk since IES", metric: "appt_needed_within_week_since_ies_count" },
//     { id: "appointment-needed-over-wk", label: "Appointment needed over 1 wk since IES", metric: "appt_needed_over_week_since_ies_count" },
//     { id: "reschedule-no-show", label: "Reschedule No-show", metric: "reschedule_no_show_count" },
//     { id: "to-scheduled", label: "TO Scheduled", metric: "to_schedule_count" },
//     { id: "to-attended", label: "TO Attended", metric: "to_attend_count" },
//     { id: "eligible-pending-clearance", label: "Eligible - Pending MD Clearance", metric: "eligible_pending_clearance_count" },
//     { id: "device-distribution", label: "Device Distribution", metric: "device_distribution_count" },
//     { id: "baseline-ready", label: "Self-measures Ready", metric: "self_measure_ready_count" },
//     { id: "randomized", label: "R1 - Randomized", metric: "randamization_count" }
// ];

// async function populateRecruitmentTable(startDateDoc, endDateDoc) {
//     const tbody = document.getElementById("recruitment-body");
//     tbody.innerHTML = ""; // Clear existing rows

//     tableRows.forEach(row => {
//         const cumulative = endDateDoc.totals[row.metric] || 0;
//         const startValue = startDateDoc.totals[row.metric] || 0;
//         const weeklyChange = cumulative - startValue;
//         const percentage = cumulative ? ((weeklyChange / cumulative) * 100).toFixed(2) : 0;

//         const uic = endDateDoc.sitesDict["1"][row.metric] || 0;
//         const uicChange = uic - (startDateDoc.sitesDict["1"][row.metric] || 0);

//         const stl = endDateDoc.sitesDict["2"][row.metric] || 0;
//         const stlChange = stl - (startDateDoc.sitesDict["2"][row.metric] || 0);

//         const pit = endDateDoc.sitesDict["3"][row.metric] || 0;
//         const pitChange = pit - (startDateDoc.sitesDict["3"][row.metric] || 0);

//         // Append a new row
//         const newRow = `
//             <tr>
//                 <td>${row.label}</td>
//                 <td>${cumulative}</td>
//                 <td>${percentage}%</td>
//                 <td>${weeklyChange}</td>
//                 <td>${uic}</td>
//                 <td>${uicChange}</td>
//                 <td>${stl}</td>
//                 <td>${stlChange}</td>
//                 <td>${pit}</td>
//                 <td>${pitChange}</td>
//             </tr>
//         `;
//         tbody.innerHTML += newRow;
//     });
// }

async function populateMdReviewTable(startDateDoc, endDateDoc) {
    // Replace with the actual API endpoint
    // const startDateDoc = await fetch('API_ENDPOINT_START').then(response => response.json());
    // const endDateDoc = await fetch('API_ENDPOINT_END').then(response => response.json());

    // TO Attended
    document.getElementById('to-attended').innerText = endDateDoc.totals.to_attended;
    document.getElementById('to-attended-percent').innerText = ((endDateDoc.totals.to_attended - startDateDoc.totals.to_attended) / endDateDoc.totals.to_attended) * 100;
    document.getElementById('uic-to-attended').innerText = endDateDoc.sitesDict["1"].to_attended;
    document.getElementById('stl-to-attended').innerText = endDateDoc.sitesDict["2"].to_attended;
    document.getElementById('pit-to-attended').innerText = endDateDoc.sitesDict["3"].to_attended;

    // MD Clearance Total
    document.getElementById('md-clearance-total').innerText = endDateDoc.totals.md_clearance_required_total;
    document.getElementById('md-clearance-total-percent').innerText = ((endDateDoc.totals.md_clearance_required_total - startDateDoc.totals.md_clearance_required_total) / endDateDoc.totals.md_clearance_required_total) * 100;
    document.getElementById('uic-md-clearance-total').innerText = endDateDoc.sitesDict["1"].md_clearance_required_total;
    document.getElementById('stl-md-clearance-total').innerText = endDateDoc.sitesDict["2"].md_clearance_required_total;
    document.getElementById('pit-md-clearance-total').innerText = endDateDoc.sitesDict["3"].md_clearance_required_total;

    // MD Clearance required < 10.3.23 standard PARQ
    document.getElementById('standard-parq').innerText = endDateDoc.totals.md_clearance_required_standard_parq;
    document.getElementById('standard-parq-percent').innerText = ((endDateDoc.totals.md_clearance_required_standard_parq - startDateDoc.totals.md_clearance_required_standard_parq) / endDateDoc.totals.md_clearance_required_standard_parq) * 100 || 0;
    document.getElementById('uic-standard-parq').innerText = endDateDoc.sitesDict["1"].md_clearance_required_standard_parq;
    document.getElementById('stl-standard-parq').innerText = endDateDoc.sitesDict["2"].md_clearance_required_standard_parq;
    document.getElementById('pit-standard-parq').innerText = endDateDoc.sitesDict["3"].md_clearance_required_standard_parq;

    // MD Clearance required > 10.3.23 modified PARQ
    document.getElementById('modified-parq').innerText = endDateDoc.totals.md_clearance_required_modified_parq;
    document.getElementById('modified-parq-percent').innerText = ((endDateDoc.totals.md_clearance_required_modified_parq - startDateDoc.totals.md_clearance_required_modified_parq) / endDateDoc.totals.md_clearance_required_modified_parq) * 100 || 0;
    document.getElementById('uic-modified-parq').innerText = endDateDoc.sitesDict["1"].md_clearance_required_modified_parq;
    document.getElementById('stl-modified-parq').innerText = endDateDoc.sitesDict["2"].md_clearance_required_modified_parq;
    document.getElementById('pit-modified-parq').innerText = endDateDoc.sitesDict["3"].md_clearance_required_modified_parq;

    // PAR review pending
    document.getElementById('par-review-pending').innerText = endDateDoc.totals.par_review_pending;
    document.getElementById('par-review-pending-percent').innerText = ((endDateDoc.totals.par_review_pending - startDateDoc.totals.par_review_pending) / endDateDoc.totals.par_review_pending) * 100 || 0;
    document.getElementById('uic-par-review-pending').innerText = endDateDoc.sitesDict["1"].par_review_pending;
    document.getElementById('stl-par-review-pending').innerText = endDateDoc.sitesDict["2"].par_review_pending;
    document.getElementById('pit-par-review-pending').innerText = endDateDoc.sitesDict["3"].par_review_pending;

    // PAR reviewed - Ineligible
    document.getElementById('par-reviewed-ineligible').innerText = endDateDoc.totals.par_reviewed_ineligible;
    document.getElementById('par-reviewed-ineligible-percent').innerText = ((endDateDoc.totals.par_reviewed_ineligible - startDateDoc.totals.par_reviewed_ineligible) / endDateDoc.totals.par_reviewed_ineligible) * 100;
    document.getElementById('uic-par-reviewed-ineligible').innerText = endDateDoc.sitesDict["1"].par_reviewed_ineligible;
    document.getElementById('stl-par-reviewed-ineligible').innerText = endDateDoc.sitesDict["2"].par_reviewed_ineligible;
    document.getElementById('pit-par-reviewed-ineligible').innerText = endDateDoc.sitesDict["3"].par_reviewed_ineligible;

    // PAR reviewed - Eligible
    document.getElementById('par-reviewed-eligible').innerText = endDateDoc.totals.par_reviewed_eligible;
    document.getElementById('par-reviewed-eligible-percent').innerText = ((endDateDoc.totals.par_reviewed_eligible - startDateDoc.totals.par_reviewed_eligible) / endDateDoc.totals.par_reviewed_eligible) * 100 || 0;
    document.getElementById('uic-par-reviewed-eligible').innerText = endDateDoc.sitesDict["1"].par_reviewed_eligible;
    document.getElementById('stl-par-reviewed-eligible').innerText = endDateDoc.sitesDict["2"].par_reviewed_eligible;
    document.getElementById('pit-par-reviewed-eligible').innerText = endDateDoc.sitesDict["3"].par_reviewed_eligible;

    endDateDocTotal = (endDateDoc.totals.par_review_pending + endDateDoc.totals.par_reviewed_ineligible + endDateDoc.totals.par_reviewed_eligible)
    startDateDocTotal = (startDateDoc.totals.par_review_pending + startDateDoc.totals.par_reviewed_ineligible + startDateDoc.totals.par_reviewed_eligible)
    // MD Clearance required
    document.getElementById('md-clearance-required').innerText = endDateDocTotal;
    document.getElementById('md-clearance-required-percent').innerText = ((endDateDocTotal - startDateDocTotal) / endDateDocTotal) * 100 || 0;
    document.getElementById('uic-md-clearance-required').innerText = endDateDoc.sitesDict["1"].par_review_pending + endDateDoc.sitesDict["1"].par_reviewed_ineligible + endDateDoc.sitesDict["1"].par_reviewed_ineligible;
    document.getElementById('stl-md-clearance-required').innerText = endDateDoc.sitesDict["2"].par_review_pending + endDateDoc.sitesDict["2"].par_reviewed_ineligible + endDateDoc.sitesDict["2"].par_reviewed_ineligible;
    document.getElementById('pit-md-clearance-required').innerText = endDateDoc.sitesDict["3"].par_review_pending + endDateDoc.sitesDict["3"].par_reviewed_ineligible + endDateDoc.sitesDict["3"].par_reviewed_ineligible;
}

// Call the function to populate the table
// populateTable();

// Example usage of the function
// Pass in the startDate and endDate in the 'YYYY-MM-DD' format
function getSummariesAndDisplay() {
    // const startDate = document.getElementById('startDateSelect').value;
    // const endDate = document.getElementById('endDateSelect').value;
    const startDateInput = document.getElementById('startDateInput');
    const endDateInput = document.getElementById('endDateInput');

    const startDate = startDateInput.value; // yyyy-mm-dd format
    const endDate = endDateInput.value; // yyyy-mm-dd format

    console.log('vars', startDate, endDate);
    
    fetchRecruitmentSummaries(startDate, endDate).then(data => {
        console.log(data.startDateDoc, data.endDateDoc)
        populateRecruitmentTable(data.startDateDoc, data.endDateDoc);
    });

    fetchMdReviewSummaries(startDate, endDate).then(data => {
        console.log('md', data.startDateDoc, data.endDateDoc)
        populateMdReviewTable(data.startDateDoc, data.endDateDoc);
    })
}



function exportToExcel() {
    var wb = XLSX.utils.table_to_book(document.getElementById('recruitment-table'), {sheet: "PivotReport"});
    
    // Append the second table ('md-review-summaries') as Sheet2
    var ws2 = XLSX.utils.table_to_sheet(document.getElementById('md-review-table'));
    XLSX.utils.book_append_sheet(wb, ws2, "MDReview");

    XLSX.writeFile(wb, 'pivot.xlsx');
}

function switchTabToPivotReport() {
    document.getElementById('recruitment-table').style.display = 'block';
    document.getElementById('md-review-table').style.display = 'none';
    
    // Set the active tab
    document.getElementById('pivot-tab').classList.add('active');
    document.getElementById('md-review-tab').classList.remove('active');
}

function switchTabToMdReview() {
    document.getElementById('recruitment-table').style.display = 'none';
    document.getElementById('md-review-table').style.display = 'block';
    
    // Set the active tab
    document.getElementById('pivot-tab').classList.remove('active');
    document.getElementById('md-review-tab').classList.add('active');
}

switchTabToPivotReport()


// document.getElementById("md-review-table").display = "block";
