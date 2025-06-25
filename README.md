# 📊 Real-Time Smart Attendance Tracker (Cloud-Based)

This project is a **cloud-based attendance tracking system** using **Google Cloud Platform** and **Firebase**. It allows uploading a `.csv` file to a GCS bucket, automatically processes and stores data into **Firestore**, and displays it in a real-time updating **JavaScript dashboard**.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🔧 Technologies & Services Used

| Service                                   | Purpose                                                                 |
|-------------------------------------------|-------------------------------------------------------------------------|
| **Google Cloud Storage (GCS)**            | To upload `.csv` files containing attendance data                       |
| **Cloud Pub/Sub**                         | Messaging layer triggered when a file is uploaded                       |
| **Cloud Functions**                       | Serverless backend to parse uploaded `.csv` and push to Firestore       |
| **Firebase Firestore**                    | NoSQL database to store attendance entries                              |
| **Firebase Hosting (Optional)**           | To host the real-time web dashboard (if needed)                         |
| **JavaScript + Firebase SDK**             | For frontend dashboard to show real-time updates                        |

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🛠️ How It Works

### 1. Upload `.csv` to GCS Bucket
- Bucket Name: `attendance-tracker-upload-madhura`
- Trigger: When a `.csv` file is uploaded

### 2. GCS Event triggers **Cloud Function**
- Cloud Function Name: `process_attendance`
- Reads the `.csv` file
- Extracts rows like: `Name, Date, Status`
- Pushes data into Firestore (Collection: `attendance`)

### 3. Firestore stores structured data
Example document:
```json
{
  "Name": "Madhura",
  "Date": "2025-06-25",
  "Status": "Present"
}

### 4. JavaScript Dashboard shows data
>Connects to Firestore using Firebase SDK
>Displays real-time table on webpage
>Updates instantly when Firestore changes

### 5. Running the Dashboard Locally
>Copy index.html (provided in this repo)
>Paste your Firebase config from [Firebase Console > Project Settings > Web App]
>Double-click the HTML file to open in browser
You’ll see a live-updating attendance table!

🗂️ Folder Structure

gcs-function/
├── attendance-function/        # Cloud Function Python code
│   └── main.py                 # Parses CSV and updates Firestore
│   └── requirements.txt        # Python deps (google-cloud packages)
├── dashboard/
│   └── index.html              # Real-time dashboard UI

