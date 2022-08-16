import requests, json, sys, re, time, os, warnings, argparse
from requests_toolbelt.multipart.encoder import MultipartEncoder
from datetime import datetime

warnings.filterwarnings("ignore")

parser=argparse.ArgumentParser(description="Python script for creating a new device from scratch in EdgeX Foundry")
parser.add_argument('-ip',help='EdgeX Foundry IP address', required=True)

args=vars(parser.parse_args())

edgex_ip=args["ip"]


def createValueDescriptors():
    url = 'http://%s:48080/api/v1/valuedescriptor' % edgex_ip

    payload =   {
                    "name":"dishwasher",
                    "description":"Energy consumed by dishwasher in W", 
                    "min":"0",
                    "max":"10000",
                    "type":"Int64",
                    "uomLabel":"count",
                    "defaultValue":"0",
                    "formatting":"%s",
                    "labels":["environment", "dishwasher"]
                }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
    print("Result for createValueDescriptors #1: %s - Message: %s" % (response, response.text))

    payload =   {
                    "name":"microwave",
                    "description":"Energy consumed by microwave in W", 
                    "min":"0",
                    "max":"10000",
                    "type":"Int64",
                    "uomLabel":"count",
                    "defaultValue":"0",
                    "formatting":"%s",
                    "labels":["environment","microwave"]
                }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
    print("Result for createValueDescriptors #2: %s - Message: %s" % (response, response.text))


    payload =   {
                    "name":"fridge",
                    "description":"Energy consumed by fridge in W", 
                    "min":"0",
                    "max":"10000",
                    "type":"Int64",
                    "uomLabel":"count",
                    "defaultValue":"0",
                    "formatting":"%s",
                    "labels":["environment","fridge"]
                }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
    print("Result for createValueDescriptors #3: %s - Message: %s" % (response, response.text))


    payload =   {
                    "name":"washingmachine",
                    "description":"Energy consumed by washingmachine in W", 
                    "min":"0",
                    "max":"10000",
                    "type":"Int64",
                    "uomLabel":"count",
                    "defaultValue":"0",
                    "formatting":"%s",
                    "labels":["environment","washingmachine"]
                }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
    print("Result for createValueDescriptors #4: %s - Message: %s" % (response, response.text))


    payload =   {
                    "name":"tvairconditioner",
                    "description":"Energy consumed by TV and air conditioner in W", 
                    "min":"0",
                    "max":"10000",
                    "type":"Int64",
                    "uomLabel":"count",
                    "defaultValue":"0",
                    "formatting":"%s",
                    "labels":["environment","tvairconditioner"]
                }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
    print("Result for createValueDescriptors #5: %s - Message: %s" % (response, response.text))


    payload =   {
                    "name":"printerscanner",
                    "description":"Energy consumed by printer and scanner in W", 
                    "min":"0",
                    "max":"10000",
                    "type":"Int64",
                    "uomLabel":"count",
                    "defaultValue":"0",
                    "formatting":"%s",
                    "labels":["environment","printerscanner"]
                }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
    print("Result for createValueDescriptors #6: %s - Message: %s" % (response, response.text))


    payload =   {
                    "name":"furnace",
                    "description":"Energy consumed by furnace in W", 
                    "min":"0",
                    "max":"10000",
                    "type":"Int64",
                    "uomLabel":"count",
                    "defaultValue":"0",
                    "formatting":"%s",
                    "labels":["environment","furnace"]
                }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
    print("Result for createValueDescriptors #7: %s - Message: %s" % (response, response.text))


    payload =   {
                    "name":"garagedoor",
                    "description":"Energy consumed by garage door in W", 
                    "min":"0",
                    "max":"10000",
                    "type":"Int64",
                    "uomLabel":"count",
                    "defaultValue":"0",
                    "formatting":"%s",
                    "labels":["environment","garagedoor"]
                }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
    print("Result for createValueDescriptors #8: %s - Message: %s" % (response, response.text))


    payload =   {
                    "name":"generator",
                    "description":"Energy generated in total in W", 
                    "min":"0",
                    "max":"10000",
                    "type":"Int64",
                    "uomLabel":"count",
                    "defaultValue":"0",
                    "formatting":"%s",
                    "labels":["environment","generator"]
                }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
    print("Result for createValueDescriptors #9: %s - Message: %s" % (response, response.text))



def uploadDeviceProfile():
    multipart_data = MultipartEncoder(
        fields={
                'file': ('sensorClusterDeviceProfile.yaml', open('sensorClusterDeviceProfile.yaml', 'rb'), 'text/plain')
               }
        )

    url = 'http://%s:48081/api/v1/deviceprofile/uploadfile' % edgex_ip
    response = requests.post(url, data=multipart_data,
                      headers={'Content-Type': multipart_data.content_type})

    print("Result of uploading device profile: %s with message %s" % (response, response.text))



def addNewDevice():
    url = 'http://%s:48081/api/v1/device' % edgex_ip

    payload =   {
                    "name":"Sensor_cluster_smart_house_v2",
                    "description":"Sensor cluster for smart house version 2.0",
                    "adminState":"unlocked",
                    "operatingState":"enabled",
                    "protocols": {
                        "example": {
                        "host": "tea",
                        "port": "2904",
                        "unitID": "1"
                        }
                    },
                    "labels": ["Dishwasher sensor","Microwave sensor", "Fridge sensor", "Washingmachine sensor", "TVAirconditioner sensor", "PrinterScanner sensor", "Furnace sensor", "Garagedoor sensor", "Generator sensor"],
                    "location":"Nis",
                    "service": {
                        "name":"edgex-device-rest"
                    },
                    "profile": {
                        "name":"SensorClusterSmartHouse2"
                    }
                }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
    print("Result for addNewDevice: %s - Message: %s" % (response, response.text))



if __name__ == "__main__":
    createValueDescriptors()
    uploadDeviceProfile()
    addNewDevice()
