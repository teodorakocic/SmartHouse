import csv
from math import ceil
import requests
import json
import random
import time

logFilesWeek = list()
logFilesMonth = list()

dishwasherList = list()
microwaveList = list()
fridgeList = list()
washingMachineList = list()
tv_airConditionerList = list()
printer_scannerList = list()
furnaceList = list()
garageDoorList = list()
generatedEnergyList = list()

totalWeek = 0
totalMonth = 0

dishwasherWeek = 0
microwaveWeek = 0
fridgeWeek = 0
washingMachineWeek = 0
tvAirConditionerWeek = 0
printerScannerWeek = 0
furnaceWeek = 0
garageDoorWeek = 0
generatorWeek = 0

dishwasherMonth = 0
microwaveMonth = 0
fridgeMonth = 0
washingMachineMonth = 0
tvAirConditionerMonth = 0
printerScannerMonth = 0
furnaceMonth = 0
garageDoorMonth = 0
generatorMonth = 0


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

    
    logsData = {"weekLog": logFilesWeek, 
                "monthLog": logFilesMonth,
                "totalWeek": totalWeek,
                "totalMonth": totalMonth}

    with open("docker-compose\energy-consumption\logData.json", "w") as outfile:
        json.dump(logsData, outfile)

    print("Sending values for energy consumption in W for home devices: Dishwasher %s, Microwave %s, Fridge %s, Washing machine %s, TV and Air Conditioner %s, Printer and Scanner %s, Furnace %s, Garage door %s. Energy generated in total is %s W." % (device1, device2, device3, device4, device5, device6, device7, device8, generator))

    return (device1, device2, device3, device4, device5, device6, device7, device8, generator)


if __name__ == "__main__":
    
    sensorTypes = ["dishwasher", "microwave", "fridge", "washingmachine", "tvairconditioner", "printerscanner", "furnace", "garagedoor", "generator"]

    counter = 1
    dictionary = dict()

    while(1):

        (dishwasher, microwave, fridge, washingmachine, tvairconditioner, printerscanner, furnace, garagedoor, generator) = generateSensorData()

        dishwasherWeek += dishwasher
        microwaveWeek += microwave
        fridgeWeek += fridge
        washingMachineWeek += washingmachine
        tvAirConditionerWeek += tvairconditioner
        printerScannerWeek += printerscanner
        furnaceWeek += furnace
        garageDoorWeek += garagedoor
        generatorWeek += generator

        totalWeek += dishwasherWeek + microwaveWeek + fridgeWeek + washingMachineWeek + tvAirConditionerWeek + printerScannerWeek + furnaceWeek + garageDoorWeek

        dishwasherMonth += dishwasher
        microwaveMonth += microwave
        fridgeMonth += fridge
        washingMachineMonth += washingmachine
        tvAirConditionerMonth += tvairconditioner
        printerScannerMonth += printerscanner
        furnaceMonth += furnace
        garageDoorMonth += garagedoor
        generatorMonth += generator

        totalMonth += dishwasherMonth + microwaveMonth + fridgeMonth + washingMachineMonth + tvAirConditionerMonth + printerScannerMonth + furnaceMonth + garageDoorMonth

        counter += 1

        time.sleep(5)

        if counter % 7 == 0:
            dictionary = {
                "dishwasher": dishwasherWeek,
                "microwave": microwaveWeek,
                "fridge": fridgeWeek,
                "washing machine": washingMachineWeek,
                "tv and air conditioner": tvAirConditionerWeek,
                "printer and scanner": printerScannerWeek,
                "furnace": furnaceWeek,
                "garage door": garageDoorWeek,
                "generator": generatorWeek
            }

            dishwasherWeek = 0
            microwaveWeek = 0
            fridgeWeek = 0
            washingMachineWeek = 0
            tvAirConditionerWeek = 0
            printerScannerWeek = 0
            furnaceWeek = 0
            garageDoorWeek = 0
            generatorWeek = 0

            with open("docker-compose\energy-consumption\logData.json", mode='w') as file:
                logFilesWeek.append(dictionary)
                json.dump(logFilesWeek, file)

            with open("docker-compose\energy-consumption\logData.json", mode='w') as outfile:
                totalWeek = totalWeek
                json.dump(totalWeek, outfile)

            totalWeek = 0

        if counter % 30 == 0:
            dictionary = {
                "dishwasher": dishwasherMonth,
                "microwave": microwaveMonth,
                "fridge": fridgeMonth,
                "washing machine": washingMachineMonth,
                "tv and air conditioner": tvAirConditionerMonth,
                "printer and scanner": printerScannerMonth,
                "furnace": furnaceMonth,
                "garage door": garageDoorMonth,
                "generator": generatorMonth
            }

            dishwasherMonth = 0
            microwaveMonth = 0
            fridgeMonth = 0
            washingMachineMonth = 0
            tvAirConditionerMonth = 0
            printerScannerMonth = 0
            furnaceMonth = 0
            garageDoorMonth = 0
            generatorMonth = 0
            totalMonth = totalMonth

            with open("docker-compose\energy-consumption\logData.json", mode='w') as file:
                logFilesMonth.append(dictionary)
                json.dump(logFilesMonth, file)

            with open("docker-compose\energy-consumption\logData.json", mode='w') as outfile:
                totalMonth = totalMonth
                json.dump(totalMonth, outfile)

            totalMonth = 0

