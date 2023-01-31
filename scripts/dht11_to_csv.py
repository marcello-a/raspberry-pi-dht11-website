#!/usr/bin/python
# Copyright (c) 2020 Marcello Alte
# Author: Marcello Alte
############################################################
# Get data from raspberry pi and dht11
# save the data to a csv file
############################################################

import Adafruit_DHT

import datetime
import os.path

# import psutil
# If true: import psutil
raspberry_data = None

# Adds following value to dht 11 temperature value
temperature_correction = 1.0

# Make sure the directory exist
filename = "/var/www/html/dht11_sensor_data.csv"

data_to_send = []

print("Start reading DHT11")

# Time
data_to_send.append(str(datetime.datetime.now()))

# Raspberrys data
if raspberry_data:
        data_to_send.append(psutil.disk_usage("/").percent)
        data_to_send.append(psutil.cpu_percent(1))
        data_to_send.append(0)
        data_to_send.append(psutil.sensors_temperatures()["cpu-thermal"][0].current)
        data_to_send.append(psutil.virtual_memory().percent)
        print("Got your PI data")



# Humidity sensor : Options are DHT11,DHT22 or AM2302
sensor = Adafruit_DHT.DHT11
# connected to GPIO pin (4, 17).
pin = 4
# get data from sensor
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
if humidity is not None and temperature is not None:
        data_to_send.append(temperature + temperature_correction)
        data_to_send.append(humidity)
        print("dht11 measured temperature:")
        print(temperature)
        print("dht11 measured temperature (with correction):")
        print(temperature + temperature_correction)
        print("dht11 measured humidity:")
        print(humidity)

# convert array to string and split each entry with ","
data_to_send_string = ",".join(str(x) for x in data_to_send)
# print(data_to_send_string)

print("Write to file")

# check if file exists
if os.path.isfile(filename):
		    # open and write to csv file
		    with open(filename, "a") as csv_file:
				        csv_file.write(data_to_send_string + "\n")
else:
        # create header
        header = "date,dht11_temperature,dht11_humidity"
        if raspberry_data:
                header = "date,disk_usage,cpu,memory,cpu_temperature,dht11_temperature,dht11_humidity"
        # create file and add header additional to data
        with open(filename, "w") as csv_file:
                csv_file.write(header + "\n" + data_to_send_string + "\n")


print("Finished " + datetime.datetime.now().strftime('%Y_%m_%d %H:%M:%S'))