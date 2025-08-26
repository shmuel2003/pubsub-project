from kafka_consumer import KafkaSubscriber
from mongo_repository import MongoRepository
import threading

class SubscriberService:
    def __init__(self, topic: str):
        self.topic = topic
        self.repo = MongoRepository(collection_name=topic)
        self.consumer = KafkaSubscriber(topic)

    def start_listening(self):
        def run():
            for msg in self.consumer.listen():
                self.repo.insert_message(msg)
        thread = threading.Thread(target=run, daemon=True)
        thread.start()

    def get_messages(self):
        return self.repo.get_all_messages()