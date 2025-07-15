from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse, Http404
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from pymongo import MongoClient
from bson.json_util import dumps
import json
import datetime
import threading
import time

## IGNITE
import ignite_recruitment_report
from django.views.decorators.csrf import csrf_exempt
from ignite_detailed_list import fetch_redcap_staff_report
from ignite_self_harm import process_self_harm_data
from ignite_intervention_report import fetch_ignite_intervention_report

## ACED
from aced_scripts.aced_exclusions_refusals import getExclusionsRefusalsData

## For scheduler
from apscheduler.schedulers.background import BackgroundScheduler
from django.utils.timezone import now
import datetime
import threading
import pytz

# Initialize MongoDB client (global)
client = MongoClient('mongodb://localhost:27017/')

db = client['pivot-report-summaries']  # Your database name
ignite_db = client['ignite_report_db']
aced_db = client["aced_automated_reporting"]

collectionRecruitment = db['summaries']  # Your collection name
collectionMdReview = db['md-review-summaries']

collectionIgniteRecruitment = ignite_db['ignite_recruitment_records']  # New collection for Ignite recruitment data
collectionAcedRecruitment = aced_db['recruitment']  # New collection for ACED recruitment data

@login_required
def protected_page(request):
    return render(request, 'report/report.html')

@login_required
def ignite_report_page(request):
    """Render the Ignite Report Page."""
    return render(request, 'ignite/index.html')

@login_required
def aced_report_page(request):
    """Render the Ignite Report Page."""
    return render(request, 'aced/index.html')

@login_required
@api_view(['POST'])
def get_recruitment_data_from_mongo(request):
    try:
        start_date = request.POST.get('startDate')
        end_date = request.POST.get('endDate')

        if not start_date or not end_date:
            return JsonResponse({"error": "Missing 'startDate' or 'endDate'"}, status=400)

        start_date_doc = collectionRecruitment.find_one({"date": start_date})
        end_date_doc = collectionRecruitment.find_one({"date": end_date})

        if start_date_doc is None or end_date_doc is None:
            return JsonResponse({"error": "Documents not found for the provided dates"}, status=404)

        response_data = {
            "startDateDoc": json.loads(dumps(start_date_doc)),
            "endDateDoc": json.loads(dumps(end_date_doc))
        }
        return JsonResponse(response_data)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@login_required
@api_view(['POST'])
def get_mdreview_data_from_mongo(request):
    try:
        start_date = request.POST.get('startDate')
        end_date = request.POST.get('endDate')

        if not start_date or not end_date:
            return JsonResponse({"error": "Missing 'startDate' or 'endDate'"}, status=400)

        start_date_doc = collectionMdReview.find_one({"date": start_date})
        end_date_doc = collectionMdReview.find_one({"date": end_date})

        if start_date_doc is None or end_date_doc is None:
            return JsonResponse({"error": "Documents not found for the provided dates"}, status=404)

        response_data = {
            "startDateDoc": json.loads(dumps(start_date_doc)),
            "endDateDoc": json.loads(dumps(end_date_doc))
        }
        return JsonResponse(response_data)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@login_required
@api_view(['GET'])
def get_available_dates(request):
    dates = collectionRecruitment.distinct('date')
    return JsonResponse({'dates': dates})

@csrf_exempt
@api_view(['GET'])
@login_required
def get_detailed_staff_report(request):
    """
    GET endpoint to return staff activity summary from REDCap.
    """
    try:
        report_data = fetch_redcap_staff_report()
        return JsonResponse(report_data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
@api_view(['GET'])
@login_required
def get_ignite_intervention_report(request):
    """
    GET endpoint to return staff activity summary from REDCap.
    """
    try:
        report_data = fetch_ignite_intervention_report()
        return JsonResponse(report_data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
@api_view(['GET'])
@login_required
def get_selfharm_summary(request):
    """
    GET endpoint to return the self-harm REDCap summary report.
    """
    try:
        summary_data = process_self_harm_data()
        return JsonResponse(summary_data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
@csrf_exempt
@api_view(['GET'])
@login_required
def get_aced_exclusions_refusals_data(request):
    """
        GET endpoint to return the exclusions refusals for ACED REDCap summary report.
    """
    try:
        summary_data = getExclusionsRefusalsData()
        return JsonResponse(summary_data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
@api_view(['GET'])
# @login_required
def get_aced_recruitment_data(request):
    """
    GET endpoint to return ACED REDCap recruitment data between two dates.
    Expects startDate and endDate as URL parameters in mm-dd-yyyy format.
    Example: /api/aced-data?startDate=07-01-2025&endDate=07-08-2025
    """
    try:
        start_date = request.GET.get('startDate')
        end_date = request.GET.get('endDate')

        print(start_date)
        print(end_date)

        if not start_date or not end_date:
            return JsonResponse({"error": "Missing 'startDate' or 'endDate'"}, status=400)

        start_date_doc = collectionAcedRecruitment.find_one({"date": start_date})
        end_date_doc = collectionAcedRecruitment.find_one({"date": end_date})

        if not start_date_doc or not end_date_doc:
            return JsonResponse({"error": "Data not found for one or both dates"}, status=500)

        response = {
            "startDateDoc": json.loads(dumps(start_date_doc)),
            "endDateDoc": json.loads(dumps(end_date_doc)),
        }

        return JsonResponse(response)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


#### =========== SCHEDULING =================

# Initialize APScheduler
scheduler = BackgroundScheduler()
# Set the timezone to Central Time (CST/CDT)
central_tz = pytz.timezone('America/Chicago')

# Schedule fetching of data daily
def fetch_and_store_data_for_ignite():
    """Fetch recruitment data once per day and store it in MongoDB."""
    try:
        now_central = datetime.datetime.now(central_tz).isoformat()
        print(f"[INFO] Fetching IGNITE recruitment data at {now_central} CST/CDT...")
        data = ignite_recruitment_report.process_redcap_data_for_ignite()

        if not data:
            print("[ERROR] No data received")
        else:
            data["timestamp"] = now_central  # Store timestamp in CST/CDT
            result = collectionIgniteRecruitment.insert_one(data)
            print(f"[SUCCESS] Data stored successfully: {result.inserted_id}")

    except Exception as e:
        print(f"[ERROR] {str(e)}")

def schedule_daily_fetch(hour=3, minute=00):
    """Schedule `fetch_and_store_data_for_ignite` to run daily at a specified time in CST/CDT."""
    scheduler.add_job(
        fetch_and_store_data_for_ignite, 
        'cron', 
        hour=hour, 
        minute=minute,
        timezone=central_tz  # Set timezone to America/Chicago (CST/CDT)
    )
    print(f"[Scheduler] Scheduled `fetch_and_store_data_for_ignite` at {hour}:{minute} CST/CDT daily")

# Start the scheduler when the server starts
def start_scheduler():
    scheduler.start()
    schedule_daily_fetch(hour=3, minute=00)  # Change time as needed

# Run scheduler in a separate thread
def start_background_task():
    threading.Thread(target=start_scheduler, daemon=True).start()

#### ==============================

@csrf_exempt
@api_view(['GET'])
@login_required
def get_saved_data_for_ignite(request):
    """Retrieve stored Ignite recruitment data based on date range."""
    try:
        start_date_str = request.GET.get("start", "")
        end_date_str = request.GET.get("end", "")

        if not start_date_str or not end_date_str:
            return JsonResponse({"error": "Missing 'start' or 'end' parameters"}, status=400)

        start_date = datetime.datetime.strptime(start_date_str, "%Y%m%d").date()
        end_date = datetime.datetime.strptime(end_date_str, "%Y%m%d").date()

        print(f"Requested Start Date: {start_date}")
        print(f"Requested End Date: {end_date}")

        startDateDoc = collectionIgniteRecruitment.find_one(
            {"timestamp": {"$regex": f"^{start_date.strftime('%Y-%m-%d')}" }},
            {"_id": 0}
        )

        endDateDoc = collectionIgniteRecruitment.find_one(
            {"timestamp": {"$regex": f"^{end_date.strftime('%Y-%m-%d')}" }},
            {"_id": 0}
        )

        if not startDateDoc or not endDateDoc:
            return JsonResponse({"error": "No data found for the selected dates"}, status=404)

        return JsonResponse({"startDateDoc": startDateDoc, "endDateDoc": endDateDoc})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def custom_404_view(request, exception):
    if request.user.is_authenticated:
        return redirect('ignite/report')  # Redirect authenticated users
    return redirect(reverse('login'))  # Redirect unauthenticated users


# Start the scheduled background task when the server starts
start_background_task()