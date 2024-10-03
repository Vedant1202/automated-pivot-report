from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from pymongo import MongoClient
from bson.json_util import dumps
import json

@login_required
def protected_page(request):
    return render(request, 'report/report.html')


# Initialize MongoDB client (best practice to do this once globally)
client = MongoClient('mongodb://localhost:27017/')
db = client['pivot-report-summaries']  # Replace with your database name
collectionRecruitment = db['summaries']  # Replace with your collection name
collectionMdReview = db['md-review-summaries']  # Replace with your collection name

@login_required
@api_view(['POST'])
def get_recruitment_data_from_mongo(request):
    # if request.method == 'POST':
        try:
            # Parse the request body to get the startDate and endDate
            # print(request.body)
            start_date = request.POST.get('startDate')
            end_date = request.POST.get('endDate')
            (start_date, end_date)

            if not start_date or not end_date:
                return JsonResponse({"error": "Missing 'startDate' or 'endDate'"}, status=400)

            # Query the collection for documents with the specific dates
            start_date_doc = collectionRecruitment.find_one({"date": start_date})
            end_date_doc = collectionRecruitment.find_one({"date": end_date})

            if start_date_doc is None or end_date_doc is None:
                return JsonResponse({"error": "Documents not found for the provided dates"}, status=404)

            # Return the documents as a JSON response
            response_data = {
                "startDateDoc": json.loads(dumps(start_date_doc)),
                "endDateDoc": json.loads(dumps(end_date_doc))
            }

            return JsonResponse(response_data)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    # else:
    #     return JsonResponse({"error": "Invalid request method"}, status=405)

@login_required
@api_view(['POST'])
def get_mdreview_data_from_mongo(request):
    # if request.method == 'POST':
        try:
            # Parse the request body to get the startDate and endDate
            # print(request.body)
            start_date = request.POST.get('startDate')
            end_date = request.POST.get('endDate')
            (start_date, end_date)

            if not start_date or not end_date:
                return JsonResponse({"error": "Missing 'startDate' or 'endDate'"}, status=400)

            # Query the collection for documents with the specific dates
            start_date_doc = collectionMdReview.find_one({"date": start_date})
            end_date_doc = collectionMdReview.find_one({"date": end_date})

            if start_date_doc is None or end_date_doc is None:
                return JsonResponse({"error": "Documents not found for the provided dates"}, status=404)

            # Return the documents as a JSON response
            response_data = {
                "startDateDoc": json.loads(dumps(start_date_doc)),
                "endDateDoc": json.loads(dumps(end_date_doc))
            }

            return JsonResponse(response_data)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    # else:
    #     return JsonResponse({"error": "Invalid request method"}, status=405)

from django.shortcuts import redirect
from django.urls import reverse
from django.http import Http404

def custom_404_view(request, exception):
    if request.user.is_authenticated:
        # Redirect to a protected page if the user is logged in
        return redirect('protected')  # Replace with your protected URL name
    else:
        # Redirect to the login page if the user is not logged in
        return redirect(reverse('login'))  # Ensure this matches your login URL name
