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
echoPin1 = 6
trigPin2 = 10
echoPin2 = 11
buttonA = 2
thermistorA = 0
ldrA = 1

# Necessary Constants
steinHartA = service.steinHartA
steinHartB = service.steinHartB
steinHartC = service.steinHartC
circuitR1 = service.circuitR1
supplyVoltage = service.supplyVoltage
ultraSonic2Height = service.ultraSonic2Height
tempCalibration = 10.4

board = service.board

# Persisting input data in the subsystem for other usages with relevant time when required. eg graphing
ultra_sonic_distance_input = []
ultra_sonic_time_input = []
push_button_input = []
temperature_readings = []
temp_time_readings = []
ultra_sonic_height = []
push_button_voltage_input = []

def input_sub_system(type):

    """
        Function that houses the main functionality of the input subsystem
        Takes in a single parameter named type that indicated the type of input needed
    """
    global ultra_sonic_distance_input
    global ultra_sonic_time_input
    global push_button_voltage_input
    global push_button_input
    global temperature_readings
    global temp_time_readings
    global board

    
    if type == 1: # Button Presses

        board.set_pin_mode_analog_input(buttonA)
        measurement = board.analog_read(buttonA)
        voltage = measurement[0]
        push_button_voltage_input.append(voltage)
        if voltage <= 20:
            push_button_input.append(1)
            return 1
        else:
            push_button_input.append(0)
            return 0

    elif type == 2: # UltraSonic main

        board.set_pin_mode_sonar(trigPin1, echoPin1, timeout=200000)
        time.sleep(0.25)

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
        if voltage != 0:
            R2 = circuitR1 * ((supplyVoltage/voltage)-1)
            logR2 = math.log(R2)
            tempK = (1.0 / (steinHartA + steinHartB*logR2 + steinHartC*(logR2**3)))
            tempC = tempK - 273.15 + tempCalibration
            temperature_readings.append(tempC)
            temp_time_readings.append(time_read)
        else:
            tempC = 15
        return tempC

    elif type == 4:

        board.set_pin_mode_sonar(trigPin2, echoPin2, timeout=200000)
        time.sleep(0.25)

        data = board.sonar_read(trigPin2)
        heightReturned = data[0]
        actualHeight = ultraSonic2Height - heightReturned
        ultra_sonic_height.append(actualHeight)
        return actualHeight

    elif type == 5:

        board.set_pin_mode_analog_input(ldrA)
        condition = None
        firstIter = True
        while True:
            time.sleep(0.25)
            measurement = board.analog_read(ldrA)
            voltageMeasure = measurement[0]

            if firstIter == True:
                firstIter = False
            else:
                if voltageMeasure >= 300:
                    condition = "Night"
                else:
                    condition = "Day"

            return condition







