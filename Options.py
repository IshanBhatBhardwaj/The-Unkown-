space = "    "
import pyfiglet
import time
wait = 1.5
from Monsters import *
from Timer import *

def oneOption():
    print("1. Look around", end = space)
    print("2. Scream")
    option = input()

    if option == "1":
        print(pyfiglet.figlet_format("Wooaaah", font = "slant", justify = "center", width = 110))
        time.sleep(wait)
        print("Towering mountains lean over you")
        time.sleep(wait)
        print("The ground under your torn boots is covered in thick grass")
        time.sleep(wait)
        print("In front of you is a cave")

    if option == "2":
        print(pyfiglet.figlet_format("HELP", font = "slant", justify = "center", width = 110))
        time.sleep(wait)
        print("Nobody hears you")
        time.sleep(wait)
        print("Towering mountains lean over you")
        time.sleep(wait)
        print("The ground under you torn boots is covered in thick grass")
        time.sleep(wait)
        print("In front of you is a cave")


def twoOption():
    print("1. Enter cave", end = space)
    print("2. Climb Mountain")
    option = input()

    if option == "1":
        print(pyfiglet.figlet_format("Darnkness", justify="center", width=110))
        time.sleep(wait)
        print("Carefully,an inch at a time, you enter the Unknown")
        time.sleep(wait)
        print("The air is heavy, almost like it's pushing you down, or keeping you away")
        time.sleep(wait)
        print(pyfiglet.figlet_format("plop"))
        time.sleep(wait)
        print("Somewhere down the cave, you can hear water dripping")
        time.sleep(wait)
        print(pyfiglet.figlet_format("plop"))
        time.sleep(wait)
        print("You follow the sound")



    if option == "2":
        print(pyfiglet.figlet_format("Oh yea", font="slant", justify="center", width=110))
        time.sleep(wait)
        print("As you prepare to climb the mountain, you remember your equipment")
        time.sleep(wait)
        print("Gloves, a knife, and some matches")
        time.sleep(wait)
        print("You look up at the towering mountains, unsure if you could make it to the top")
        time.sleep(wait)
        print("You have second doubts")
        twoOption()

def threeOption():
    print("1. Turn Left", end=space)
    print("2. Turn Right")
    option = input()

    if option == "1":
        print(pyfiglet.figlet_format("ROOOAAARRR",justify= "center",width= 110))
        time.sleep(.5)
        printmainMonster()
        timer()
        print("heLLO")









