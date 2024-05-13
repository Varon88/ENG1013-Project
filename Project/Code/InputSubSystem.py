# Function that handles all the inputs necessary system wide. 
# ENG-1013 - Project - A21
# Created By : Varon Nethan Rasiah 
# Created Date: 22/03/2024
# version ='1.0'
from pymata4 import pymata4
import time
import ServicesSubSystem as service
import math

# Pins
trigPin1 = 5
echoPin1 = 3
trigPin2 = 10
echoPin2 = 11
button = 4
thermistorA = 0

# Necessary Constants
steinHartA = service.steinHartA
steinHartB = service.steinHartB
steinHartC = service.steinHartC
circuitR1 = service.circuitR1
supplyVoltage = service.supplyVoltage
ultraSonic2Height = service.ultraSonic2Height

board = service.board

# Persisting input data in the subsystem for other usages with relevant time when required. eg graphing
ultra_sonic_distance_input = []
ultra_sonic_time_input = []
push_button_input = []
temperature_readings = []
temp_time_readings = []
ultra_sonic_height = []

def input_sub_system(type):

    """
        Function that houses the main functionality of the input subsystem
        Takes in a single parameter named type that indicated the type of input needed
    """
    global ultra_sonic_distance_input
    global ultra_sonic_time_input
    global push_button_input
    global temperature_readings
    global temp_time_readings
    global board
    
    if type == 1: # Button Presses

        #TODO: Covert this into a analog input
        board.set_pin_mode_digital_input(button)
        time.sleep(0.025)

        buttonData = board.digital_read(button)
        buttonPress = buttonData[0]
        push_button_input.append(buttonData)
        return buttonPress
    
    elif type == 2: # UltraSonic main

        board.set_pin_mode_sonar(trigPin1, echoPin1, timeout=200000)
        time.sleep(0.5)

        data = board.sonar_read(trigPin1)
        ultra_sonic_distance_input.append(data[0])
        ultra_sonic_time_input.append(data[1])
        distance = data[0]
        return distance

    elif type == 3: # Temperature

        board.set_pin_mode_analog_input(thermistorA)
        rawReading = board.analog_read(thermistorA)
        voltage = rawReading[0]
        if voltage == 0:
            time.sleep(0.02)
            rawReading = board.analog_read(thermistorA)
            voltage = rawReading[0]
        time_read = rawReading[1]
        R2 = circuitR1 * ((supplyVoltage/voltage)-1)
        logR2 = math.log(R2)
        tempK = (1.0 / (steinHartA + steinHartB*logR2 + steinHartC*(logR2**3)))
        tempC = tempK - 273.15
        temperature_readings.append(tempC)
        temp_time_readings.append(time_read)
        return tempC

    elif type == 4:

        board.set_pin_mode_sonar(trigPin2, echoPin2, timeout=200000)
        time.sleep(0.5)

        data = board.sonar_read(trigPin2)
        heightReturned = data[0]
        actualHeight = ultraSonic2Height - heightReturned
        ultra_sonic_height.append(actualHeight)
        return actualHeight




