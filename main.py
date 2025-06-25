import functions_framework
from google.cloud import storage, firestore
import csv

@functions_framework.cloud_event
def process_attendance(cloud_event):
    bucket_name = cloud_event.data["bucket"]
    file_name = cloud_event.data["name"]

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    content = blob.download_as_text().splitlines()

    db = firestore.Client()
    reader = csv.DictReader(content)
    
    for row in reader:
        doc_ref = db.collection("attendance").document()
        doc_ref.set(dict(row))

    print(f"Attendance from {file_name} saved to Firestore")
