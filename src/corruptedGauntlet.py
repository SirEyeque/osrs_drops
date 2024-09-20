import os
import random

import time

from getch import getch

def simulateCG(value):
    Ecws = value & 1
    full = value & 2
    noHelm = value & 4
    llef = value & 8

    shard = 0
    weaponSeed = 0
    armourSeed = 0
    enhanced = 0
    pet = 0

    obtained = 0

    count = 0

    while obtained != value:
        time.sleep(0.01)
        count += 1

        shard += random.randint(0,5) + 7

        roll1 = random.randint(0,799)
        
        if roll1 > 102 and roll1 < 119:
            weaponSeed += 1

        roll2 = random.randint(0,799)

        if roll2 > 315 and roll2 < 332:
            armourSeed += 1
            print("Amour seed %d on KC %d" % (armourSeed, count))

        roll3 = random.randint(0,799)

        if roll3 == 295 or roll3 == 712:
            enhanced += 1
            print("ENHANCED SEED!!! Obtained at %d KC" % count)

        roll4 = random.randint(0,799)
        if roll4 == 742:
            pet += 1
            print("You have a funny feeling like you're being followed. KC: %d" % count)

        if Ecws > 0 and enhanced > 0:
            obtained |= 1

        if full > 0 and armourSeed >= 6:
            obtained |= 2

        if noHelm > 0 and armourSeed >= 5:
            obtained |= 4

        if llef > 0 and pet > 0:
            obtained |= 8

    print("\n\nFinal Stats\n_______________________________")
    print("KC: ", count)
    print("Crystal shards: ", shard)
    print("Crystal weapon seeds: ", weaponSeed)
    print("Crystal armour seeds: ", armourSeed)
    print("Enhanced crystal armour seeds: ", enhanced)
    print("Youngllef: ", pet)

def printIt(val, cursorPos):
    os.system("clear")
    print("Welcome to the corrupted Gauntlet simulator")
    print("Please use the arrow keys and the space bar to make your selections below\n\n")
    val1 = val & 1
    val2 = val & 2
    val3 = val & 4
    val4 = val & 8
    if val1: 
        print(f"[X]\tEnhanced crystal weapon seed")
    else:
        print(f"[ ]\tEnhanced crystal weapon seed")

    if val2: 
        print(f"[X]\t6 Crystal armour seeds (Full Crystal)")
    else:
        print(f"[ ]\t6 Crystal armour seeds (Full Crystal)")

    if val3: 
        print(f"[X]\t5 Crystal armour seeds (No crystal helm)")
    else:
        print(f"[ ]\t5 Crystal armour seeds (No crystal helm)")

    if val4: 
        print(f"[X]\tYoungllef")
    else:
        print(f"[ ]\tYoungllef")

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


def runCG():

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
                if cursorPos == 1 and selected & 4 == 0:
                    selected += 2**cursorPos
                elif cursorPos == 2 and selected & 2 == 0:
                    selected += 2**cursorPos
                elif cursorPos == 0 or cursorPos == 3:
                    selected += 2**cursorPos

        if var == "B":
            if cursorPos < 4:
                cursorPos += 1
        if var == "A":
            if cursorPos > 0:
                cursorPos -= 1
        printIt(selected, cursorPos)

    simulateCG(selected)

    print("\n\nWould you like to return to the simulator?")
    print("Press \'e\' to exit")
    print("Press any other key to continue...")

    var = getch()

    if var == 'e':
        return 1
    return 0

