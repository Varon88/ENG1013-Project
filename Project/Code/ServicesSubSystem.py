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
import numpy as np
import Display as disp

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

                    userEnteredPassocdeString = str(userEnteredPasscode)

                    if len(userEnteredPassocdeString) == 1:
                        userEnteredPassocdeString = userEnteredPassocdeString + "zzz"
                    elif len(userEnteredPassocdeString) == 2:
                        userEnteredPassocdeString = userEnteredPassocdeString + "zz"
                    elif len(userEnteredPassocdeString) == 3:
                        userEnteredPassocdeString = userEnteredPassocdeString + "z"

                    if len(str(userEnteredPasscode)) >= 4:
                        disp.display((str(userEnteredPassocdeString)+"z"), 2)
                    else:
                        disp.display((str(userEnteredPassocdeString)), 2)

                    passwordTries += 1
                    pinCondition = authenticate(userEnteredPasscode)
                    timeoutCondition = check_timeout(startTime)
                    if timeoutCondition:
                        timeout_message()
                        break
                    if pinCondition == True:
                        disp.display("5UCCE55z",2)
                        disp.turn_off_display()
                        break
                    else:
                        disp.display("Errorz",2)
                        disp.turn_off_display()
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
                                        disp.display(str(newPin)+"z",2)
                                        break
                                    else:
                                        disp.display("Errorz",2)
                                        disp.turn_off_display()
                                        print("Pin requires 4 digits. Please try again.")
                                except ValueError:
                                    disp.display("Errorz",2)
                                    disp.turn_off_display()
                                    print("please enter a set of digits and not letters or any other symbols")
                                except KeyboardInterrupt:
                                    interruptCondition = True
                                    break
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            if not interruptCondition:
                                disp.display("5UCCE55z",2)
                                disp.turn_off_display()
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
                                    disp.display("Errorz",2)
                                    disp.turn_off_display()
                                    print("Please enter a set of digits and not letters or any other symbols")
                                except KeyboardInterrupt:
                                    interruptCondition = True
                                    break
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            if not interruptCondition:
                                disp.display("5UCCE55z",2)
                                disp.turn_off_display()
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
                                    disp.display("Errorz",2)
                                    disp.turn_off_display()
                                    print("Please enter a set of digits and not letters or any other symbols")
                                except KeyboardInterrupt:
                                    interruptCondition = True
                                    break
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            if not interruptCondition:
                                disp.display("5UCCE55z",2)
                                disp.turn_off_display()
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
                                    disp.display("Errorz",2)
                                    disp.turn_off_display()
                                    print("Please enter a set of digits and not letters or any other symbols")
                                except KeyboardInterrupt:
                                    interruptCondition = True
                                    break
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            if not interruptCondition:
                                disp.display("5UCCE55z",2)
                                disp.turn_off_display()
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
                                    disp.display("Errorz",2)
                                    disp.turn_off_display()
                                    print("Please enter a set of digits and not letters or any other symbols")
                                except KeyboardInterrupt:
                                    interruptCondition = True
                                    break
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            if not interruptCondition:
                                disp.display("5UCCE55z",2)
                                disp.turn_off_display()
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
                                    disp.display("Errorz",2)
                                    disp.turn_off_display()
                                    print("Please enter a set of digits and not letters or any other symbols")
                                except KeyboardInterrupt:
                                    interruptCondition = True
                                    break
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            if not interruptCondition:
                                disp.display("5UCCE55z",2)
                                disp.turn_off_display()
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
                                    disp.display("Errorz",2)
                                    disp.turn_off_display()
                                    print("Please enter a set of digits and not letters or any other symbols")
                                except KeyboardInterrupt:
                                    interruptCondition = True
                                    break
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            if not interruptCondition:
                                disp.display("5UCCE55z",2)
                                disp.turn_off_display()
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
                                    disp.display("Errorz",2)
                                    disp.turn_off_display()
                                    print("Please enter a set of digits and not letters or any other symbols")
                                except KeyboardInterrupt:
                                    interruptCondition = True
                                    break
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            if not interruptCondition:
                                disp.display("5UCCE55z",2)
                                disp.turn_off_display()
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
                                    disp.display("Errorz",2)
                                    disp.turn_off_display()
                                    print("Please enter a set of digits and not letters or any other symbols")
                                except KeyboardInterrupt:
                                    interruptCondition = True
                                    break
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            if not interruptCondition:
                                disp.display("5UCCE55z",2)
                                disp.turn_off_display()
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
                                    disp.display("Errorz",2)
                                    disp.turn_off_display()
                                    print("Please enter a set of digits and not letters or any other symbols")
                                except KeyboardInterrupt:
                                    interruptCondition = True
                                    break
                            timeoutCondition = check_timeout(startTime)
                            if timeoutCondition:
                                timeout_message()
                                break
                            if not interruptCondition:
                                disp.display("5UCCE55z",2)
                                disp.turn_off_display()
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
            print("Turning off display")
            disp.turn_off_display()
            print("saving system variables")
            system_variable_persistence()
            print("Shutting down-board")
            board.shutdown()
            print("Exiting program functionality")
            break


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


def system_lockout():
    lockoutTime = 120
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
    disp.display("5E55ztzoUtz",2)
    disp.turn_off_display()
    print("\nSession has timed out.")
