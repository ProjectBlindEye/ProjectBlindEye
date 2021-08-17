import time
from picamera import PiCamera
CAMERA = PiCamera()

def take_picture():
    #Takes Picture and saves to path pic.jpg
    time.sleep(2)
    CAMERA.resolution = (1024, 768)
    CAMERA.capture("pic.jpg")
