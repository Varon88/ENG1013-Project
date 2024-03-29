
import InputSubSystem as input 
import OutputSubSystem as output

def ControlSubSystem(mode):
   
    if mode == 1:
        try:
            while True:
                print("stages")
        except KeyboardInterrupt:
            print("Polling loop terminated")

    elif mode == 2:

        try:
            print("Normal mode")
        except KeyboardInterrupt:
            print("Data observation")



def light_sequence(startStage):
    if startStage == 1:
        output(startStage)
        output(startStage+1)
        output(startStage+2)
    elif startStage == 4:
        output(startStage)
        output(startStage+1)
        output(startStage+2)
    

