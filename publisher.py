import paho.mqtt.client as mqtt
import json
import time
import random

# Free Cloud MQTT Broker (HiveMQ)
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "iot/mobile/sensor"

# Function to simulate sensor data
def get_sensor_data():
    return {
        "device_id": "mobile_001",
        "timestamp": time.time(),
        "gps": {
            "latitude": round(random.uniform(-90.0, 90.0), 6),
            "longitude": round(random.uniform(-180.0, 180.0), 6)
        },
        "temperature": round(random.uniform(20.0, 40.0), 2)
    }

# Setup MQTT client
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Keep the connection alive
client.loop_start()

try:
    while True:
        data = get_sensor_data()
        payload = json.dumps(data)
        result = client.publish(MQTT_TOPIC, payload)
        
        # Print only if publish was successful
        if result.rc == mqtt.MQTT_ERR_SUCCESS:
            print(f"Published: {payload}")
        else:
            print("Failed to publish message")
        
        time.sleep(5)  # Send message every 5 seconds

except KeyboardInterrupt:
    print("Stopping Publisher")
    client.loop_stop()
    client.disconnect()
