# Function that handles all the inputs necessary system wide. 
# ENG-1013 - Project - A21
# Created By : Varon Nethan Rasiah 
# Created Date: 22/03/2024
# version ='1.0'
from pymata4 import pymata4
import time

trigPin = 3
echoPin = 6
board = pymata4.Pymata4

def Input_Sub_System(type):

    """
        Function that houses the main functionality of the input subsystem
        Takes in a single parameter named type that indicated the type of input needed
    """
    global board
    
    if type == 1:
        return 5 # simulates the number of button presses
    elif type == 2:

        board.set_pin_mode_sonar(trigPin,echoPin, timeout=200000)
        time.sleep(2)

        data = board.sonar_read(trigPin)
        return data

    elif type == 3:
        return 200