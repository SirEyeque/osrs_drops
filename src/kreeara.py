import os
import time
import random

from getch import getch

def simulateK(value):
    bcpVal = value & 1
    btVal = value & 2
    bbVal = value & 4
    bhVal = value & 8
    petVal = value & 16

    bcp = 0
    bt = 0
    bb = 0
    bh = 0
    pet = 0

    count = 0

    obtained = 0    

    while obtained != value:
        time.sleep(0.001)
        count += 1
        roll = random.randint(0, 1523)

        if roll == 1199 or roll == 310 or roll == 4:
            bh += 1
            print("Armadyl Hilt!! KC: ", count)
        if roll == 1234 or roll == 123 or roll == 12 or roll == 91:
            bcp += 1
            print("Armadyl chestplate!! KC: ", count)
        if roll == 532 or roll == 510 or roll == 199 or roll == 9:
            bt += 1
            print("Armadyl chainskirt!! KC: ", count)
        if roll == 918 or roll == 723 or roll == 322 or roll == 491:
            bb += 1
            print("Armadyl helmet! KC: ", count)

        roll = random.randint(0, 4999)

        if roll == 3916:
            print("You have a funny feeling like you're being followed. KC: ", count)
            pet += 1



        if bcpVal > 0 and bcp > 0:
            obtained |= 1

        if btVal > 0 and bt > 0:
            obtained |= 2

        if bbVal > 0 and bb > 0:
            obtained |= 4

        if bhVal > 0 and bh > 0:
            obtained |= 8

        if petVal > 0 and pet > 0:
            obtained |= 16


    print("Final Stats\n________________________")
    print("KC: ", count)
    print("Armadyl chestplate: ", bcp)
    print("Armadyl tassets: ", bt)
    print("Armadyl helmets: ", bb)
    print("Armadyl hilts: ", bh)
    print("Pet Kree\'arra: ", pet)

def printIt(val, cursorPos):
    os.system("clear")
    print("Welcome to the Kree'arra simulator")
    print("Please use the arrow keys and the space bar to make your selections below\n\n")
    val1 = val & 1
    val2 = val & 2
    val3 = val & 4
    val4 = val & 8
    val5 = val & 16
    if val1: 
        print(f"[X]\tArmadyl chestplate")
    else:
        print(f"[ ]\tArmadyl chestplate")

    if val2: 
        print(f"[X]\tArmadyl chainskirt")
    else:
        print(f"[ ]\tArmadyl chainskirt")

    if val3: 
        print(f"[X]\tArmadyl helmet")
    else:
        print(f"[ ]\tArmadyl helmet")

    if val4: 
        print(f"[X]\tArmadyl hilt")
    else:
        print(f"[ ]\tArmadyl hilt")

    if val5:
        print(f"[X]\tPet Kree\'arra")
    else:
        print(f"[ ]\tPet Kree\'arra")
        

    print("\n\nEnter")
    match cursorPos:
        case 0:
            print("\033[4;2H")
        case 1:
            print("\033[5H")
        case 2:
            print("\033[6H")
        case 3:
            print("\033[7H")
        case 4:
            print("\033[8H")
        case 5:
            print("\033[11H")


def runK():

    enter = False

    cursorPos = 0

    selected = 0

    printIt(selected, cursorPos)
    while not enter:
        var = getch()

        if var == " ":
            if cursorPos == 5:
                print("\033[2B")
                break 

            if (selected & 2**cursorPos) != 0:
                selected -= 2**cursorPos
            else:
                selected += 2**cursorPos

        if var == "B":
            if cursorPos < 5:
                cursorPos += 1
        if var == "A":
            if cursorPos > 0:
                cursorPos -= 1
        printIt(selected, cursorPos)

    simulateK(selected)

    print("\n\nWould you like to return to the simulator?")
    print("Press \'e\' to exit")
    print("Press any other key to continue...")

    var = getch()

    if var == 'e':
        return 1
    return 0


