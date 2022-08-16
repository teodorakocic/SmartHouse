import csv
from math import ceil
import requests
import json
import random
import time


edgexip = '127.0.0.1'

dishwasherList = list()
microwaveList = list()
fridgeList = list()
washingMachineList = list()
tv_airConditionerList = list()
printer_scannerList = list()
furnaceList = list()
garageDoorList = list()
generatedEnergyList = list()

with open("sensor-data-gen\HomeC.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        dishwasherList.append(row['Dishwasher'])
        microwaveList.append(row['Microwave'])
        fridgeList.append(row['Fridge'])
        washingMachineList.append(row['Barn'])
        tv_airConditionerList.append(row['Living room'])
        printer_scannerList.append(row['Home office'])
        furnaceList.append(row['Furnace 1'])
        garageDoorList.append(row['Garage door'])
        generatedEnergyList.append(row['gen'])

def generateSensorData():

    i = random.randint(1, 503910)
    
    device1 = int(ceil(float(dishwasherList[i]) * 1000))
    device2 = int(ceil(float(microwaveList[i]) * 1000))
    device3 = int(ceil(float(fridgeList[i]) * 1000))
    device4 = int(ceil(float(washingMachineList[i]) * 1000))
    device5 = int(ceil(float(tv_airConditionerList[i]) * 1000))
    device6 = int(ceil(float(printer_scannerList[i]) * 1000))
    device7 = int(ceil(float(furnaceList[i]) * 1000))
    device8 = int(ceil(float(garageDoorList[i]) * 1000))

    generator = int(ceil(float(generatedEnergyList[i]) * 1000))

    print("Sending values for energy consumption in W for home devices: Dishwasher %s, Microwave %s, Fridge %s, Washing machine %s, TV and Air Conditioner %s, Printer and Scanner %s, Furnace %s, Garage door %s. Energy generated in total is %s W." % (device1, device2, device3, device4, device5, device6, device7, device8, generator))

    return (device1, device2, device3, device4, device5, device6, device7, device8, generator)
            

if __name__ == "__main__":

    sensorTypes = ["dishwasher", "microwave", "fridge", "washingmachine", "tvairconditioner", "printerscanner", "furnace", "garagedoor", "generator"]

    while(1):

        (dishwasher, microwave, fridge, washingmachine, tvairconditioner, printerscanner, furnace, garagedoor, generator) = generateSensorData()

        url = 'http://%s:49986/api/v1/resource/Sensor_cluster_smart_house_v2/dishwasher' % edgexip
        payload = dishwasher
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)

        url = 'http://%s:49986/api/v1/resource/Sensor_cluster_smart_house_v2/microwave' % edgexip
        payload = microwave
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)

        url = 'http://%s:49986/api/v1/resource/Sensor_cluster_smart_house_v2/fridge' % edgexip
        payload = fridge
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)

        url = 'http://%s:49986/api/v1/resource/Sensor_cluster_smart_house_v2/washingmachine' % edgexip
        payload = washingmachine
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)

        url = 'http://%s:49986/api/v1/resource/Sensor_cluster_smart_house_v2/tvairconditioner' % edgexip
        payload = tvairconditioner
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)

        url = 'http://%s:49986/api/v1/resource/Sensor_cluster_smart_house_v2/printerscanner' % edgexip
        payload = printerscanner
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)

        url = 'http://%s:49986/api/v1/resource/Sensor_cluster_smart_house_v2/furnace' % edgexip
        payload = furnace
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)

        url = 'http://%s:49986/api/v1/resource/Sensor_cluster_smart_house_v2/garagedoor' % edgexip
        payload = garagedoor
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)

        url = 'http://%s:49986/api/v1/resource/Sensor_cluster_smart_house_v2/generator' % edgexip
        payload = generator
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
        
        time.sleep(5)