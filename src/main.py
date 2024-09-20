import os
import time


from simulator import simulate
from calculator import calculate

title = """
██████████████████████████████████████████████████████████████████████████████████████████████
█▌                                                                                          ▐█
█▌  ▄██████▄     ▄████████    ▄████████    ▄████████         ▄████████  ▄█    ▄▄▄▄███▄▄▄▄   ▐█
█▌ ███    ███   ███    ███   ███    ███   ███    ███        ███    ███ ███  ▄██▀▀▀███▀▀▀██▄ ▐█
█▌ ███    ███   ███    █▀    ███    ███   ███    █▀         ███    █▀  ███▌ ███   ███   ███ ▐█
█▌ ███    ███   ███         ▄███▄▄▄▄██▀   ███               ███        ███▌ ███   ███   ███ ▐█
█▌ ███    ███ ▀███████████ ▀▀███▀▀▀▀▀   ▀███████████      ▀███████████ ███▌ ███   ███   ███ ▐█
█▌ ███    ███          ███ ▀███████████          ███               ███ ███  ███   ███   ███ ▐█
█▌ ███    ███    ▄█    ███   ███    ███    ▄█    ███         ▄█    ███ ███  ███   ███   ███ ▐█
█▌  ▀██████▀   ▄████████▀    ███    ███  ▄████████▀        ▄████████▀  █▀    ▀█   ███   █▀  ▐█
█▌                           ███    ███                                                     ▐█
█▌    ▄████████ ███▄▄▄▄   ████████▄        ▄████████    ▄████████  ▄█        ▄████████      ▐█
█▌   ███    ███ ███▀▀▀██▄ ███   ▀███      ███    ███   ███    ███ ███       ███    ███      ▐█
█▌   ███    ███ ███   ███ ███    ███      ███    █▀    ███    ███ ███       ███    █▀       ▐█
█▌   ███    ███ ███   ███ ███    ███      ███          ███    ███ ███       ███             ▐█
█▌ ▀███████████ ███   ███ ███    ███      ███        ▀███████████ ███       ███             ▐█
█▌   ███    ███ ███   ███ ███    ███      ███    █▄    ███    ███ ███       ███    █▄       ▐█
█▌   ███    ███ ███   ███ ███   ▄███      ███    ███   ███    ███ ███▌    ▄ ███    ███      ▐█
█▌   ███    █▀   ▀█   █▀  ████████▀       ████████▀    ███    █▀  █████▄▄██ ████████▀       ▐█
█▌                                                                ▀                         ▐█
█▌                                                                                          ▐█
██████████████████████████████████████████████████████████████████████████████████████████████
"""

note = """
NOTE: Currently, this simulator only has the ability to
simulate a few specific bosses. It is not a comprehensive 
simulation including the entire drop table for each of the 
included bosses. It only includes the main drops in the
collection log.
"""


loot_or_calc = """
Please choose an option from the list below:

    (a) Simulate the drops from a boss in Gilenor
    (b) Calculate how lucky (or unlucky) you are with a drop 

    (x) Exit the OSRS Loot Simulator
"""


while True:

    os.system("clear")

    print(title)


    print("\n\n\n==============================================================")
    print("Welcome to the Old School Runescape Loot Simulator v1.0")
    print("==============================================================")

    print(note,"\n\n", loot_or_calc)

    item_selected = False

    ch = ""

    while not item_selected:
        ch = input("Your Selection: ")
        
        if ch == "a" or ch == "b" or ch == "x":
            item_selected = True
        else:
            print("Your input is not valid, Please try again")
            print("(HINT: your input should only be a single letter, \"a\", \"b\" or \"x\")")

    print("\n\n")

    barRot = ["|", "/", "-", "\\"]
    j = 0

    #Just a fancy terminal animation nothing is actually being loaded
    #despite what the console is saying
    if ch == "a":
        for i in range(0,20):
            print("========== Loading Simulator... " + barRot[j] + "  ==========")
            if j == 3:
                j = 0
            else:
                j += 1
            time.sleep(0.09)
            print("\033[A                                                         \033[A")

        print("==========   Loading Complete!     ==========")
        time.sleep(0.5)

        simulate()

    if ch == "b":
        for i in range(0,20):
            print("========== Loading Calculator... " + barRot[j] + "  ==========")
            if j == 3:
                j = 0
            else:
                j += 1
            time.sleep(0.09)
            print("\033[A                                                         \033[A")

        print("==========   Loading Complete!     ==========")
        time.sleep(0.5)

        calculate()

    if ch == "x":
        break
