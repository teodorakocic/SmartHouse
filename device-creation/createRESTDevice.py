import requests, json, sys, re, time, os, warnings, argparse
from requests_toolbelt import MultipartEncoder
from datetime import datetime

warnings.filterwarnings("ignore")

# Gather information from arguments
parser=argparse.ArgumentParser(description="Python script for creating a new device from scratch in EdgeX Foundry")
parser.add_argument('-ip',help='EdgeX Foundry IP address', required=True)
parser.add_argument('-devip',help='Target device IP address', required=True)

args=vars(parser.parse_args())

edgex_ip    = args["ip"]
device_ip   = args["devip"]

def createAddressables():

    url = 'http://%s:48081/api/v1/addressable' % edgex_ip

    payload = {
        "name":"SmartHouseProject2",
        "protocol":"HTTP",
        "address":device_ip,
        "port":5000,
        "path":"/register"
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
    print("Result for createAddressables: %s - Message: %s" % (response, response.text))


def createValueDescriptors():
    url = 'http://%s:48080/api/v1/valuedescriptor' % edgex_ip

    payload =   {
                    "name":"energy",
                    "description":"Consumed Energy to be shown in test app web UI",
                    "type":"Str",
                    "uomLabel":"energy",
                    "defaultValue":"",
                    "formatting":"%s",
                    "labels":["energy","smarthouseproject2"]
                }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
    print("Result for createValueDescriptors #1: %s - Message: %s" % (response, response.text))


def uploadDeviceProfile():
    multipart_data = MultipartEncoder(
        fields={
                'file': ('RESTDeviceProfile.yaml', open('RESTDeviceProfile.yaml', 'rb'), 'text/plain')
               }
        )

    url = 'http://%s:48081/api/v1/deviceprofile/uploadfile' % edgex_ip
    response = requests.post(url, data=multipart_data,
                      headers={'Content-Type': multipart_data.content_type})

    print("Result of uploading device profile: %s with message %s" % (response, response.text))



def createDeviceService():
    url = 'http://%s:48081/api/v1/deviceservice' % edgex_ip

    payload = {
        "name":"rest-device-service",
        "description":"Gateway for control in energy consumption in a smart house",
        "labels":["energy","smarthouseproject2"],
        "adminState":"unlocked",
        "operatingState":"enabled",
        "addressable": {
            "name":"SmartHouseProject2"
        }
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
    print("Result for createDeviceService: %s - Message: %s" % (response, response.text))



def addNewDevice():
    url = 'http://%s:48081/api/v1/device' % edgex_ip

    payload = {
        "name": "SmartHouseProject2",
        "description": "Project for IoTs course",
        "adminState": "unlocked",
        "operatingState": "enabled",
        "protocols": {
            "example": {
            "host": "localhost",
            "port": "0",
            "unitID": "1"
            }
        },
        "addressable": {
            "name": "SmartHouseProject2"
        },
        "labels": [
            "energy",
            "smarthouseproject2"
        ],
        "location": "nis",
        "service": {
            "name": "rest-device-service" 
        },
        "profile": {
            "name": "energyConsumption"
        }
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
    print("Result for addNewDevice: %s - Message: %s" % (response, response.text))


if __name__ == "__main__":
    createAddressables()
    createValueDescriptors()
    uploadDeviceProfile()
    createDeviceService()
    addNewDevice()
