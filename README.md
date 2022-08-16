# Smart House

An IoT system based on a microservice platform and functions as a service for consumption control of electric energy in a smart house.

<img style="margin: 10px" src="https://raw.githubusercontent.com/teodorakocic/SmartHouse/main/documentation/images/readme.JPG" />


## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on deploying the project on a live system.

### Prerequisites

Requirements for the software and other tools to build, test and push 
- [https://www.docker.com]

### Installing

A step by step series of examples that tell you how to get a development
environment running

1. Position yourself from console into the directory docker-compose
	
	cd docker-compose

2. From file docker-compose run the following command

    docker-compose -p smarthouse up -d
	
3. Now position yourself in the directory device-creation

	cd ../device-creation

4. From file device-creation run next commands

    python createSensorCluster.py -ip 127.0.0.1
	python createRESTDevice.py -ip 127.0.0.1 -devip energy-consumption-edgex
	
5. Position yourself from console into the directory sensor-data-gen

	cd ../sensor-data-gen

6. Then run two python files

	python genSensorData.py
	python trackLogs.py
	
7. Set a few kuiper rules by following the steps described in the section documentation/kuiper-rules (listed rules are supported in older versions of EdgeX and eKuiper)

	Printer and Scanner rule
	Fridge rule
	Furnace rule
	Garage door rule
	
8. If You need to change the parameters for openwhisk actions check the section documentation/openwhisk-setup

9. For visualization part follow next steps

	Go to URL http://localhost:3000 and log as admin with password admin
	Configuration > Data Sources > Add new data source > InfluxDB
	Set: URL on http://influxdb-edgex:8086, Database on sensordata, User and Password are both admin
	Dashboards > New dashboard > Add a new panel
	In the section select measurement choose sensor_cluster_smart_house_v2
	

## Authors

  - **Teodora Kocic**

## Acknowledgments

  - https://github.com/osipov/openwhisk-python-twilio.git
  - https://ekuiper.org/docs/en/latest/operation/manager-ui/overview.html#getting-started
  - https://docs.edgexfoundry.org/2.2/examples/Ch-CommandingDeviceThroughRulesEngine/