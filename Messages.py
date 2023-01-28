import time
import pyfiglet


def printOpenMessage():
    print(pyfiglet.figlet_format("THE UNKOWN", justify="center", width=110))

    time.sleep(3)

    print(pyfiglet.figlet_format("RUN", font="small", justify="center", width=110, ))
    time.sleep(1)
    print(pyfiglet.figlet_format("RUN", font="standard", justify="center", width=110, ))
    time.sleep(.50)
    print(pyfiglet.figlet_format("RUN", font="starwars", justify="center", width=110, ))
    time.sleep(.40)



def oneMessage():
    print("Tuesday")
    time.sleep(.5)
    print("Somewhere up the mountains")
