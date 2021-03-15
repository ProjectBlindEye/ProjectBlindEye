import time
from picamera import PiCamera

def take_picture():

    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    time.sleep(2) # Camera warm-up time

    capture_time = int(time.time()) # used for naming file
    filename = "images/" + str(capture_time) + ".jpg"
    camera.capture(filename)
    print("File name:", filename)

    return filename # returns "images/<number>.jpg"
