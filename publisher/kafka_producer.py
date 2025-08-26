from kafka import KafkaProducer
import json

class KafkaPublisher:
    def __init__(self, bootstrap_servers="kafka:9092"):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )

    def publish(self, topic: str, message: dict):
        self.producer.send(topic, value=message)
        self.producer.flush()