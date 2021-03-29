import time
from picamera import PiCamera

camera = PiCamera()
time.sleep(2)
camera.resolution = (1024, 768)
camera.capture("pic.jpg")
print("Image saved in pic.jpg")
print("Test Completed")
