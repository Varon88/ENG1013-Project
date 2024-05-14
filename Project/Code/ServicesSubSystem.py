# Entry point into the system include functions such as mode selection and the editing of system variables
# ENG-1013 - Project - A21
# Created By : Varon Nethan Rasiah 
# Created Date: 22/03/2024
# version ='1.0'

import GlobalSystemVariables as systemVariables
import time

passwordFile = "/Users/varonrasiah/Documents/Moansh/ENG1013/Project/Code/password.txt"
userPin = systemVariables.userPin
pollingFrequency = systemVariables.pollingFrequency
maintenanceTimeout = systemVariables.maintenanceTimeout
maxHeight = systemVariables.maxHeight
steinHartA = systemVariables.steinHartA
steinHartB = systemVariables.steinHartB
steinHartC = systemVariables.steinHartC
circuitR1 = systemVariables.circuitR1
supplyVoltage = systemVariables.supplyVoltage
ultraSonic2Height = systemVariables.ultraSonic2Height


from pymata4 import pymata4
try:
    board = pymata4.Pymata4()
except:
    print("Board Instance ID has timed out. Try reconnecting the board and restart the code")
import ControlSubSystem as control
# Initialization of system variables with default values


pins = []

lookupDictionary = {
    "0" : "1111110",
    "1" : "0110000",
    "2" : "1101101",
    "3" : "1111001",
    "4" : "0110011",
    "5" : "1011011",
    "6" : "1011111", 
    "7" : "1110000",
    "8" : "1111111",
    "9" : "1111011",

    "A" : "1110111",
    "B" : "1111111",
    "C" : "1001110",
    "D" : "1111110",
    "E" : "1001111",
    "F" : "1000111",
    "G" : "1011110",
    "r" : "0000101",
    "U" : "0111110"
}

def servies_sub_system():

    """
        The function that hold the main functionality of the services subsystem
        No parameters are taken in.
        Contains the main menu
        
    """

    global userPin, pollingFrequency, maintenanceTimeout, maxHeight, steinHartA
    global steinHartB, steinHartC, circuitR1, supplyVoltage, ultraSonic2Height

    while True:
        while True:
            try:
                print_welcome_screen()
                mode = int(input("Enter the selected mode --> "))
                if mode > 4 and mode < 0:
                    print("Enter a valid number within the range 1 to 4.")
                    pass
                else:
                    break
            except ValueError:
                print("Enter a valid input of 1,2 or 3")
            except KeyboardInterrupt:
                print("\nKeyboard interrupt not allowed enter 4 in the main menu to exit program functionality")
                pass
        
        if mode == 1:
            control.control_sub_system(mode)
        elif mode == 2:
            control.control_sub_system(mode)
        elif mode == 3:

            try:
                passwordTries = 0
                startTime = time.time()
                while passwordTries < 3:
                    timeoutCondition = check_timeout(startTime)
                    if timeoutCondition:
                        timeout_message()
                        break
                    while True:
                        timeoutCondition = check_timeout(startTime)
                        if timeoutCondition:
                            timeout_message()
                            break
                        try:
                            userEnteredPasscode = int(str(input("Enter pin to access admin functionality --> ")))  #validate the pin
                            break
                        except ValueError:
                            print("please enter a set of digits and not letters or any other symbols")
                    display(str(userEnteredPasscode))
                    passwordTries += 1
                    pinCondition = authenticate(userEnteredPasscode)
                    timeoutCondition = check_timeout(startTime)
                    if timeoutCondition:
                        timeout_message()
                        break
                    if pinCondition == True:
                        display("ACCG")
                        break
                    else:
                        display("Err")
                        print(f"Incorrect pin entered please try again; Tries remaining = {3-passwordTries}")
                timeoutCondition = check_timeout(startTime)
                if timeoutCondition:
                    timeout_message()
                    continue

                if pinCondition == True:
                    print("Access to system variables granted.")
                    timeoutCondition = check_timeout(startTime)
                    if timeoutCondition:
                        timeout_message()
                        continue

                    while True:
                        while True:
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            try:
                                print_system_variable_edit_menu()
                                systemVarChangeSelection = int(str(input("Enter which system variable that needes to be changed --> ")))
                                break
                            except ValueError:
                                print("please enter a selection of either 1 for pin or 2 for the polling frequency -->")
                            except KeyboardInterrupt:
                                print("Exited to main program functionality")
                        timeoutCondition = check_timeout(startTime)
                        if timeoutCondition:
                            timeout_message()
                            break

                        interruptCondition = False

                        if systemVarChangeSelection == 1:
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            while True:
                                timeoutCondition = check_timeout(startTime)
                                if timeoutCondition:
                                    timeout_message()
                                    break
                                try:
                                    newPin = int(str(input("Enter new pin of 4 digits--> ")))
                                    if len(str(newPin)) == 4:
                                        display(str(newPin))
                                        break
                                    else:
                                        display("Err")
                                        print("Pin requires 4 digits. Please try again.")
                                except ValueError:
                                    display("Err")
                                    print("please enter a set of digits and not letters or any other symbols")
                                except KeyboardInterrupt:
                                    interruptCondition = True
                                    break
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            if not interruptCondition:
                                display("5UC5")
                                userPin = newPin
                            else:
                                continue

                        elif systemVarChangeSelection == 2:
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            while True:
                                timeoutCondition = check_timeout(startTime)
                                if timeoutCondition:
                                    timeout_message()
                                    break
                                try:
                                    newPollingFreq = int(str(input("Enter new polling frequency --> ")))
                                    if newPollingFreq > 5:
                                        print("Invalid polling frequency entered please enter a frequency below 5.")
                                        continue
                                    break
                                except ValueError:
                                    display("Err")
                                    print("Please enter a set of digits and not letters or any other symbols")
                                except KeyboardInterrupt:
                                    interruptCondition = True
                                    break
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            if not interruptCondition:
                                pollingFrequency = newPollingFreq
                            else:
                                continue

                        elif systemVarChangeSelection == 3:
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            while True:
                                timeoutCondition = check_timeout(startTime)
                                if timeoutCondition:
                                    timeout_message()
                                    break
                                try:
                                    newMaintenanceTimeout = int(str(input("Enter new maintenance timeout in seconds --> ")))
                                    if newMaintenanceTimeout > 120:
                                        print("Invalid polling frequency entered please enter a frequency above 120s.")
                                        continue
                                    break
                                except ValueError:
                                    display("Err")
                                    print("Please enter a set of digits and not letters or any other symbols")
                                except KeyboardInterrupt:
                                    interruptCondition = True
                                    break
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            if not interruptCondition:
                                maintenanceTimeout = newMaintenanceTimeout
                            else:
                                continue

                        elif systemVarChangeSelection == 4:
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            while True:
                                timeoutCondition = check_timeout(startTime)
                                if timeoutCondition:
                                    timeout_message()
                                    break
                                try:
                                    newMaxHeight = int(str(input("Enter max height of vehicles allowed to pass in cm --> ")))
                                    if newMaxHeight > 28:
                                        print("Invalid max height please enter a max height less than 28 cm.")
                                        continue
                                    break
                                except ValueError:
                                    display("Err")
                                    print("Please enter a set of digits and not letters or any other symbols")
                                except KeyboardInterrupt:
                                    interruptCondition = True
                                    break
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            if not interruptCondition:
                                maxHeight = newMaxHeight
                            else:
                                continue

                        elif systemVarChangeSelection == 5:
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            while True:
                                timeoutCondition = check_timeout(startTime)
                                if timeoutCondition:
                                    timeout_message()
                                    break
                                try:
                                    newSteinA = int(str(input("Enter new Stein Hart Coefficient A --> ")))
                                    break
                                except ValueError:
                                    display("Err")
                                    print("Please enter a set of digits and not letters or any other symbols")
                                except KeyboardInterrupt:
                                    interruptCondition = True
                                    break
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            if not interruptCondition:
                                steinHartA = newSteinA
                            else:
                                continue


                        elif systemVarChangeSelection == 6:
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            while True:
                                timeoutCondition = check_timeout(startTime)
                                if timeoutCondition:
                                    timeout_message()
                                    break
                                try:
                                    newSteinB = int(str(input("Enter new Stein Hart Coefficient B --> ")))
                                    break
                                except ValueError:
                                    display("Err")
                                    print("Please enter a set of digits and not letters or any other symbols")
                                except KeyboardInterrupt:
                                    interruptCondition = True
                                    break
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            if not interruptCondition:
                                steinHartB = newSteinB
                            else:
                                continue


                        elif systemVarChangeSelection == 7:
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            while True:
                                timeoutCondition = check_timeout(startTime)
                                if timeoutCondition:
                                    timeout_message()
                                    break
                                try:
                                    newSteinC = int(str(input("Enter new Stein Hart Coefficient C --> ")))
                                    break
                                except ValueError:
                                    display("Err")
                                    print("Please enter a set of digits and not letters or any other symbols")
                                except KeyboardInterrupt:
                                    interruptCondition = True
                                    break
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            if not interruptCondition:
                                steinHartC = newSteinC
                            else:
                                continue

                        elif systemVarChangeSelection == 8:
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            while True:
                                timeoutCondition = check_timeout(startTime)
                                if timeoutCondition:
                                    timeout_message()
                                    break
                                try:
                                    newCircuitR1 = int(str(input("Enter new R1 value for the thermistor set up --> ")))
                                    if newCircuitR1 > 0:
                                        print("Please make sure the entered value of resistance is positive")
                                    break
                                except ValueError:
                                    display("Err")
                                    print("Please enter a set of digits and not letters or any other symbols")
                                except KeyboardInterrupt:
                                    interruptCondition = True
                                    break
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            if not interruptCondition:
                                circuitR1 = newCircuitR1
                            else:
                                continue

                        elif systemVarChangeSelection == 9:
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            while True:
                                timeoutCondition = check_timeout(startTime)
                                if timeoutCondition:
                                    timeout_message()
                                    break
                                try:
                                    newSupplyVoltage = int(str(input("Enter new supply voltage (5v -> 1023 and 0V -> 0 ) --> ")))
                                    if 0 >= newSupplyVoltage >= 1023:
                                        print("Voltage range should be between a value of 1023 and 0 please re-enter a value within this range.")
                                    break
                                except ValueError:
                                    display("Err")
                                    print("Please enter a set of digits and not letters or any other symbols")
                                except KeyboardInterrupt:
                                    interruptCondition = True
                                    break
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            if not interruptCondition:
                                supplyVoltage = newSupplyVoltage
                            else:
                                continue

                        elif systemVarChangeSelection == 10:
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            while True:
                                timeoutCondition = check_timeout(startTime)
                                if timeoutCondition:
                                    timeout_message()
                                    break
                                try:
                                    newUltraSonicHeight = int(str(input("Enter new ultrasonic height in cm--> ")))
                                    if 5 >= newUltraSonicHeight >= 28:
                                        print("Please enter a valid Ultrasonic height within the range 28 <= height <= 0.")
                                    break
                                except ValueError:
                                    display("Err")
                                    print("Please enter a set of digits and not letters or any other symbols")
                                except KeyboardInterrupt:
                                    interruptCondition = True
                                    break
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            if not interruptCondition:
                                ultraSonic2Height = newUltraSonicHeight
                            else:
                                continue

                        elif systemVarChangeSelection == 11:
                            break
                        interruptCondition = False
                else:
                    print("Incorrect pin entered multiple times! System Locked out.")
                    system_lockout()
                    continue
            except KeyboardInterrupt:
               print("\n Exited maintenance and adjustment mode.")
        elif mode == 4:
            system_variable_persistence()
            print("Shutting down-board")
            board.shutdown()
            print("Exiting program functionality")
            break



def trigger_pins(binaryString = None,mode = 1):  #mode 1 for normal operation, mode 2 for clear with string as None

    """
        This function is used to trigger relevant pins in the arduino to display messages that are needed
        Parameters : binaryString(String) contains the binary version of a character that needs to be displayed, None by default
                     mode(int) caries the mode where 1 is normal operation and 2 is used to reset all pins to turn of currently displayed elements
        
        Clear functionality functions only when the binaryString is set to None and the mode is set to 2
    """

    if mode == 1 and not(binaryString == None):
        for j in range(len(binaryString)):
            if binaryString[j] == "1":
                board.digital_write(pins[j],1)
            elif binaryString[j] == "0":
                board.digital_write(pins[j],0)
    elif mode == 2 and (binaryString == None):
        for pin in pins:
            board.digital_write(pin,0)


def segment_selection(digitNum):
    """
        This function is used to preset the segment at which the number is to be displayed based on the requirement.
        Parameters : digitNum(int) corresponds to the relevant digit spot that needs to be enabled
    """
    D1 = 9
    D2 = 10
    D3 = 11
    D4 = 12
    if digitNum == 1:
        board.digital_write(D1,0)
        board.digital_write(D2,1)
        board.digital_write(D3,1)
        board.digital_write(D4,1)
    elif digitNum == 2:
        board.digital_write(D1,1)
        board.digital_write(D2,0)
        board.digital_write(D3,1)
        board.digital_write(D4,1)
    elif digitNum == 3:
        board.digital_write(D1,1)
        board.digital_write(D2,1)
        board.digital_write(D3,0)
        board.digital_write(D4,1)
    elif digitNum == 4:
        board.digital_write(D1,1)
        board.digital_write(D2,1)
        board.digital_write(D3,1)
        board.digital_write(D4,0)

def display(displayString):

    """
        Function is used to display needed element on the seven segment display
        1 parameter named pin is taken in, This usually holds the user pin
    
    """
    initialize_display_pins()
    repetitionFactor = 0
    startTime = time.time()
    displayTime = 0
    currentCycle = 1
    displayStringLength = len(displayString)

    if displayStringLength <= 4:
        if displayStringLength == 4:
            repetitionFactor = 4
        elif displayStringLength == 3:
            repetitionFactor = 3
        elif displayStringLength == 2:
            repetitionFactor = 2
        elif displayStringLength == 1:
            repetitionFactor = 1

    if repetitionFactor == 4:
        element1 = lookupDictionary[displayString[0]]
        element2 = lookupDictionary[displayString[1]]
        element3 = lookupDictionary[displayString[2]]
        element4 = lookupDictionary[displayString[3]]
    elif repetitionFactor == 3:
        element1 = lookupDictionary[displayString[0]]
        element2 = lookupDictionary[displayString[1]]
        element3 = lookupDictionary[displayString[2]]
    elif repetitionFactor == 2:
        element1 = lookupDictionary[displayString[0]]
        element2 = lookupDictionary[displayString[1]]
    elif repetitionFactor == 1:
        element1 = lookupDictionary[displayString[0]]


    while displayTime < 3:
        if repetitionFactor == 1:
            segment_selection(1)
            trigger_pins(element1)
            trigger_pins(None,2)
        else:
            if currentCycle%repetitionFactor == 1:
                segment_selection(1)
                trigger_pins(element1)
                trigger_pins(None,2)
            elif currentCycle%repetitionFactor == 2:
                segment_selection(2)
                trigger_pins(element2)
                trigger_pins(None,2)
            elif currentCycle%repetitionFactor == 3:
                segment_selection(3)
                trigger_pins(element3)
                trigger_pins(None,2)
            elif currentCycle%repetitionFactor == 0:
                if repetitionFactor == 4:
                    segment_selection(4)
                    trigger_pins(element4)
                elif repetitionFactor == 3:
                    segment_selection(3)
                    trigger_pins(element3)
                elif repetitionFactor == 2:
                    segment_selection(2)
                    trigger_pins(element2)

                trigger_pins(None,2)

        displayTime = time.time() - startTime

        currentCycle += 1

        if currentCycle > repetitionFactor:
            currentCycle = 1
        


def authenticate(userEnteredPassCode):

    """
        Function is used to authenticate the user entered pin
        1 parameter of type integer is taken in.
    """

    if userEnteredPassCode == userPin:
        return True
    else:
        return False
    

def system_variable_persistence():

    """
        Function saves the user edited system variables on to the file specified.
        takes in 1 parameter named pin of type int
    """
    global userPin, pollingFrequency, maintenanceTimeout, maxHeight, steinHartA
    global steinHartB, steinHartC, circuitR1, supplyVoltage, ultraSonic2Height
    variables_list = [userPin, pollingFrequency, maintenanceTimeout, maxHeight, steinHartA, steinHartB, steinHartC, circuitR1, supplyVoltage, ultraSonic2Height]
    try:
        f = open(passwordFile, "w")
        for variable in variables_list:
            f.writelines(str(variable) + "\n")
        f.close()
    except:
        print("some error has occurred during the file write operation in trying to persist the user pass code.")


def print_welcome_screen():

    """
        Function that prints in the formatted main menu
        No parameters taken in
    """

    print()
    print("================================================================================")
    print("============================= Main Menu ========================================")
    print("================================================================================")
    print()
    print("Modes Available --> ")
    print()
    print("       1 : For Normal Operation Mode")
    print("       2 : For Data Observation Mode")
    print("       3 : Maintenance and Adjustment Mode")
    print("       4 : Terminate program")
    print()
    print("================================================================================")
    print("================================================================================")



def print_system_variable_edit_menu():

    """
        Function that prints in the formatted system settings menu
        No parameters taken in
    """

    print()
    print("================================================================================")
    print("============================= System Variables =================================")
    print("================================================================================")   
    print()
    print("Current System Variable Values --> ")
    print()
    print(f"       User-Pin : {userPin}")
    print(f"       Polling rate : {pollingFrequency}")
    print(f"       Maintenance timeout : {maintenanceTimeout}")
    print(f"       Max height : {maxHeight}")
    print(f"       Stein Hart Constant A : {steinHartA}")
    print(f"       Stein Hart Constant B : {steinHartB}")
    print(f"       Stein Hart Constant C : {steinHartC}")
    print(f"       Resistance R1 Temp : {circuitR1}")
    print(f"       Supply Voltage Proportion : {supplyVoltage}")
    print(f"       Ultra Sonic 2 height : {ultraSonic2Height}")
    print()
    print("       Enter 1 : To change the user pin")
    print("       Enter 2 : To change Polling Rate")
    print("       Enter 3 : To change the maintenance timeout")
    print("       Enter 4 : To change the max height of vehicles allowed")
    print("       Enter 5 : To change Stein Hart Constant A")
    print("       Enter 6 : To change Stein Hart Constant B")
    print("       Enter 7 : To change Stein Hart Constant C")
    print("       Enter 8 : To change the permanent resistance of R1")
    print("       Enter 9 : To change the supply voltage proportion")
    print("       Enter 10 : To change the 2nd ultrasonic sensor height")
    print("       Enter 11 : To navigate to the main menu")
    print()
    print("================================================================================")
    print("================================================================================")


def initialize_display_pins():

    """
        Function initialises pin numbers and specifies the function of each pin and populates the global pin array
    """
    global pins

    pinA = 2
    pinB = 3
    pinG = 4
    pinD = 5
    pinE = 6
    pinF = 7
    pinC = 8
    D1 = 9
    D2 = 10
    D3 = 11
    D4 = 12

    pins = [pinA,pinB,pinC,pinD,pinE,pinF,pinG]

    board.set_pin_mode_digital_output(pinA)
    board.set_pin_mode_digital_output(pinB)
    board.set_pin_mode_digital_output(pinC)
    board.set_pin_mode_digital_output(pinD)
    board.set_pin_mode_digital_output(pinE)
    board.set_pin_mode_digital_output(pinF)
    board.set_pin_mode_digital_output(pinG)
    board.set_pin_mode_digital_output(D1)
    board.set_pin_mode_digital_output(D2)
    board.set_pin_mode_digital_output(D3)
    board.set_pin_mode_digital_output(D4)



def system_lockout():
    lockoutTime = 20
    startTime = time.time()
    timeDifference = 0
    print(f"System has been locked out for {lockoutTime} seconds, system will reset to regular functionality after this time.")
    while timeDifference < lockoutTime:
        currentTime = time.time()
        timeDifference = (currentTime - startTime)



def check_timeout(startTime):
    currentTime = time.time()
    if (currentTime - startTime) >= maintenanceTimeout:
        return True
    else:
        return False


def timeout_message():
    print("\nSession has timed out.")
