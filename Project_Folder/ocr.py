import pytesseract

#Main Get Text Function
def get_text(image):
    text = pytesseract.image_to_string(image)
    return text
