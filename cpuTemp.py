#!/usr/bin/env python3
import paho.mqtt.publish as publish
import os
import time

# Return CPU temperature as a character string
def measure_temp():
	res = os.popen('vcgencmd measure_temp').readline()
	return(res.replace("temp=","").replace("'C\n",""))

def publish_message(topic, message):
	print("Publishing to MQTT topic: " + topic)
	print("Message: " + message)

	publish.single(topic, message, hostname="192.168.2.101")

temp = measure_temp()
publish_message("/pi/temp/", temp)

