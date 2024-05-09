# Function that handles all the inputs necessary system wide. 
# ENG-1013 - Project - A21
# Created By : Varon Nethan Rasiah 
# Created Date: 22/03/2024
# version ='1.0'
from pymata4 import pymata4
import time
import ServicesSubSystem as service
import math

trigPin = 5
echoPin = 3
button = 4
thermistorA = 0

steinHartA = 1.1235*(10**-3)
steinHartB = 2.3500*(10**-4)
steinHartC = 8.4538*(10**-8)
circuitR1 = 9900
supplyVoltage = 1023.00

board = service.board

ultra_sonic_distance_input = []
ultra_sonic_time_input = [] #Persisting input data in the subsystem for other usages with relevant time when required. eg graphing
push_button_input = []
temperature_readings = []
temp_time_readings = []

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



