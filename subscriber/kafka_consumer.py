from kafka import KafkaConsumer
import json

class KafkaSubscriber:
    def __init__(self, topic: str, bootstrap_servers="kafka:9092"):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            value_deserializer=lambda v: json.loads(v.decode("utf-8")),
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            group_id=f"group_{topic}"
        )

    def listen(self):
        for message in self.consumer:
            yield message.value
