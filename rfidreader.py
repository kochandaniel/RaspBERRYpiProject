#Project DANK
#!/usr/bin/env python

import greengrasssdk
import logging
import platform
import RPi.GPIO as GPIO
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

def reader():
    reader = SimpleMFRC522()
    print("Hold a tag near the reader")

    try:
        id, text = reader.read()
        print(id)
        send_iot_payload("id")
        print(text)
        send_iot_payload("text")

    finally:
        GPIO.cleanup()

def send_iot_payload(payload):
    try:
        client.publish(
                topic='pi/id',
                queueFullPolicy='AllOrException',
                payload=payload)
    except Exception as e:
        logger.error('Failed to publish message: ' + repr(e))


def greengrass_hello_world_run():
    reader()
   # Asynchronously schedule this function to be run again in 5 seconds
    Timer(5, greengrass_hello_world_run).start()



# Start executing the function above
greengrass_hello_world_run()


# This is a dummy handler and will not be invoked
# Instead the code above will be executed in an infinite loop for our example
def function_handler(event, context):
    return
