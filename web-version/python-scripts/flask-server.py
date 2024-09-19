from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
from bson import json_util
from flask_cors import CORS  # Import CORS

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Set up MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['pivot-report-summaries']
collection = db['summaries']

# POST endpoint to fetch documents by date range
@app.route('/fetch-summary', methods=['POST'])
def fetch_summary():
    data = request.get_json()

    start_date_str = data.get('startDate')
    end_date_str = data.get('endDate')

    # Convert string dates to datetime objects
    try:
        start_date = start_date_str
        end_date = end_date_str
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

    # Fetch matching documents for the given dates
    print(start_date, end_date)
    start_date_doc = collection.find_one({"date": start_date})
    end_date_doc = collection.find_one({"date": end_date})
    

    # If documents are found, return them, else return error message
# If documents are found, return them, else return error message
    if start_date_doc and end_date_doc:
        # Use json_util to serialize the MongoDB documents properly
        return json_util.dumps({
            "startDateDoc": start_date_doc,
            "endDateDoc": end_date_doc
        }), 200
    else:
        return jsonify({"error": "Documents not found for the provided dates"}), 404


if __name__ == '__main__':
    app.run(debug=True)
