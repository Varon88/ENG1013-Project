# Entry point into the system include functions such as mode selection and the editing of system variables
# ENG-1013 - Project - A21
# Created By : Varon Nethan Rasiah 
# Created Date: 22/03/2024
# version ='1.0'


import ControlSubSystem as control
from pymata4 import pymata4
import time

# Iniitalization of system variables
passwordFile = "/Users/varonrasiah/Documents/Moansh/ENG1013/Project/Code/password.txt"
userPin = 1234
pollingFrequency = 5
board = pymata4.Pymata4()
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
    "G" : "1101111"
}

def Servies_Sub_System():

    """
        The function that hold the main functionality of the servies subsystem
        No parameters are taken in.
        Contains the main menu
        
    """

    global userPin
    global pollingFrequency

    initialize_display_pins()

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
                print("\nKeyboard interupt not allowed enter 4 in the main menu to exit program functionlaity")
                pass
        
        if mode == 1:
            control.Control_Sub_System(mode)
        elif mode == 2:
            control.Control_Sub_System(mode)
        elif mode == 3:

            passwordTries = 0 
            while passwordTries < 3:
                while True:
                    try:
                        userEnteredPasscode = int(str(input("Enter pin to access admin fucntionality --> ")))  #validate the pin
                        break
                    except ValueError:
                        print("please enter a set of digits and not letters or any other symbols")
                display(str(userEnteredPasscode))
                passwordTries += 1
                pinCondition = authenticate(userEnteredPasscode)
                if pinCondition == True:
                    display("AG")
                    break
                else:
                    print(f"Incorrect pin entered please try again; Tries remaining = {3-passwordTries}")

            if pinCondition == True:
                print("Access to system variables granted.")
                while True:
                    try:
                        print_system_variable_edit_menu()
                        systemVarChangeSelection = int(str(input("Enter which system variable that needes to be changed -->")))
                        break
                    except ValueError:
                        print("please enter a selection of either 1 for pin or 2 for the polling frequency -->")
                if systemVarChangeSelection == 1:
                    while True:
                        try:
                            newPin = int(str(input("Enter new pin --> ")))  
                            break
                        except ValueError:
                            print("please enter a set of digits and not letters or any other symbols")
                    userPin =newPin
                elif systemVarChangeSelection == 2:
                    while True:
                        try:
                            newPollingFreq = int(str(input("Enter new polling frequency --> ")))  #validate the pin
                            break
                        except ValueError:
                            print("please enter a set of digits and not letters or any other symbols")
                    pollingFrequency = newPollingFreq
                elif systemVarChangeSelection == 3:
                    pass
            else:
                print("Incorrect pin! exiting program.")
                break
        elif mode == 4:
            password_Persistence(userPin)
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
        Parameters : digitNum(int) corresponds to the relevant digitspot that needs to be enabled
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
        Function is used to display needed element on the seven segement display
        1 prameter named pin is taken in, This usually holds the user pin
    
    """
    
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
    

def password_Persistence(pin):

    """
        Function saves the user edited passcode on to the file specified.
        takes in 1 parameter named pin of type int
    """

    try:
        f = open(passwordFile,"w")
        f.write(str(pin))
        f.close()
    except:
        print("some error has occured during the file write operation in trying to persist the user pass code.")


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
    print("       3 : Maintenence and Adjustment Mode")
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
    print()
    print("       Enter 1 : To change the user pin")
    print("       Enter 2 : To change Polling Rate")
    print("       Enter 3 : To naviagte to the main menu")
    print()
    print("================================================================================")
    print("================================================================================")


def initialize_display_pins():

    """
        Function initialises pin numbers and specifes the function of each pin and populates the global pin array
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


