# Code that acts as the entry point ot the services subsystem
# ENG-1013 - Project - A21
# Created By : Varon Nethan Rasiah 
# Created Date: 22/03/2024
# version ='1.0'



import GlobalSystemVariables as systemVariables

# system variable retrival
try:
    passwordFile = "/Users/varonrasiah/Documents/Moansh/ENG1013/Project/Code/password.txt"
    f = open(passwordFile, "r")
    password = f.readline()
    pollFreq = f.readline()
    mainTimeout = f.readline()
    maxHeight = f.readline()
    sthA = f.readline()
    sthB = f.readline()
    sthC = f.readline()
    crR1 = f.readline()
    supVolt = f.readline()
    usHeight = f.readline()

    f.close()
    
    systemVariables.userPin = int(password)
    systemVariables.pollingFrequency = int(pollFreq)
    systemVariables.maintenanceTimeout = int(mainTimeout)
    systemVariables.maxHeight = int(maxHeight)
    systemVariables.steinHartA = int(sthA)
    systemVariables.steinHartB = int(sthB)
    systemVariables.steinHartC = int(sthC)
    systemVariables.supplyVoltage = int(supVolt)
    systemVariables.ultraSonic2Height = int(usHeight)


except FileNotFoundError:
    print("File storing passwords hasn't been found please recheck path specification or file existence and try again")
except ValueError:
    print("Check if the passcode is stored is in the valid format within the password file")

import ServicesSubSystem as service
service.servies_sub_system()
