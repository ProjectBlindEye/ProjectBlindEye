import time
from picamera import PiCamera
import cv2
import os
CAMERA = PiCamera()

def take_picture():
    #Takes Picture and saves to path pic.jpg
    time.sleep(2)
    CAMERA.resolution = (1024, 768)
    CAMERA.capture("pic.jpg")
    img = cv2.imread("pic.jpg")
    flipped_img = cv2.rotate(img, cv2.ROTATE_180)
    cropped_img = flipped_img[0:0+768, 231:231+591]
    cv2.imwrite("pic.jpg", cropped_img)
