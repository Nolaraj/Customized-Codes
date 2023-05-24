#
from itertools import permutations

import pyautogui
from time import sleep
import os

dataset = [
# "above",                 #5
"harsh",
"obvious",
# "kind",                 #9
# "rabbit",                 #1
# "obey",                 #2
# "edge",                 #12
"sadness",
# "hammer",               #4
# "nation",
"ramp"]
# "panda"]                #7

def image_checkpoint_return_location(image, confidence = 0.5):
    try:
        location = pyautogui.locateOnScreen(image, confidence=confidence) #For Confidence to be used in Code pip install opencv-python is needed
        if location is not None:
            return (location)
        else:
            print(f'{image} position is None during runtime')
            #Active value not set as per required by code error
            if image == "longitudinal_reinforcing.png":
                print(f'Set {image} as active before running the code')
            return (location)
    except:
        print(f'{image} is not available in the screen during runtime')

def click_topleft_one_third(box):
    x = int(box[0]) + int(box[2])*1/6
    y = int(box[1]) + int(box[3])*1/10
    pyautogui.click(x,y)
def hold_on(icon):           # If item is present then Code HOLDS
    presence = pyautogui.locateOnScreen(icon)
    while presence != "None":
        sleep(1)
        presence = pyautogui.locateOnScreen(icon)
        if presence == None:
            sleep(1)
            break

def try_clicking(image_one, confidence = 0.9):
    try:
        sleep(2)
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(image_one,confidence)))

    except:
        try:
            pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(image_one, confidence)))


        except:
            print("Image not found", image_one)
os.chdir(os.path.join(os.getcwd(),"External Files", "Safe Pal"))

# generate all permutations of the list
permutations_list = list(permutations(dataset))

print("Sleeping for 3 seconds until the desired window is opened")
sleep(3)
# print the permutations
keys_done = -1
list2 = [6,27,28,40,57,63,71,85,100]
list2 = [x - 2 for x in list2]
# list2 = [4, 26, 83, 98]
for index, perm in enumerate(permutations_list):
    list1 = []
    for item in perm:
        list1.append(item)
    list1.insert(0, "rabbit")
    list1.insert(1, "obey")
    list1.insert(3, "hammer")
    list1.insert(4, "above")
    list1.insert(5, "nation")
    list1.insert(6, "panda")
    list1.insert(8, "kind")
    list1.insert(11, "edge")

    print(list1)

    print(index)

    if index in list2:
        # print("Inside", index)
        text = ''
        for items in list1:
            text = text +" " + str(items)
    #     print(index, text)
    if (permutations_list.index((perm)) > keys_done) :
        try_clicking("phrase.png")
        try_clicking("next.png")
        try_clicking("one.png")
        print(index)
        for items in list1:
            items = str(items)
            pyautogui.write(items)
            pyautogui.hotkey('tab')
        try_clicking("next.png")
        if image_checkpoint_return_location("invalid.png") is None:
            print(permutations_list.index(perm), list1, "Break Point")
            try_clicking("entry.png")
            sleep(1)
            pyautogui.write(list1[0])
            sleep(1)
            try_clicking("confirm.png")
            try_clicking("confirm_1.png")
            sleep(10)
            hold_on("undefined.png")
            if image_checkpoint_return_location("balance_0.png", 0.95) is not None:
                print(permutations_list.index(perm), list1, "Break Point iNSIDER vALUE  ")
                sleep(15)
                try_clicking("triple_dot.png")
                sleep(1)
                try_clicking("add_wallet.png")
                sleep(1)
                try_clicking("import_wallet.png")
            else:
                print(permutations_list.index(perm), list1, "Break Point Balance doesnot = 0")
                break
        else:
            try_clicking("back.png")