import os
import time

from corruptedGauntlet import runCG
from generalGraardor import runGG
from kreeara import runK
from kril import runKT
from zilyana import runZ
from zulrah import runZU


title = """
 _____                                                 _____ 
( ___ )                                               ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |  ____  _                 _       _              |   | 
 |   | / ___|(_)_ __ ___  _   _| | __ _| |_ ___  _ __  |   | 
 |   | \___ \| | '_ ` _ \| | | | |/ _` | __/ _ \| '__| |   | 
 |   |  ___) | | | | | | | |_| | | (_| | || (_) | |    |   | 
 |   | |____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|    |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                               (_____)
"""

boss_list = """
(a) Corrupted Gauntlet
(b) General Graardor
(c) Kree'arra
(d) K'ril Tsutsaroth
(e) Zilyana
(f) Zulrah

(x) exit to main menu
"""

def printScr():
    
    os.system("clear")
    print(title + "\n")
    print("Please select a boss to simulate from the list below: ")
    print(boss_list)

def simulate():
    
    tryagain = False

    cont = 0

    while True:
        printScr()
        
        if tryagain:
            var = input("Your selection (Try Again): ")
        else:
            var = input("Your selection: ")

        if var == 'a':
            cont = runCG()
            if cont == 1:
                return
            tryagain = False
        elif var == 'b':
            cont = runGG()
            if cont == 1:
                return
            tryagain = False
        elif var == 'c':
            cont = runK()
            if cont == 1:
                return
            tryagain = False
        elif var == 'd':
            cont = runKT()
            if cont == 1:
                return
            tryagain = False
        elif var == 'e':
            cont = runZ()
            if cont == 1:
                return
            tryagain = False
        elif var == 'f':
            cont = runZU()
            if cont == 1:
                return
            tryagain = False
        elif var == 'x':
            return
        else:
            tryagain = True
