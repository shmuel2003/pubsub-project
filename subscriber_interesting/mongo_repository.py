from pymongo import MongoClient
import time

class MongoRepository:
    def __init__(self, db_name="pubsubDB", collection_name="messages"):
        client = MongoClient("mongodb://mongo:27017/")
        self.collection = client[db_name][collection_name]

    def insert_message(self, message: dict):
        message["timestamp"] = time.time()
        self.collection.insert_one(message)

    def get_all_messages(self):
        return list(self.collection.find({}, {"_id": 0}))