import os

from math import comb
from getch import getch


def isFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def calculate():
    os.system("clear")
    
    title = """
╔╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╗
╠╬╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╬╣
╠╣  ______            __                      __              __                         ╠╣
╠╣ /      \          /  |                    /  |            /  |                        ╠╣
╠╣/$$$$$$  | ______  $$ |  _______  __    __ $$ |  ______   _$$ |_     ______    ______  ╠╣
╠╣$$ |  $$/ /      \ $$ | /       |/  |  /  |$$ | /      \ / $$   |   /      \  /      \ ╠╣
╠╣$$ |      $$$$$$  |$$ |/$$$$$$$/ $$ |  $$ |$$ | $$$$$$  |$$$$$$/   /$$$$$$  |/$$$$$$  |╠╣
╠╣$$ |   __ /    $$ |$$ |$$ |      $$ |  $$ |$$ | /    $$ |  $$ | __ $$ |  $$ |$$ |  $$/ ╠╣
╠╣$$ \__/  /$$$$$$$ |$$ |$$ \_____ $$ \__$$ |$$ |/$$$$$$$ |  $$ |/  |$$ \__$$ |$$ |      ╠╣
╠╣$$    $$/$$    $$ |$$ |$$       |$$    $$/ $$ |$$    $$ |  $$  $$/ $$    $$/ $$ |      ╠╣
╠╣ $$$$$$/  $$$$$$$/ $$/  $$$$$$$/  $$$$$$/  $$/  $$$$$$$/    $$$$/   $$$$$$/  $$/       ╠╣
╠╬╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╬╣
╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╝

Enter the word \"exit\" to return to the Main Menu
    """

    while True:
        os.system("clear")
        print(title + "\n")

        goodVal = False

        rate = 0.0

        while not goodVal:
            value = input("Enter the drop rate for the item: ")

            if value == "exit":
                return

            if isFloat(value):
                if float(value) < 1:
                    print("Successfully input decimal value")
                    rate = float(value)
                    goodVal = True
                else:
                    print("Drop rate cannot be greater than 1")
            else:
                vals = value.split("/")
                if len(vals) != 2:
                    print("Invalid fraction entered")
                    continue
                if vals[0].isdigit() and vals[1].isdigit():
                    rate = float(vals[0])/float(vals[1])
                    goodVal = True


        print("Value: %.6f" % rate) 
        print("Drop rate: 1/%.1f\n" % (1/rate))

        goodVal = False

        KC = 0

        while not goodVal:
            newValue = input("Enter your kill count: ")
            if newValue == "exit":
                return
            if newValue.isdigit():
                KC = int(newValue)
                goodVal = True
            else:
                print("Invalid number")

        goodVal = False

        total = 0

        while not goodVal:
            Value = input("Enter total drops obtained: ")
            if Value == "exit":
                return
            if Value.isdigit() and int(Value) <= KC:
                total = int(Value)
                goodVal = True
            else:
                print("Invalid number")


        prob = 0.0
        last_prob = 0.0
        for i in range(0, total+1):
            last_prob = 100.0*(comb(KC, i)*(rate**i)*((1-rate)**(KC-i)))
            prob += last_prob

        #prob = 100.0 - prob

        perc = "%"

        print("You have a %.4f%s chance to have exactly %d drops in %d kills" % (last_prob, perc, total, KC))
        if total != KC:
            print("You would have a %.4f%s percent chance of having more than %d drops" % (100.0-prob, perc, total))
        if total != 0:
            print("You would have a %.4f%s percent chance of having less than %d drops" % (prob-last_prob, perc, total))


        if prob < 1.0:
            print("\nWOW... maybe consider giving up?")
        elif prob < 5.0:
            print("\nWelcome to HELL!! It's dry here isn't it.")
        elif prob < 15.0:
            print("\nDid you put those numbers in right??")
        elif prob < 30.0:
            print("\nHey, things could be worse!")
        elif prob < 50.0:
            print("\nIf it makes you feel any better, you are not any closer to obtaining the drop")
        elif prob < 70.0:
            print("\nHey, not to bad huh?")
        elif prob < 85.0:
            print("\nWe get it, you got lucky")
        elif prob < 95.0:
            print("\nNo big deal... happens all the time (-_-)")
        elif prob < 99.0:
            print("\nThere are a lot of people who really do not like you")
        else:
            print("\nThis must be the second coming, because you are RN JESUS!!")



        print("\n\nPress any key to continue")
        print("Or press \'e\' to exit")
        var = getch()

        if var == 'e':
            return
