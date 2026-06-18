from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import datetime
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

notifications = [
    {"id": 1, "title": "Exam Schedule Out", "sender": "Dean Office", "text": "The final exam schedule is published.", "time": "2026-06-18 10:00:00"},
    {"id": 2, "title": "Free Pizza", "sender": "Student Club", "text": "Free pizza at the lounge now!", "time": "2026-06-18 11:30:00"},
    {"id": 3, "title": "Urgent: Fee Deadline", "sender": "Finance", "text": "Pay your tuition fee by tonight to avoid a penalty.", "time": "2026-06-18 09:00:00"}
]

HIGH_PRIORITY_SENDERS = {"Dean Office", "Finance", "Facilities", "Career Cell"}
URGENT_KEYWORDS = {"urgent", "deadline", "emergency", "immediately", "exam", "pay"}

def calculate_priority(notification):
    score = 0
    if notification["sender"] in HIGH_PRIORITY_SENDERS:
        score += 50
    content_lower = (notification["title"] + " " + notification["text"]).lower()
    if any(keyword in content_lower for keyword in URGENT_KEYWORDS):
        score += 40
    return score

@app.get("/api/notifications/priority")
def get_priority_notifications():
    for n in notifications:
        n["priority_score"] = calculate_priority(n)
    
    sorted_notif = sorted(
        notifications, 
        key=lambda x: (x["priority_score"], x["time"]), 
        reverse=True
    )[:10]
    return sorted_notif

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
