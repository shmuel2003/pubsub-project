from dataset_loader import DatasetLoader
from kafka_producer import KafkaPublisher
import time

class PublisherService:
    def __init__(self):
        self.loader = DatasetLoader()
        self.kafka = KafkaPublisher()

    def publish_batch(self):
        samples = self.loader.get_samples()
        for text in samples["interesting"]:
            self.kafka.publish("interesting", {"text": text, "sent_at": time.time()})
        for text in samples["not_interesting"]:
            self.kafka.publish("not_interesting", {"text": text, "sent_at": time.time()})
        return {"status": "20 messages published per category"}