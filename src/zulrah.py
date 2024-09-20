import os
import time
import random

from getch import getch

def simulateZU(value):
    tfVal = value & 1
    mfVal = value & 2
    svVal = value & 4
    uoVal = value & 8
    tmVal = value & 16
    mmVal = value & 32
    jsVal = value & 64
    psVal = value & 128 

    tf = 0
    mf = 0
    sv = 0
    uo = 0
    tm = 0
    mm = 0
    js = 0
    ps = 0

    count = 0

    obtained = 0

    while obtained != value:
        time.sleep(0.0005)
        count += 1

        roll = random.randint(0,7935)

        if roll > 1200 and roll < 1232:
            roll = random.randint(0, 3)
            if roll == 0:
                tf += 1
                print("Tanz fang! KC: ", count)
            elif roll == 1:
                mf += 1
                print("Magic fang! KC: ", count)
            elif roll == 2:
                sv += 1
                print("Serpentine visage! KC: ", count)
            elif roll == 3:
                uo += 1
                print("Uncut onyx... KC: ", count)
        elif roll > 5325 and roll < 5646:
            roll = random.randint(0, 2631)
            if roll > 1440 and roll < 1451:
                roll = random.randint(0, 1)
                if roll == 0:
                    tm += 1
                    print("\nTanzanite Mutagen!!!!! KC: ", count)
                    print()
                elif roll == 1:
                    mm += 1
                    print("\nMagma Mutagen!!!!! KC: ", count)
                    print()


        roll = random.randint(0,7935)

        if roll > 1200 and roll < 1232:
            roll = random.randint(0, 3)
            if roll == 0:
                tf += 1
                print("Tanz fang! KC: ", count)
            elif roll == 1:
                mf += 1
                print("Magic fang! KC: ", count)
            elif roll == 2:
                sv += 1
                print("Serpentine visage! KC: ", count)
            elif roll == 3:
                uo += 1
                print("Uncut onyx... KC: ", count)
        elif roll > 5325 and roll < 5646:
            roll = random.randint(0, 2631)
            if roll > 1440 and roll < 1451:
                roll = random.randint(0, 1)
                if roll == 0:
                    tm += 1
                    print("\nTanzanite Mutagen!!!!! KC: ", count)
                    print()
                elif roll == 1:
                    mm += 1
                    print("\nMagma Mutagen!!!!! KC: ", count)
                    print()


        roll = random.randint(0,3999)

        if roll == 3120:
            ps += 1
            print("\nYou have a funny feeling like you're being followed. KC: ", count)
            print()

        roll = random.randint(0,2999)

        if roll == 1266:
            js += 1
            print("Jar of swamp!!!! KC: ", count)

        if tfVal > 0 and tf > 0: 
            obtained |= 1

        if mfVal > 0 and mf > 0:
            obtained |= 2

        if svVal > 0 and sv > 0:
            obtained |= 4

        if uoVal > 0 and uo > 0:
            obtained |= 8

        if tmVal > 0 and tm > 0:
            obtained |= 16

        if mmVal > 0 and mm > 0:
            obtained |= 32

        if jsVal > 0 and js > 0:
            obtained |= 64 

        if psVal > 0 and ps > 0:
            obtained |= 128


    print("Final Stats\n________________________")
    print("KC: ", count)
    print("Tanzanite fang: ", tf)
    print("Magic fang: ", mf)
    print("Serpentine visage: ", sv)
    print("Uncut onyx: ", uo)
    print("Tanzanite mutagen: ", tm)
    print("Magic mutagen: ", mm)
    print("Jar of swamp: ", js)
    print("Pet snakeling: ", ps)

def printIt(val, cursorPos):
    os.system("clear")
    print("Welcome to the Zulrah simulator")
    print("Please use the arrow keys and the space bar to make your selections below\n\n")
    val1 = val & 1
    val2 = val & 2
    val3 = val & 4
    val4 = val & 8
    val5 = val & 16
    val6 = val & 32
    val7 = val & 64 
    val8 = val & 128 
    if val1: 
        print(f"[X]\tTanzanite fang")
    else:
        print(f"[ ]\tTanzanite fang")

    if val2: 
        print(f"[X]\tMagic fang")
    else:
        print(f"[ ]\tMagic fang")

    if val3: 
        print(f"[X]\tSerpentine visage")
    else:
        print(f"[ ]\tSerpentine visage")

    if val4: 
        print(f"[X]\tUncut Onyx")
    else:
        print(f"[ ]\tUncut Onyx")

    if val5:
        print(f"[X]\tTanzanite mutagen")
    else:
        print(f"[ ]\tTanzanite mutagen")
        
    if val6: 
        print(f"[X]\tMagma mutagen")
    else:
        print(f"[ ]\tMagma mutagen")

    if val7: 
        print(f"[X]\tJar of swamp")
    else:
        print(f"[ ]\tJar of swamp")

    if val8: 
        print(f"[X]\tPet snakeling")
    else:
        print(f"[ ]\tPet snakeling")


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
            print("\033[9H")
        case 6:
            print("\033[10H")
        case 7:
            print("\033[11H")
        case 8:
            print("\033[14H")


def runZU():

    enter = False

    cursorPos = 0

    selected = 0

    printIt(selected, cursorPos)
    while not enter:
        var = getch()

        if var == " ":
            if cursorPos == 8:
                print("\033[2B")
                break 

            if (selected & 2**cursorPos) != 0:
                selected -= 2**cursorPos
            else:
                selected += 2**cursorPos

        if var == "B":
            if cursorPos < 8:
                cursorPos += 1
        if var == "A":
            if cursorPos > 0:
                cursorPos -= 1
        printIt(selected, cursorPos)

    simulateZU(selected)

    print("\n\nWould you like to return to the simulator?")
    print("Press \'e\' to exit")
    print("Press any other key to continue...")

    var = getch()

    if var == 'e':
        return 1
    return 0


