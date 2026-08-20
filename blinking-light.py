import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module

GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial value to low (off)
count = 0

while count < 20: # Run forever
    GPIO.output(8, GPIO.HIGH) # Turn on
    print("turned on")
    sleep(1)                  # Sleep for 1 second (1)
    GPIO.output(8, GPIO.LOW)  # Turn off
    print("turned off")
    sleep(1)                  # Sleep for 1 second (2)
    count += 1

