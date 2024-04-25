import requests
import json
from time import sleep
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         x.encode('utf-8'))

while True:
    url = 'https://environment.data.gov.uk/flood-monitoring/id/floods'
    response = requests.get(url)
    items = response.json()['items']
    message = json.dumps(items)
    producer.send('uk-flood', value=message)
    sleep(10)
