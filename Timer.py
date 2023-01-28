import time
global timeLimit
from Options import *


class Time:
    def __init__(self):
        self.timeLimit = 10
        self.startTime = time.time()

    def timer(self):
        while True:
            elapsedTime = time.time() - self.startTime
            # print(timeLimit - int(elapsedTime))
            if elapsedTime > self.timeLimit:
                print("YOU TOOK TOO LONG!GAME OVER")
                break



