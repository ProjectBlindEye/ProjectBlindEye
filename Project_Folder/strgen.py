import cmudict

def use_an(word, pronunciations=cmudict.dict()):
    for syllables in pronunciations.get(word, []):
        return syllables[0][-1].isdigit()

def generate_read_string(objects):
    returnString = "The image contains "
    for object, number in objects.items():
        if number > 1:
            lastChar = object[-1]
            addedString = str(number) + " " + object
            if lastChar == 's':
                addedString += "es"
            else:
                addedString += "s"
            index = list(objects.keys()).index(object)
        else:
            if use_an(object):
                addedString = "an " + object
            else:
                addedString = "a " + object
        index = list(objects.keys()).index(object) + 1
        if index != len(objects):
            #  Not Last Item
            if index == (len(objects) - 1):
                addedString += ", and "
            else:
                addedString += ", "
        returnString += addedString

    returnString += ". "
    return returnString
