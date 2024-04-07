# Entry point into the system include functions such as mode selection and the editing of system variables
# ENG-1013 - Project - A21
# Created By : Varon Nethan Rasiah 
# Created Date: 22/03/2024
# version ='1.0'


import ControlSubSystem as control

# Iniitalization of system variables
passwordFile = "/Users/varonrasiah/Documents/Moansh/ENG1013/Project/Code/password.txt"
userPin = 1234
pollingFrequency = 5

def ServiesSubSystem():

    global userPin
    global pollingFrequency

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
        
        if mode == 1:
            control.ControlSubSystem(mode)
        elif mode == 2:
            control.ControlSubSystem(mode)
        elif mode == 3:

            passwordTries = 0 
            while passwordTries < 3:
                while True:
                    try:
                        userEnteredPasscode = int(str(input("Enter pin to access admin fucntionality --> ")))  #validate the pin
                        break
                    except ValueError:
                        print("please enter a set of digits and not letters or any other symbols")
                display(userEnteredPasscode)
                passwordTries += 1
                pinCondition = authenticate(userEnteredPasscode)
                if pinCondition == True:
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
            passwordPersistence(userPin)
            print("Exiting program functionality")
            break





def display(pin):
    print(pin)


def authenticate(userEnteredPassCode):
    if userEnteredPassCode == userPin:
        return True
    else:
        return False
    

def passwordPersistence(pin):
    try:
        f = open(passwordFile,"w")
        f.write(str(pin))
        f.close()
    except:
        print("some error has occured during the file write operation in trying to persist the user pass code.")


def print_welcome_screen():
    print()
    print("================================================================================")
    print("============================= Main Menu ========================================")
    print("================================================================================")
    print()
    print("Modes Available --> ")
    print()
    print("       1 : for Normal Operation Mode")
    print("       2 : for Data Observation Mode")
    print("       3 : Maintenence and Adjustment Mode")
    print("       4 : Terminate program")
    print()
    print("================================================================================")
    print("================================================================================")



def print_system_variable_edit_menu():
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
