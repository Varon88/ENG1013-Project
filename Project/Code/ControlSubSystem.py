# Function that holds the polling loop and all intermediary functionality
# ENG-1013 - Project - A21
# Created By : Varon Nethan Rasiah 
# Created Date: 22/03/2024
# version ='1.0'


import time as time
import InputSubSystem as input 
import OutputSubSystem as output
import ServicesSubSystem as service

# light_sequence() parameters; 1 - start from start stage 1 and go on until stage 3; 4 - start from start stage 4 to stage 6


def ControlSubSystem(mode):
    
    if mode == 1:
        try:
            # light_sequence(0) -- to be used in the real scenario where output should be maintained for prolonged periods of time
            light_sequence_test(0) #test function with similar functionaly is used
            while True:

                pollingLoopStartTime = time.time()

                sensorInput = input.InputSubSystem(1)
                buttonInput = input.InputSubSystem(2)
                conditionState = check_conditions(sensorInput,buttonInput,"t")
                if conditionState == 1:
                    # light_sequence(1)
                    light_sequence_test(1)
                elif conditionState == 2:
                    # light_sequence(4)
                    light_sequence_test(4)
                elif conditionState == 3:
                    # light_sequence(1)
                    light_sequence_test(1)
                
                time.sleep(service.pollingFrequency)

                print(f"polling loop cycle time : {get_current_time() - pollingLoopStartTime}")

        except KeyboardInterrupt:
            print("Polling loop terminated")

    elif mode == 2:

        try:
            print("Data Observation mode")
            while True:
                print(f"Sensor 1 input : {input.InputSubSystem(1)}")
                print(f"Button input : {input.InputSubSystem(2)}")
                
                time.sleep(service.pollingFrequency)
        
        except KeyboardInterrupt:
            print("")
            print("Data Observation mode terminated.")




def light_sequence(startStage):
    if startStage == 1:

        initialTime0 = get_current_time()
        timeDifference0 = 0 
        while timeDifference0 <= 1.5:
            output.OutputSubSystem(0)
            timeDifference0 = get_current_time() - initialTime0
        
        initialTime = get_current_time()
        timeDiffrerence = 0 
        while timeDiffrerence <= 30.0:
            output.OutputSubSystem(startStage)
            timeDiffrerence = get_current_time() - initialTime

        initialTime2 = get_current_time()
        timeDifference2 = 0 
        while timeDifference2 <= 3:
            output.OutputSubSystem(startStage+1)
            timeDifference2 = get_current_time() - initialTime2


        initialTime3 = get_current_time()
        timeDifference3 = 0 
        while timeDifference3 <= 3:
            output.OutputSubSystem(startStage+2)
            timeDifference3 = get_current_time() - initialTime3

    elif startStage == 4:

        # implemented a seperate output sequnce to make sure there is a smooth transistion between the red lights to green lights
        initialTime0 = get_current_time()
        timeDifference0 = 0 
        while timeDifference0 <= 1.5:
            output.OutputSubSystem(3.5)
            timeDifference0 = get_current_time() - initialTime0 

        initialTime = get_current_time()
        timeDiffrerence = 0 
        while timeDiffrerence <= 30.0:
            output.OutputSubSystem(startStage)
            timeDiffrerence = get_current_time() - initialTime

        initialTime2 = get_current_time()
        timeDifference2 = 0 
        while timeDifference2 <= 3:
            output.OutputSubSystem(startStage+1)
            timeDifference2 = get_current_time() - initialTime2

        initialTime3 = get_current_time()
        timeDifference3 = 0 
        while timeDifference3 <= 3:
            output.OutputSubSystem(startStage+2)
            timeDifference3 = get_current_time() - initialTime3
    
    elif startStage == 0:

        initialTime = get_current_time()
        timeDiffrerence = 0 
        while timeDiffrerence <= 30.0:
            output.OutputSubSystem(startStage+1)
            timeDiffrerence = get_current_time() - initialTime

        initialTime2 = get_current_time()
        timeDifference2 = 0 
        while timeDifference2 <= 3:
            output.OutputSubSystem(startStage+2)
            timeDifference2 = get_current_time() - initialTime2


        initialTime3 = get_current_time()
        timeDifference3 = 0 
        while timeDifference3 <= 3:
            output.OutputSubSystem(startStage+3)
            timeDifference3 = get_current_time() - initialTime3


# used to store the number of times condition 1 and condition 2 are run and change the task run accordingly
conditionState1Count = 0
conditionState2Count = 0

def check_conditions(buttonInput, SensorInput,mode):
    if mode == "t":
        global conditionState1Count 
        global conditionState2Count 
        # these assigments are just test assignemnet proper conditions should be implemented in the future under the else section
        if buttonInput >= 3 and SensorInput >= 100:
            if conditionState2Count <= 1:
                conditionState = 2
                conditionState2Count += 1
            else:
                conditionState = 1
                conditionState2Count = 0
            
        elif buttonInput <= 3 and SensorInput <= 50:
            if conditionState1Count <= 2:
                conditionState == 1
                conditionState1Count += 1
            else:
                conditionState == 2
                conditionState1Count = 0
    
        return conditionState
    else:
        print("actual conditions to be implemented")



def get_current_time():
    return time.time()



# Test light sequence function that doesnt require 30 seconds of printing similar to the main function
def light_sequence_test(startStage):
    print("one print here is considered to be equivalent to 1 second")
    if startStage == 1:
        output.OutputSubSystem(0)
        output.OutputSubSystem(startStage)
        output.OutputSubSystem(startStage+1)
        output.OutputSubSystem(startStage+2)
    if startStage == 4:
        output.OutputSubSystem(3.5)
        output.OutputSubSystem(startStage)
        output.OutputSubSystem(startStage+1)
        output.OutputSubSystem(startStage+2)
    if startStage == 0:
        output.OutputSubSystem(startStage+1)
        output.OutputSubSystem(startStage+2)
        output.OutputSubSystem(startStage+3)


           
