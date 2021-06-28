import pytesseract as pyt
from PIL import ImageGrab
from pynput.keyboard import Controller
import time

pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
kb = Controller()
generated_name_matches_desired = False

print("Enter desired names. Put * if unnecessary.")
desired_name1 = input("Enter desired FIRST NAME: ")
desired_name2 = input("Enter desired SECOND NAME: ")
desired_name3 = input("Enter desired THIRD NAME: ")

x1, y1, x2, y2 = 267, 418, 495, 458


def determine_name():
    name_image = ImageGrab.grab(bbox=(x1, y1, x2, y2)).convert("LA")
    # name_image.show()

    generated_name = pyt.image_to_string(name_image, lang='eng', config="-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\ ")
    names_list = generated_name.split(" ")

    if len(names_list[0]) < 2:
        try:
            name1 = names_list[1]
            name2 = names_list[2]
            name3 = names_list[3][:-2]
        except IndexError:
            print("Could not recognize name. Skipping...")
    else:
        try:
            name1 = names_list[0]
            name2 = names_list[1]
            name3 = names_list[2][:-2]
        except IndexError:
            print("Could not recognize name. Skipping...")
            name3 = "ERROR"

    if name3.endswith("\n"):
        name3 = name3[:-1]

    print(name1, name2, name3)

    if desired_name1 == "*" or desired_name1 == name1:
        first_name_matches = True
    else:
        first_name_matches = False

    if desired_name2 == "*" or desired_name2 == name2:
        second_name_matches = True
    else:
        second_name_matches = False


    if desired_name3 == "*" or desired_name3 == name3:
        third_name_matches = True
    else:
        third_name_matches = False

    if first_name_matches and second_name_matches and third_name_matches:
        global generated_name_matches_desired
        generated_name_matches_desired = True

    time.sleep(3)


print("Executing in 5 seconds. Focus on Fall Guys window.")
time.sleep(5)

while not generated_name_matches_desired:
    kb.press("p")
    kb.release("p")
    determine_name()
