"""Consumer application that consumes data from queue and pushes data in postgres."""
import json
import logging

from kafka import KafkaConsumer
from sqlalchemy import create_engine

from config import KAFKA_CONFIG, GROUP_ID, TOPIC, URI
from db_push import dump_data

engine = create_engine(URI, echo=True)

logging.basicConfig(level=logging.INFO)


class ConsumeData(object):
    KAFKA_CONFIG = KAFKA_CONFIG

    @staticmethod
    def on_send_success(record_metadata):
        """
        Call back function to log details on success of consumer able to consume the data.

        :param record_metadata: details of the consumed data from queue.
        :return: None
        """
        logging.info(
            f"data successfully pushed into topic: {record_metadata.topic}, partition: {record_metadata.partition}, offset: {record_metadata.offset}"
        )

    @staticmethod
    def on_send_error(excp):
        """
        Call back function to log details exception while consumer failed to consume data.
        :param excp: Exception
        :return: None
        """
        logging.exception(excp)

    @staticmethod
    def desereliazer(data):
        """
        Json Desereliazer.
        :param data: Message from consumer
        :return: Json
        """
        return json.loads(data)

    def __init__(self):
        self.consumer = KafkaConsumer(
            **self.KAFKA_CONFIG,
            group_id=GROUP_ID,
            value_deserializer=ConsumeData.desereliazer,
        )
        self.consumer.subscribe(TOPIC)

    def consume_data(self):
        """
        Consumes data from queue and pushes data in postgres.
        :return: None
        """

        # assumption the consumer is setup using queue architecture else duplication of data can occur in DB.
        try:
            for message in self.consumer:
                logging.info(
                    "%s:%d:%d: key=%s value=%s"
                    % (
                        message.topic,
                        message.partition,
                        message.offset,
                        message.key,
                        message.value,
                    )
                )
                dump_data(data=message.value, engine=engine)

        except Exception as e:
            logging.error(f"Some error occured with context as {e}")
        finally:
            self.consumer.close()


if __name__ == "__main__":
    ConsumeData().consume_data()
