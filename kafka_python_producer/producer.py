import json
import time

from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers='rover-cluster-kafka-bootstrap:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
    producer.send('123test', {'foo': 'bar'})
    time.sleep(3)
