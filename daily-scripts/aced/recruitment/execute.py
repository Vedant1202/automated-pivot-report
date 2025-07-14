import pymongo
from datetime import datetime
from aced_recruitment_report import fetch_aced_recruitment_data  # if kept in another file

def save_to_mongo(siteDict):
    today = datetime.today().strftime('%m-%d-%Y')
    
    # Setup MongoDB client
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["aced_automated_reporting"]
    collection = db["recruitment"]

    # Create document
    document = {
        "data": siteDict,
        "date": today
    }

    # Insert into MongoDB
    collection.insert_one(document)
    print(f"Data saved for {today}")

if __name__ == "__main__":
    siteDict = fetch_aced_recruitment_data()
    save_to_mongo(siteDict)
