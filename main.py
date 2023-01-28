import pyfiglet
import time
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

            twoOption()
            time.sleep(wait)

            threeOption()


        print("Do you want to play again?")
        print("1. Yes    2. No")
        option = input()
        if option == "1":
            game = False
        if option == "2":
            "Thanks for playing!"
            break








# print("Game over")






































