import time as time
import InputSubSystem as input 
import OutputSubSystem as output

def ControlSubSystem(mode):
    stage1 = True
    stage2 = True

    if mode == 1:
        try:
            light_sequence(1)
            while True:
                sensorInput = input(1)
                buttonInput = input(2)
                conditionState = check_conditions(sensorInput,buttonInput)
                if conditionState == 1:
                    light_sequence(1)
                elif conditionState == 2:
                    light_sequence(2)
                elif conditionState == 3:
                    light_sequence(1)
                
        except KeyboardInterrupt:
            print("Polling loop terminated")

    elif mode == 2:

        try:
            print("Normal mode")
        except KeyboardInterrupt:
            print("Data observation")



def light_sequence(startStage):
    if startStage == 1:

        initialTime = get_current_time()
        timeDiffrerence = 0 
        while timeDiffrerence <= 30.0:
            output(startStage)
            timeDiffrerence = get_current_time() - initialTime

        output(startStage+1)
        output(startStage+2)
    elif startStage == 4:
        output(startStage)
        output(startStage+1)
        output(startStage+2)
    

def check_conditions(buttonInput, SensorInput,mode):
    if mode == "t":
        
        # these assigments are just test assignemnet proper conditions should be implemented in the future under the else section
        if buttonInput >= 3 and SensorInput >= 100:
            conditionState = 2
        elif buttonInput >= 3 and SensorInput <= 50:
            conditionState == 1
    
        
    else:
        print("actual conditions to be implemented")



def get_current_time():
    return time.time()