import pytesseract
from PIL import Image
from gtts import gTTS
import os


pytesseract.pytesseract.tesseract_cmd = input(
    r'Enter the path for pytesseract: ')

img = input(r"Enter the path for image: ")
target = Image.open(img)
text = pytesseract.image_to_string(target, config='')

with open("./Imagetospeech/text.txt", 'w') as f:
    f.write(text)

with open(r'./Imagetospeech/text.txt') as file:
    mytext = file.read().replace("\n", " ")
    language = 'en'
    output = gTTS(text=mytext, lang=language, slow=False)
    output.save('./Imagetospeech/imagetospeech.mp3')
os.system("start ./Imagetospeech/imagetospeech.mp3")

question = input("Do you want to delete the files (Y/N): ")
if question in ['Y', 'y']:
    os.remove('./Imagetospeech/text.txt')
    os.remove('./Imagetospeech/imagetospeech.mp3')

elif question in ['N', 'n']:
    print("Files saved")
