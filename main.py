import ObjectDetection as oDetect
import StringGenerator as strGen
import SpeakOut

def main():
    image = oDetect.get_image("images/dining_table.jpg")
    objects = oDetect.scan_image(image, "yololib", True)
    readString = strGen.generate_read_string(objects)
    print(readString)
    SpeakOut.speak_text(readString)

if __name__ == "__main__": main()
