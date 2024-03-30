
import ControlSubSystem as control

# Iniitalization of system variables
userPin = 1234

def ServiesSubSystem():
    while True:
        while True:
            try:
                mode = int(input("Enter the selected mode, 1: Normal, 2: Data and 3: maintenence and adjustments 4: terminate program--> "))
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
            while passwordTries <= 3:
                try:
                    userEnteredPasscode = int(str(input("Enter pin to access admin fucntionality --> ")))  #validate the pin
                    display(userEnteredPasscode)
                    passwordTries += 1
                    pinCondition = authenticate(userEnteredPasscode)
                    if pinCondition == True:
                        break
                except ValueError:
                    print("please enter a set of digits and not letters or any other symbols")
            if pinCondition == True:
                print("access to system variables granted.")
                # grant access to system variables
                # grant access to system variable editing
            else:
                print("Incorrect pin! exiting program.")
                break
        elif mode == 4:
            break





def display(pin):
    print(pin)


def authenticate(userEnteredPassCode):
    if userEnteredPassCode == userPin:
        return True
    else:
        return False