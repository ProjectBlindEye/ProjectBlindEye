import pytesseract
import cv2

#Preprocessing of Image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Main Get Text Function
def get_text(image):
    image = get_grayscale(image)
    text = pytesseract.image_to_string(image)

    return text
