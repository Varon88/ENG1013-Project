# Function that handles all the inputs necessary system wide. 
# ENG-1013 - Project - A21
# Created By : Varon Nethan Rasiah 
# Created Date: 22/03/2024
# version ='1.0'

def Input_Sub_System(type):

    """
        Function that houses the main functionality of the input subsystem
        Takes in a single parameter named type that indicated the type of input needed
    """

    if type == 1:
        return 5 # simulates the number of button presses
    elif type == 2:
        return 450 #Simulates the disntace measurement using the US sensor
    elif type == 3:
        return 200