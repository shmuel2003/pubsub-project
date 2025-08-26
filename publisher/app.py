from fastapi import FastAPI
from publisher_service import PublisherService

app = FastAPI()
service = PublisherService()

@app.get("/publish")
def publish():
    return service.publish_batch()