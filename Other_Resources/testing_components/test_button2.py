import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)

print("Start")
while True:
    if GPIO.input(23) == GPIO.HIGH:
        print("button is pressed")
