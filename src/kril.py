import os
import time
import random

from getch import getch

def simulateKT(value):
    spVal = value & 1
    sdVal = value & 2
    zhVal = value & 4
    petVal = value & 8 

    sp = 0
    sd = 0
    zh = 0
    pet = 0

    count = 0

    obtained = 0    

    while obtained != value:
        time.sleep(0.001)
        count += 1
        roll = random.randint(0, 1523)

        if roll == 1199 or roll == 310 or roll == 4:
            zh += 1
            print("Zamorak Hilt!! KC: ", count)
        if roll == 195 or roll == 629 or roll == 1520:
            sd += 1
            print("Staff of the dead!! KC: ", count)

        if roll == 1234 or roll == 123 or roll == 12 or roll == 91:
            sp += 1
            print("Zammy spear! KC: ", count)
        if roll == 532 or roll == 510 or roll == 199 or roll == 9:
            sp += 1
            print("Zammy spear! KC: ", count)
        if roll == 918 or roll == 723 or roll == 322 or roll == 491:
            sp += 1
            print("Zammy spear! KC: ", count)

        roll = random.randint(0, 4999)

        if roll == 3916:
            print("You have a funny feeling like you're being followed. KC: ", count)
            pet += 1



        if spVal > 0 and sp > 0:
            obtained |= 1

        if sdVal > 0 and sd > 0:
            obtained |= 2

        if zhVal > 0 and zh > 0:
            obtained |= 4

        if petVal > 0 and pet > 0:
            obtained |= 8


    print("Final Stats\n________________________")
    print("KC: ", count)
    print("Zamorakian spear: ", sp)
    print("Staff of the dead: ", sd)
    print("Zamorak hilt: ", zh)
    print("Pet k\'ril tsutsaroth: ", pet)

def printIt(val, cursorPos):
    os.system("clear")
    print("Welcome to the K'ril Tsutsaroth simulator")
    print("Please use the arrow keys and the space bar to make your selections below\n\n")
    val1 = val & 1
    val2 = val & 2
    val3 = val & 4
    val4 = val & 8
    if val1: 
        print(f"[X]\tZamorkian Spear")
    else:
        print(f"[ ]\tZamorkian Spear")

    if val2: 
        print(f"[X]\tStaff of the dead")
    else:
        print(f"[ ]\tStaff of the dead")

    if val3: 
        print(f"[X]\tZamorak Hilt")
    else:
        print(f"[ ]\tZamorak Hilt")

    if val4:
        print(f"[X]\tPet K\'ril Tsutsaroth")
    else:
        print(f"[ ]\tPet K\'ril Tsutsaroth")
        

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
            print("\033[10H")


def runKT():

    enter = False

    cursorPos = 0

    selected = 0

    printIt(selected, cursorPos)
    while not enter:
        var = getch()

        if var == " ":
            if cursorPos == 4:
                print("\033[2B")
                break 

            if (selected & 2**cursorPos) != 0:
                selected -= 2**cursorPos
            else:
                selected += 2**cursorPos

        if var == "B":
            if cursorPos < 4:
                cursorPos += 1
        if var == "A":
            if cursorPos > 0:
                cursorPos -= 1
        printIt(selected, cursorPos)

    simulateKT(selected)

    print("\n\nWould you like to return to the simulator?")
    print("Press \'e\' to exit")
    print("Press any other key to continue...")

    var = getch()

    if var == 'e':
        return 1
    return 0


