space = "    "
import pyfiglet
import time
wait = 0
from Monsters import *
from Timer import *
# from main import *
global future
from Timer import *

# sevenCount = 0

def gameOver():
    global game
    game = True


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
        time.sleep(wait)
        print("The beast of the unknown is hunting you")
        time.sleep(wait)
        print("Escape the cave")
        time.sleep(wait)
        print("RUN QUICK")
        fourOption()





    if option == "2":
        print(pyfiglet.figlet_format("MOOOOOOO", justify="center", width=110))
        time.sleep(.5)
        printOtherMonster()
        time.sleep(wait)
        print("The beast of the unknown is hunting you")
        time.sleep(wait)
        print("Escape the cave")
        time.sleep(wait)
        print("RUN QUICK")
        fiveOption()

def fourOption():
    print("1. Turn Left", end=space)
    print("2. Turn Right")
    option = input()

    if option == "1":
        fiveOption()

    if option == "2":
        sixOption()

def fiveOption():
    print("1. Turn Left", end=space)
    print("2. Turn Right")
    option = input()

    if option == "1":
        elevenOption()

    if option == "2":
        twelveOption()

def sixOption():
    print("1. Turn Left", end=space)
    print("2. Turn Right")
    option = input()

    if option == "1":
        sevenOption()

    if option == "2":
        eightOption()

def sevenOption():
    print("1. Turn Left", end=space)
    print("2. Turn Right")
    option = input()

    elevenOption()
def eightOption():
    print("1. Turn Left", end=space)
    print("2. Turn Right")
    option = input()

    if option == "1":
        nineOption()

    if option == "2":
        tenOption()

def nineOption():
    print("YOU RAN INTO A DEAD END")


def tenOption():
    print("YOU ESCAPED THE CAVE")


def elevenOption():
    print("1. Turn Left", end=space)
    print("2. Turn Right")
    option = input()

    fourteenOption()

def twelveOption():
    print("1. Turn Left", end=space)
    print("2. Turn Right")
    option = input()

    if option == "1":
        thirteenOption()

    if option == "2":
        fourteenOption()


def thirteenOption():
    print("1. Turn Left", end=space)
    print("2. Turn Right")
    option = input()

    if option == "1":
        fifteenOption()

    if option == "2":
        sixteenOption()


def fourteenOption():
    print("1. Turn Left", end=space)
    print("2. Turn Right")
    option = input()

    sixteenOption()

def fifteenOption():
    print("1. Turn Left", end=space)
    print("2. Turn Right")
    option = input()

    if option == "1":
        seventeenOption()

    if option == "2":
        eighteenOption()


def sixteenOption():
    print("1. Turn Left", end=space)
    print("2. Turn Right")
    option = input()

    fourOption()


def seventeenOption():
    print("YOU RAN INTO A DEAD END.")

def eighteenOption():
    print("YOU ESCAPED THE CAVE")



