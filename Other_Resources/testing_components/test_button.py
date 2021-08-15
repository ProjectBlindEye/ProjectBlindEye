import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

def button_pressed():
    print("Button Pressed!")

def main():
    #Setup
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off

    print("Welcome to Button Test!")

    start = time.time()
    current = time.time()

    while True:
        current = time.time()
        if GPIO.input(23) == GPIO.LOW and (current - start) > 0.5:
            start = current
            button_pressed()

    GPIO.cleanup() # Clean up

main()
