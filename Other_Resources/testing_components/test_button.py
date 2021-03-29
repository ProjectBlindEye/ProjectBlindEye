import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

print("Press the button")

running = True
while (running):
    if GPIO.input(23) == GPIO.HIGH:
        print("Button has been pressed")
        running = False
print("Test Completed")
