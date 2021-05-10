import json
import logging
from random import random

from kafka import KafkaProducer

from config import KAFKA_CONFIG, TOPIC

logging.basicConfig(level=logging.INFO)


class SendData(object):
    KAFKA_CONFIG = KAFKA_CONFIG
    TOPIC = TOPIC

    @staticmethod
    def on_send_success(record_metadata):
        logging.info(
            f"data successfully pushed into topic: {record_metadata.topic}, partition: {record_metadata.partition}, offset: {record_metadata.offset}"
        )

    @staticmethod
    def on_send_error(excp):
        logging.exception(excp)

    def __init__(self):
        self.producer = KafkaProducer(
            **self.KAFKA_CONFIG,
            value_serializer=lambda m: json.dumps(m).encode("ascii"),
        )

    def send_data(self):
        self.producer.send(
            self.TOPIC, {"name": "Dummy", "age": f"{random()}"}
        ).add_callback(SendData.on_send_success).add_errback(SendData.on_send_error)
        self.producer.flush()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.producer.close()


if __name__ == "__main__":
    SendData().send_data()
