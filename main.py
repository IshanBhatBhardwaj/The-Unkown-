import pyfiglet
import time

import Options
from Messages import *
from Options import *


title = "THE UNKNOWN"
speed = 0
global game
game = False
GAME = False
wait = 0
sevenCount = 0

count = 0

def end_game(x):
    if x == True:
        return True
    else:
        return False





if __name__ == '__main__':


    while GAME == False:

        while game == False:
            count += 1
            if count == 1:
                game = True
            printOpenMessage()
            oneMessage()
            oneOption()
            time.sleep(wait)

            if twoOption() == True:
                break
            else:
                pass

            clueOption()

            time.sleep(wait)

            if threeOption() == True:
                break
            else:
                break


        print("Do you want to play again?")
        print("1. Yes    2. No")
        option = input()
        if option == "1":
            game = False
        if option == "2":
            "Thanks for playing!"
            break








# print("Game over")



































