#!/usr/bin/env python

'''
' Author(s): Mathew Norman
' Date created: 10/04/18
' Description: 
'  Simulates the process of reading and validating RFID cards on the Raspberry Pi for the RFID Readers.
'''

# Import libraries.
import requests
import uuid
import os
from gpiozero import Buzzer # Import library for buzzer.
from time import sleep # Import library for sleep.
import RPi.GPIO as GPIO # Import library for GPIO pins.

# Import local libraries.
from lib import SimpleMFRC522 # Import library for MFRC522.
from lib import RFIDStatus # Import custom library for RFID status.
from lib import Validate # Import custom library for user validation library.

reader = SimpleMFRC522.SimpleMFRC522()
status = RFIDStatus.RFIDStatus()
validate = Validate.Validate()

def accessGranted():
	status.green_on()
	status.quick_buzz()
	sleep(10)
	status.green_off()
	
	
def accessDenied():
	status.red_on()
	status.quick_buzz()
	status.quick_buzz()
	status.quick_buzz()
	sleep(10)
	status.red_off()
	
# Read card reader input
def readingCards(signature):
	while True:
		print("Ready to read...")
		status.blue_on()
		id, time = reader.read()
		status.blue_off()
		if (validate.card(id, signature)):
			#accessGranted()
			print "Granted"
		else:
			print "Not granted"

# Load or create signature
if os.path.isfile('signature'):
	f = open("signature", "r")
	signature = f.read()
	f.close()
	readingCards(signature)
else:
	writesignature = str(uuid.uuid4())
	print(writesignature)
	f = open("signature","w")
	f.write(writesignature)
	f.close()
	f = open("signature", "r")
	signature = f.read()
	f.close()
	readingCards(signature)
	