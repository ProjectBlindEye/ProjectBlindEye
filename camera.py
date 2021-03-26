import time
from picamera import PiCamera

def take_picture():
    #Takes Picture and saves to path images/pic.jpg
    camera = PiCamera()
    time.sleep(2)
    camera.resolution = (1024, 768) #MIGHT BE CHANGED
    camera.capture("images/pic.jpg")
