from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'machines-data',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

TEMP_LIMIT = 90     # حد خطر للحرارة
VIB_LIMIT = 3       # حد خطر للاهتزاز

print("Listening for machine data...")

for message in consumer:
    data = message.value
    machine_id = data["machine_id"]
    temp = data["temperature"]
    vib = data["vibration"]

    alert = []

    if temp > TEMP_LIMIT:
        alert.append(f"Temp haute: {temp}")
    if vib > VIB_LIMIT:
        alert.append(f"Vibration élevée: {vib}")

    if alert:
        print(f"⚠️  ALERTE machine {machine_id}: {', '.join(alert)}")
    else:
        print(f"✅ machine {machine_id} OK - temp={temp}, vib={vib}")
