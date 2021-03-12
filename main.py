import objectdetect
import strgen
import ocr
import tts
import os
import RPi.GPIO as GPIO

def main():

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    running = False

    while not running:
        if GPIO.input(15) == GPIO.HIGH:
            running = True
            path = "images/TextAndObjects.png"

            if not (file_exists(path)):
                print(">>>File Does not Exist...")
            else:

                #Scanning Image
                image = objectdetect.get_image(path)
                ocrText = ocr.get_text(image)
                objectData = objectdetect.scan_image(image, "yololib")
                processedImage = objectData['processed_image']
                objects = objectData['objects']
                objectText = strgen.generate_read_string(objects)

                #Speaking Out Data
                tts.speak_text("PRINTING TEXT IN IMAGE...")
                tts.speak_text(ocrText)

                tts.speak_text("PRINTING OBJECTS IN IMAGE...")
                tts.speak_text(objectText)

                objectdetect.show_image(processedImage)

            running = False

def file_exists(file):
    if os.path.exists(file):
        return True
    else:
        return False

if __name__ == "__main__": main()
