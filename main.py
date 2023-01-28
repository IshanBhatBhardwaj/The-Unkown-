import pyfiglet
import time
from Messages import *
from Options import *
import Timer



title = "THE UNKNOWN"
speed = 0
global game
game = False
wait = 1.5











if __name__ == '__main__':

    printOpenMessage()
    oneMessage()


    while game == False:

        oneOption()
        time.sleep(wait)

        twoOption()
        time.sleep(wait)

        threeOption()




print("Game over")






































