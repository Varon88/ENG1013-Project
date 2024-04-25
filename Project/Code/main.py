# Code that acts as the entry point ot the services subsystem
# ENG-1013 - Project - A21
# Created By : Varon Nethan Rasiah 
# Created Date: 22/03/2024
# version ='1.0'

import ServicesSubSystem as service


# Password retrival
try:
    passwordFile = "/Users/varonrasiah/Documents/Moansh/ENG1013/Project/Code/password.txt"
    f = open(passwordFile,"r")
    password = f.read()
    f.close()
    
    service.userPin = int(password)

except FileNotFoundError:
    print("File storing passwords hasnt been found please recheck path specification or file existence and try again")
except ValueError:
    print("Check if the passcode is stored is in the valid format within the password file")


service.Servies_Sub_System()
