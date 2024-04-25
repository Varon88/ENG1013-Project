# Function that handles all the inputs necessary system wide. 
# ENG-1013 - Project - A21
# Created By : Varon Nethan Rasiah 
# Created Date: 22/03/2024
# version ='1.0'
from pymata4 import pymata4
import time
import ServicesSubSystem as service

trigPin = 3
echoPin = 6
button = 5
board = service.board

ultra_sonic_distance_input = []
ultra_sonic_time_input = [] #Persisting input data in the subsystem for other usages with relevant time when required. eg graphing
push_button_input = []

def Input_Sub_System(type):

    global ultra_sonic_distance_input
    global ultra_sonic_time_input
    global push_button_input
    """
        Function that houses the main functionality of the input subsystem
        Takes in a single parameter named type that indicated the type of input needed
    """
    global board
    
    if type == 1:
        board.set_pin_mode_digital_input(button)
        time.sleep(0.025)

        buttonData = board.digital_read(button)
        buttonPress = buttonData[0]
        push_button_input.append(buttonData)
        return buttonPress
    
    elif type == 2:

        board.set_pin_mode_sonar(trigPin,echoPin, timeout=200000)
        time.sleep(2)

        data = board.sonar_read(trigPin)
        ultra_sonic_distance_input.append(data[0])
        ultra_sonic_time_input.append(data[1])
        distance = data[0]
        return distance

    elif type == 3:
        return 200