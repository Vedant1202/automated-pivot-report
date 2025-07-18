import pymongo
from datetime import datetime
from aced_recruitment_report import fetch_aced_recruitment_data  # if kept in another file

def save_to_mongo(fetchedData):
    today = datetime.today().strftime('%m-%d-%Y')
    
    # Setup MongoDB client
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["aced_automated_reporting"]
    collection = db["recruitment"]

    # Create document
    document = {
        "data": fetchedData["siteDict"],
        "date": today,
        "milestone_date": fetchedData["milestone_date"],
        "target_value": fetchedData["target_value"],
        "stanford_summary_data": {
            "honest_broker_ceased_outreach_count": fetchedData["stanford_summary_data"]["honest_broker_ceased_outreach_count"],
            "honest_broker_partial_screen": fetchedData["stanford_summary_data"]["honest_broker_partial_screen"],
            "stanford_public_ceased_outreach_count": fetchedData["stanford_summary_data"]["stanford_public_ceased_outreach_count"],
            "stanford_public_partial_screen": fetchedData["stanford_summary_data"]["stanford_public_partial_screen"]
        }
    }

    # Insert into MongoDB
    collection.insert_one(document)
    print(f"Data saved for {today}")

if __name__ == "__main__":
    fetchedData = fetch_aced_recruitment_data()
    save_to_mongo(fetchedData)
