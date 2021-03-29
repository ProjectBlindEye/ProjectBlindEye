import objectdetect
import strgen
import ocr
import tts
import os
import camera
import RPi.GPIO as GPIO

def main():

    init_gpio()
    running = False

    print("Welcome to Project Blind Eye!")
    while not running:

        if GPIO.input(23) == GPIO.HIGH:
            running = True

            camera.take_picture()
            #---Getting Image
            image = objectdetect.get_image("images/pic.jpg")

            #---Scanning Image
            ocr_text = ocr.get_text(image)
            object_data = objectdetect.scan_image(image, "yololib")

            #---Processing Data
            #processed_image = objectData['processed_image']
            objects = object_data['objects']
            object_text = strgen.generate_read_string(objects)
            os.remove("images/pic.jpg")
            read_text = object_text + "The text in the image are as follows. " + ocr_text

            #---Ouput
            print(read_text)
            tts.text_to_speech(read_text)

            running = False

def init_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

if __name__ == "__main__": main()
