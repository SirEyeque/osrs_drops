import os
import time
import random

from getch import getch

def simulateZ(value):
    ssVal = value & 1
    slVal = value & 2
    acVal = value & 4
    shVal = value & 8
    petVal = value & 16

    ss = 0
    sl = 0
    ac = 0
    sh = 0
    pet = 0

    count = 0

    obtained = 0    

    while obtained != value:
        time.sleep(0.001)
        count += 1
        roll = random.randint(0, 1523)

        if roll == 1199 or roll == 310 or roll == 4:
            sh += 1
            print("Saradomin Hilt!! KC: ", count)
        if roll == 1422 or roll == 37 or roll == 348:
            ac += 1
            print("Armadyl crossbow!! KC: ", count)
        if roll == 1234 or roll == 123 or roll == 12 or roll == 91:
            ss += 1
            print("Saradomin Sword!! KC: ", count)
        if roll == 532 or roll == 510 or roll == 199 or roll == 9:
            ss += 1
            print("Saradomin Sword!! KC: ", count)
        if roll == 918 or roll == 723 or roll == 322 or roll == 491:
            ss += 1
            print("Saradomin Sword!! KC: ", count)
        if roll == 799 or roll == 301 or roll == 1511 or roll == 1 or roll == 81 or roll == 543:
            sl += 1
            print("Saradomin's Light!! KC: ", count)

        roll = random.randint(0, 4999)

        if roll == 3916:
            print("You have a funny feeling like you're being followed. KC: ", count)
            pet += 1



        if ssVal > 0 and ss > 0:
            obtained |= 1

        if slVal > 0 and sl > 0:
            obtained |= 2

        if acVal > 0 and ac > 0:
            obtained |= 4

        if shVal > 0 and sh > 0:
            obtained |= 8

        if petVal > 0 and pet > 0:
            obtained |= 16


    print("Final Stats\n________________________")
    print("KC: ", count)
    print("Saradomin Sword: ", ss)
    print("Saradomin Light: ", sl)
    print("Armadyl crossbow: ", ac)
    print("Saradomin Hilt: ", sh)
    print("Pet Zilyana: ", pet)

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
        print(f"[X]\tSaradomin Sword")
    else:
        print(f"[ ]\tSaradomin Sword")

    if val2: 
        print(f"[X]\tSaradomin Light")
    else:
        print(f"[ ]\tSaradomin Light")

    if val3: 
        print(f"[X]\tArmadyl Crossbow")
    else:
        print(f"[ ]\tArmadyl Crossbow")

    if val4: 
        print(f"[X]\tSaradomin hilt")
    else:
        print(f"[ ]\tSaradomin hilt")

    if val5:
        print(f"[X]\tPet zilyana")
    else:
        print(f"[ ]\tPet zilyana")
        

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


def runZ():

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

    simulateZ(selected)

    print("\n\nWould you like to return to the simulator?")
    print("Press \'e\' to exit")
    print("Press any other key to continue...")

    var = getch()

    if var == 'e':
        return 1
    return 0


