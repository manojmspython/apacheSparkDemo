"""Pytests"""
from kafka import KafkaConsumer, KafkaProducer

from .config import KAFKA_CONFIG, GROUP_ID, TOPIC


def test_consumer_producer():
    """
    Simple test function that tests the consumer and producer connection is working end to end.
    :return:
    """
    producer = KafkaProducer(**KAFKA_CONFIG, value_serializer=str.encode)
    consumer = KafkaConsumer(
        **KAFKA_CONFIG,
        value_deserializer=bytes.decode,
        group_id=GROUP_ID,
        consumer_timeout_ms=30000,
        auto_offset_reset="earliest",
    )

    topic = TOPIC

    messages = 2
    futures = []
    for i in range(messages):
        futures.append(producer.send(topic, "msg %d" % i))
    ret = [f.get(timeout=30) for f in futures]
    assert len(ret) == messages
    producer.close()

    consumer.subscribe([topic])
    msgs = set()
    for i in range(messages):
        try:
            msgs.add(next(consumer).value)
        except StopIteration:
            break

    assert msgs == set(["msg %d" % (i,) for i in range(messages)])
    consumer.close()
