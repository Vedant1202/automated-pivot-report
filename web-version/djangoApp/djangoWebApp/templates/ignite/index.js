// Fetch available dates from the Flask API
async function fetchAvailableDates() {
    // try {
    //     const response = await fetch('http://127.0.0.1:5000/data');
    //     const data = await response.json();

    //     const startDateSelect = document.getElementById('startDateSelect');
    //     const endDateSelect = document.getElementById('endDateSelect');

    //     data.forEach(entry => {
    //         const dateStr = new Date(entry.timestamp).toISOString().split('T')[0];
    //         const option = new Option(dateStr, dateStr);
    //         startDateSelect.add(option.cloneNode(true));
    //         endDateSelect.add(option.cloneNode(true));
    //     });
    // } catch (error) {
    //     console.error("Error fetching available dates:", error);
    // }
}

// Convert YYYY-MM-DD to YYYYMMDD format
function formatYYYYMMDD(dateString) {
    return dateString.replace(/-/g, ''); // Remove hyphens
}

// Fetch recruitment summaries for selected dates (using Unix timestamps)
async function fetchSummaries(startDateUnix, endDateUnix) {
    // Get formatted dates
    const startFormatted = formatYYYYMMDD(startDateUnix);
    const endFormatted = formatYYYYMMDD(endDateUnix);

    // Send request with formatted dates
    const url = `http://localhost:8000/ignite/data/?start=${startFormatted}&end=${endFormatted}`;

    try {
        const response = await fetch(url);
        const data = await response.json();

        if (!data || !data.startDateDoc || !data.endDateDoc) {
            alert("Data for the selected dates is not available.");
            return null;
        }

        return { startDateDoc: data.startDateDoc, endDateDoc: data.endDateDoc };
    } catch (error) {
        console.error("Error fetching summaries:", error);
    }
}


// Populate the table with fetched data
async function populateTable(startDateDoc, endDateDoc) {
    function calcChange(newVal, oldVal) {
        if (!oldVal || oldVal === 0) {
            return "0%"; // Avoid division by zero, return 0% instead of N/A
        }
        return ((newVal - oldVal) / oldVal * 100).toFixed(1) + "%";
    }
    

    function updateField(id, endValue, changeValue) {
        document.getElementById(id).innerText = endValue;
        document.getElementById(id + "-percent").innerText = calcChange(endValue, changeValue);
        document.getElementById(id + "-change").innerText = endValue - changeValue;
    }

    // Updating fields based on the provided data
    updateField("invites-sent", endDateDoc.invite_sent_count, startDateDoc.invite_sent_count);
    updateField("week-wait", endDateDoc.two_week_wait_count, startDateDoc.two_week_wait_count);
    updateField("calling-progress", endDateDoc.calling_in_progress_count, startDateDoc.calling_in_progress_count);
    updateField("ceased-outreach", endDateDoc.ceased_outreach_count, startDateDoc.ceased_outreach_count);
    updateField("requested-call", endDateDoc.requested_call_count, startDateDoc.requested_call_count);
    updateField("partial-screen", endDateDoc.partial_screen_count, startDateDoc.partial_screen_count);
    updateField("not-screened", endDateDoc.ineligible_prior_to_screen_count + endDateDoc.declined_to_screen_count, startDateDoc.ineligible_prior_to_screen_count + startDateDoc.declined_to_screen_count);
    updateField("ineligible-prior", endDateDoc.ineligible_prior_to_screen_count, startDateDoc.ineligible_prior_to_screen_count);
    updateField("declined-screen", endDateDoc.declined_to_screen_count, startDateDoc.declined_to_screen_count);
    updateField("screened", endDateDoc.screened_count, startDateDoc.screened_count);
    updateField("screened-ineligible", endDateDoc.ineligible_count, startDateDoc.ineligible_count);
    updateField("eligible-declined", endDateDoc.eligible_but_declined_to_count, startDateDoc.eligible_but_declined_to_count);
    updateField("eligible-undecided", endDateDoc.eligible_undecided_count, startDateDoc.eligible_undecided_count);
    updateField("maybe-eligible", endDateDoc.maybe_eligible_count, startDateDoc.maybe_eligible_count);
    updateField("ies-eligible", endDateDoc.ies_eligible_count, startDateDoc.ies_eligible_count);
    updateField("tele-orientation", endDateDoc.eligible_undecided_count + endDateDoc.maybe_eligible_count + endDateDoc.ies_eligible_count, startDateDoc.eligible_undecided_count + startDateDoc.maybe_eligible_count + startDateDoc.ies_eligible_count);
    updateField("appointment-declined", endDateDoc.appt_declined_count, startDateDoc.appt_declined_count);
    updateField("appointment-needed-week", endDateDoc.appt_needed_within_week_since_ies_count, startDateDoc.appt_needed_within_week_since_ies_count);
    updateField("appointment-needed-over-week", endDateDoc.appt_needed_over_week_since_ies_count, startDateDoc.appt_needed_over_week_since_ies_count);

    updateField("reschedule-no-show", endDateDoc.reschedule_no_show_count, startDateDoc.reschedule_no_show_count);
    updateField("to-scheduled", endDateDoc.to_schedule_count, startDateDoc.to_schedule_count);
    updateField("to-attended", endDateDoc.to_attended_count, startDateDoc.to_attended_count);
    updateField("ineligible-at-to", endDateDoc.ineligible_at_to_count, startDateDoc.ineligible_at_to_count);
    updateField("declined-icf", endDateDoc.declined_icf_count, startDateDoc.declined_icf_count);
    updateField("declined-proceed", endDateDoc.declined_to_proceed_count_1, startDateDoc.declined_to_proceed_count_1);
    updateField("eligible-undecided", endDateDoc.eligible_undecided_count, startDateDoc.eligible_undecided_count);
    updateField("eligible-pending-md", endDateDoc.eligible_pending_clearance_count, startDateDoc.eligible_pending_clearance_count);
    updateField("eligible-at-to", endDateDoc.to_attend_eligible_at_TO_count, startDateDoc.to_attend_eligible_at_TO_count);
    updateField("device-readiness", endDateDoc.self_measure_ready_count, startDateDoc.self_measure_ready_count);
    updateField("baseline-survey", endDateDoc.needs_baseline_survey_count, startDateDoc.needs_baseline_survey_count);
    updateField("setup-pending", endDateDoc.setup_pending_count, startDateDoc.setup_pending_count);
    updateField("setup-complete", endDateDoc.setup_complete_count, startDateDoc.setup_complete_count);
    updateField("eligibility-visit", endDateDoc.visit_scheduled_count, startDateDoc.visit_scheduled_count);
    updateField("appointment-declined", endDateDoc.visit_appt_declined_count, startDateDoc.visit_appt_declined_count);
    updateField("unscheduled-week", endDateDoc.appt_needed_within_week_since_setup_count, startDateDoc.appt_needed_within_week_since_setup_count);
    updateField("unscheduled-over-week", endDateDoc.appt_needed_over_week_since_setup_count, startDateDoc.appt_needed_over_week_since_setup_count);
    updateField("visit-scheduled", endDateDoc.visit_scheduled_count, startDateDoc.visit_scheduled_count);
    updateField("visit-attended", endDateDoc.visit_attended_count, startDateDoc.visit_attended_count);
    updateField("visit-ineligible-at-to", endDateDoc.visit_ineligible_count, startDateDoc.visit_ineligible_count);

    updateField("visit-declined-proceed", endDateDoc.visit_declined_to_proceed_count, startDateDoc.visit_declined_to_proceed_count);
    updateField("visit-pending-outcome", endDateDoc.visit_pending_oc_count, startDateDoc.visit_pending_oc_count);
    updateField("visit-eligible", endDateDoc.visit_eligible_count, startDateDoc.visit_eligible_count);
    updateField("tech-setup", endDateDoc.tech_setup_schedule_count, startDateDoc.tech_setup_schedule_count);
    updateField("decline-devices", endDateDoc.after_techsetup_appt_declined_to_proceed_with_device, startDateDoc.after_techsetup_appt_declined_to_proceed_with_device);
    updateField("unscheduled-week", endDateDoc.appt_needed_within_week_since_visit_count, startDateDoc.appt_needed_within_week_since_visit_count);
    updateField("unscheduled-over-week", endDateDoc.appt_needed_over_week_since_visit_count, startDateDoc.appt_needed_over_week_since_visit_count);
    updateField("reschedule-no-show", endDateDoc.res_no_show_tech_appt_count, startDateDoc.res_no_show_tech_appt_count);
    updateField("tech-setup-scheduled", endDateDoc.tech_setup_schedule_count, startDateDoc.tech_setup_schedule_count);
    updateField("tech-setup-attended", endDateDoc.tech_setup_attended_count, startDateDoc.tech_setup_attended_count);
    updateField("decline-devices-attended", endDateDoc.after_techsetup_appt_declined_to_proceed_with_device_count, startDateDoc.after_techsetup_appt_declined_to_proceed_with_device_count);
    updateField("ineligible-tech-setup", endDateDoc.after_tech_setup_attended_ineligible_count, startDateDoc.after_tech_setup_attended_ineligible_count);
    updateField("pending-tech-issue", endDateDoc.tech_issue_with_device_count, startDateDoc.tech_issue_with_device_count);
    updateField("self-measures-ready", endDateDoc.self_measure_ready_count, startDateDoc.self_measure_ready_count);
    updateField("baseline-self-measures", endDateDoc.self_measure_ready_count, startDateDoc.self_measure_ready_count); // Assuming same field for progress
    updateField("pending-day8", endDateDoc.pending_day_8_count, startDateDoc.pending_day_8_count);
    updateField("pending-day15", endDateDoc.pending_day_15_check, startDateDoc.pending_day_15_check);
    updateField("ineligible-bmi", endDateDoc.ineligible_bmi_count, startDateDoc.ineligible_bmi_count);
    updateField("ineligible-data", endDateDoc.insufficient_data_count, startDateDoc.insufficient_data_count);
    updateField("eligible-pending-randomization", endDateDoc.elig_pending_randamization_count, startDateDoc.elig_pending_randamization_count);
    updateField("randomized", endDateDoc.randamization_count, startDateDoc.randamization_count);

    document.getElementById("r-percent-target").textContent = ((endDateDoc.randamization_count / 440) * 100).toFixed(1) + "%";
}

// Trigger data fetch and display in the table
async function getSummariesAndDisplay() {
    const startDate = document.getElementById('startDateSelect').value;
    const endDate = document.getElementById('endDateSelect').value;
    console.log(startDate)

    if (!startDate || !endDate) {
        alert("Please select valid start and end dates.");
        return;
    }

    // Ensure start date is before or same as end date
    if (new Date(startDate) > new Date(endDate)) {
        alert("Start date cannot be after the end date.");
        return;
    }

    const data = await fetchSummaries(startDate, endDate);
    if (data) populateTable(data.startDateDoc, data.endDateDoc);
}


// Export table data to Excel
function exportToExcel() {
    // Load the template file
  console.log("Clicked export2");
    alert("Hi2");
    fetch("/static/excel/IGNITE Report Template in progress.xlsx")
      .then((response) => response.arrayBuffer())
      .then((data) => {
        // Read the template into a workbook object
        var workbook = XLSX.read(data, { type: "array" });
  
        // Assuming the template has a sheet named "IGNITE Report"
        var wsTemplate = workbook.Sheets["IGNITE Report"];
  
        // Convert the HTML table into a worksheet
        var wsNewData = XLSX.utils.table_to_sheet(
          document.getElementById("recruitment-table")
        );
  
        // Convert the new data worksheet into an array of arrays.
        // (Alternatively, use XLSX.utils.sheet_to_json if you prefer JSON.)
        var newData = XLSX.utils.sheet_to_json(wsNewData, { header: 1 });
  
        // Insert the table data into the template worksheet.
        // Adjust the origin as needed; here we start at A2.
        XLSX.utils.sheet_add_aoa(wsTemplate, newData, { origin: "A2" });
  
        // Write out the updated workbook for download
        XLSX.writeFile(workbook, "ignite_recruitment_report.xlsx");
      })
      .catch((error) => {
        console.error("Error loading the template:", error);
      });
  }
  

// Initialize the page by fetching available dates
fetchAvailableDates();
