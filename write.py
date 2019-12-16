# School project Dank

#!/usr/bin/env python

import greengrasssdk
import RPi.GPIO as GPIO
import logging
import platform
import sys
from threading import Timer
import signal

# Setup logging to stdout
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Creating a greengrass core sdk client
client = greengrasssdk.client('iot-data')

# Retrieving platform information to send from Greengrass Core
my_platform = platform.platform()

continue_reading = True

sys.path.append('/home/pi/MFRC522-python')
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    while True:
        text = raw_input('Your Name: ')
        print("Now place tag next to the scanner to write")
        id, text = reader.write(text)
        print("recorded")
        print(id)
        print(text)
        break

finally:
    GPIO.cleanup()

def greengrass_hello_world_run():
    read()
   # Asynchronously schedule this function to be run again in 5 seconds
    Timer(5, greengrass_hello_world_run).start()



# Start executing the function above
greengrass_hello_world_run()


# This is a dummy handler and will not be invoked
# Instead the code above will be executed in an infinite loop for our example
def function_handler(event, context):
    return
