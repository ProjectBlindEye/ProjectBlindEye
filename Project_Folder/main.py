import objectdetect
import strgen
import ocr
import tts
import camera
import os
import time
import threading
import RPi.GPIO as GPIO

OCR_TEXT = ""
OBJECT_TEXT = ""

def main():

    welcome_thread = threading.Thread(target=welcome)
    welcome_thread.start()
    init_gpio()
    welcome_thread.join()
    print("Ready!")

    start = time.time()
    current = time.time()

    while True:
        current = time.time()
        if GPIO.input(23) == GPIO.LOW and (current - start) > 0.5:
            start = current
            scan()

    GPIO.cleanup() # Clean up

def scan():

    print("Processing, Please Wait...")
    camera.take_picture()
    #---Getting Image
    image = objectdetect.get_image("pic.jpg")

    #---Scanning Image
    global OCR_TEXT, OBJECT_TEXT
    OCR_TEXT = ""
    OBJECT_TEXT = ""
    OCR = threading.Thread(target = ocr_thread, args=(image, ))
    OBJDET = threading.Thread(target = object_detect_thread, args=(image, ))
    OCR.name = "OCR"
    OBJDET.name = "OBJDET"

    OCR.start()
    OBJDET.start()

    while OCR_TEXT == "" and OBJECT_TEXT == "":
        continue

    os.remove("pic.jpg")
    read_text = OBJECT_TEXT + "The text in the image are as follows. " + OCR_TEXT + ". Press the button again to restart."

    #---Output
    tts.read(read_text)

def ocr_thread(image):
    global OCR_TEXT
    OCR_TEXT = ocr.get_text(image)


def object_detect_thread(image):
    global OBJECT_TEXT
    object_data = objectdetect.scan_image(image, "yololib")
    objects = object_data['objects']
    OBJECT_TEXT = strgen.generate_read_string(objects)

def welcome():
    tts.read("Welcome! Press the button to scan your document!")

def init_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)

if __name__ == "__main__":
    main()
