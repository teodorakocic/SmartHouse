import paho.mqtt.client as mqtt
import json
from influxdb import InfluxDBClient
from datetime import datetime
from os import environ

broker_address  = environ.get("BROKER_ADDRESS", "127.0.0.1")
topic           = environ.get("TOPIC", "edgex-tutorial")
dbhost          = environ.get("INFLUXDB_HOST", "127.0.0.1")
dbport          = int(environ.get("INFLUXDB_PORT", "8086"))
dbuser          = environ.get("INFLUXDB_USERNAME", "admin")
dbpassword      = environ.get("INFLUXDB_PASSWORD", "admin")
dbname          = environ.get("INFLUXDB_DATABASE", "sensordata")

def influxDBconnect():
    return InfluxDBClient(dbhost, dbport, dbuser, dbpassword, dbname)

def influxDBwrite(device, sensorName, sensorValue):
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    measurementData = [
        {
            "measurement": device,
            "tags": {
                "gateway": device,
                "location": "Nis"
            },
            "time": timestamp,
            "fields": {
                sensorName: sensorValue
            }
        }
    ]
    print(measurementData)
    influxDBConnection.write_points(measurementData, time_precision='ms')

def on_message(client, userdata, message):
    m = str(message.payload.decode("utf-8"))
    obj = json.loads(m)

    for entry in obj["readings"]:
        device      = entry["device"]
        sensorName  = entry["name"]
        sensorValue = entry["value"]
        if sensorValue.isdecimal():
            sensorValue = float(sensorValue)
        influxDBwrite(device, sensorName, sensorValue)

influxDBConnection = influxDBconnect()

print("Creating new instance ...")
client = mqtt.Client() 
client.on_message=on_message 
# client.username_pw_set("mqttUser", "mqttPass")

print("Connecting to broker ...")
client.connect(broker_address, 1883) 
print("...done")

client.subscribe(topic)
client.loop_forever()