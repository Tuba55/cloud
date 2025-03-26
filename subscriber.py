import paho.mqtt.client as mqtt

# Free Cloud MQTT Broker
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "iot/mobile/sensor"

# Callback function when a connection is established
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(MQTT_TOPIC)  # Subscribe after connection
    else:
        print(f"Connection failed with code {rc}")

# Callback function when a message is received
def on_message(client, userdata, msg):
    print(f"Received: {msg.payload.decode()}")

# Setup MQTT Client
client = mqtt.Client()

client.on_connect = on_connect  # Attach connection callback
client.on_message = on_message  # Attach message received callback

# Connect to the MQTT broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

print("Waiting for messages...")
client.loop_forever()  # Keep the subscriber running