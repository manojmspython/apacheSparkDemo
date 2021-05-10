"""Producer application for kafka"""

from kafka import KafkaProducer
import json
from random import random
import logging
from config import KAFKA_CONFIG, TOPIC

logging.basicConfig(level=logging.INFO)


class SendData(object):
    KAFKA_CONFIG = KAFKA_CONFIG
    TOPIC = TOPIC

    @staticmethod
    def on_send_success(record_metadata):
        """
        Call back function to log details on success of producer pushed data into kafka.

        :param record_metadata: details of the pushed data.
        :return: None
        """
        logging.info(
            f"data successfully pushed into topic: {record_metadata.topic}, partition: {record_metadata.partition}, offset: {record_metadata.offset}"
        )

    @staticmethod
    def on_send_error(excp):
        """
        Call back function to log details exception while producer failed to pushed data into kafka.
        :param excp: Exception
        :return: None
        """
        logging.exception(excp)

    def __init__(self):
        self.producer = KafkaProducer(
            **self.KAFKA_CONFIG,
            value_serializer=lambda m: json.dumps(m).encode("ascii"),
        )

    def send_data(self):
        """
        Sends data into Kafka.
        :return: None
        """
        self.producer.send(
            self.TOPIC, {"name": "Dummy", "age": f"{random()}"}
        ).add_callback(SendData.on_send_success).add_errback(SendData.on_send_error)
        """flush should be used here when multiple future/messages 
        are being added to producer else it takes sometime to push into kafka"""

        self.producer.flush()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        On exit in case of any open connection try to close that gracefully.
        :param exc_type: exc_type
        :param exc_val: exc_val
        :param exc_tb: exc_tb
        :return: None
        """
        self.producer.close()


if __name__ == "__main__":
    SendData().send_data()
