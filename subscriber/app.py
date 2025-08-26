from fastapi import FastAPI
from subscriber_service import SubscriberService

TOPIC = "interesting"   # or "not_interesting"

app = FastAPI()
service = SubscriberService(TOPIC)
service.start_listening()

@app.get("/messages")
def get_messages():
    return service.get_messages()