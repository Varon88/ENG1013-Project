
import ControlSubSystem as control

# Iniitalization of system variables
userPin = 1234

def ServiesSubSystem():
    while True:
        while True:
            try:
                mode = int(str(input("Enter the selected mode, 1: Normal, 2: Data and 3: maintenence and adjustments 4: terminate program--> ")))
                if mode != 1 or mode != 2 or mode != 3:
                    print("Enter a valid number within the range 1 to 4.")
                    pass
                else:
                    break
            except ValueError:
                print("Enter a valid input of 1,2 or 3")
        
        if mode == 1:
            control(mode)
        elif mode == 2:
            control(mode)
        elif mode == 3:
            passwordTries = 0 
            while passwordTries <= 3:
                userEnteredPasscode = int(str(input("Enter pin to access admin fucntionality --> ")))  #validate the pin
                display(userEnteredPasscode)
                tries += 1
                pinCondition = authenticate(userEnteredPasscode)
                if pinCondition == True:
                    break
            
            if pinCondition == True:
                print("access to system variables granted.")
                # grant access to system variables
                # grant access to system variable editing
        elif mode == 4:
            break





def display(pin):
    print(pin)


def authenticate(userEnteredPassCode):
    if userEnteredPassCode == userPin:
        return True
    else:
        return False