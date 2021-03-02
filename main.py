import ObjectDetection
import StringGenerator

def main():
    objects = ObjectDetection.scan_image('images/dining_table.jpg', 'yololib', True)
    readString = StringGenerator.generate_read_string(objects)
    print(readString)

if __name__ == "__main__": main()
