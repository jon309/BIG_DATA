from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_machine_data(machine_id):
    return {
        "machine_id": machine_id,
        "temperature": round(random.uniform(40, 110), 2),  # درجة الحرارة
        "vibration": round(random.uniform(0, 5), 2),       # الاهتزاز
        "status": "OK"
    }

if __name__ == "__main__":
    while True:
        for machine_id in range(1, 4): 
            data = generate_machine_data(machine_id)
            print("Send:", data)
            producer.send('machines-data', data)
        time.sleep(1)
