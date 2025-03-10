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
import ignite_recruitment_report  # Import your existing script
from django.views.decorators.csrf import csrf_exempt

# Initialize MongoDB client (global)
client = MongoClient('mongodb://localhost:27017/')
db = client['pivot-report-summaries']  # Your database name
collectionRecruitment = db['summaries']  # Your collection name
collectionMdReview = db['md-review-summaries']
collectionIgniteRecruitment = db['ignite_recruitment_records']  # New collection for Ignite recruitment data

@login_required
def protected_page(request):
    return render(request, 'report/report.html')

@login_required
def ignite_report_page(request):
    """Render the Ignite Report Page."""
    return render(request, 'ignite/index.html')

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

### 🔥 **Newly Integrated Automatic Fetching** 🔥 ###

def fetch_and_store_data_for_ignite():
    """Fetch recruitment data and store it in MongoDB every 2 minutes (Runs in the background)."""
    while True:
        try:
            print("[INFO] Fetching IGNITE recruitment data...")
            data = ignite_recruitment_report.process_redcap_data_for_ignite()

            if not data:
                print("[ERROR] No data received")
            else:
                data["timestamp"] = datetime.datetime.utcnow()
                result = collectionIgniteRecruitment.insert_one(data)
                print(f"[SUCCESS] Data stored successfully: {result.inserted_id}")

        except Exception as e:
            print(f"[ERROR] {str(e)}")

        # Wait for 2 minutes before fetching data again
        time.sleep(120)

# Start the function in a separate thread
def start_background_task():
    thread = threading.Thread(target=fetch_and_store_data_for_ignite, daemon=True)
    thread.start()

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
        return redirect('protected')  # Redirect authenticated users
    return redirect(reverse('login'))  # Redirect unauthenticated users
