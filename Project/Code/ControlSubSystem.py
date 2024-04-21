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

sensorInput = []
buttonInput = []

def Control_Sub_System(mode):
    
    """
        Function houses the main functionality of the control subsytem
        Takes in a parameter named mode that houses the mode.
    """

    if mode == 1:
        try:
            # light_sequence(0) -- to be used in the real scenario where output should be maintained for prolonged periods of time
            light_sequence_test(0) #test function with similar functionaly is used
            while True:

                pollingLoopStartTime = time.time()

                # this has to be re written with the modularized version in the actual implementation
                conditionState = check_conditions(sensorInput,buttonInput,"t")
                sensorInput = [] 
                buttonInput = []
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

                print(f"polling loop cycle time : {get_current_time() - pollingLoopStartTime}\n")

        except KeyboardInterrupt:
            print("")
            print("Polling loop terminated")

    elif mode == 2:

        try:
            print("Data Observation mode")
            while True:
                print(f"Sensor 1 input : {input.Input_Sub_System(1)}")
                print(f"Button input : {input.Input_Sub_System(2)}")
                
                time.sleep(service.pollingFrequency)
        
        except KeyboardInterrupt:
            print("")
            print("Data Observation mode terminated.")




"""
    Controls how the whole lighting sequence with periodic sensor polls based on the polling rate set
    Stages of the light sequenes are implemented with the required time delay.

"""
def light_sequence(startStage):

    """
        Function controls the light sequence stages
        Takes in 1 parameter named startStage of that holds the stage sequence this is an integer
    """

    if startStage == 1:

        # check for the start time of the sequence to check and append sensor polls within the output sequnces - has to be done for all the below implementations
        stageOneStartTime = get_current_time()

        initialTime0 = get_current_time()
        timeDifference0 = 0 
        while timeDifference0 <= 1.5:
            output.Output_Sub_System(0)
            timeDifference0 = get_current_time() - initialTime0
            if (stageOneStartTime - get_current_time())% service.pollingFrequency == 0:
                poll_Sensors()
        
        initialTime = get_current_time()
        timeDiffrerence = 0 
        while timeDiffrerence <= 30.0:
            output.Output_Sub_System(startStage)
            timeDiffrerence = get_current_time() - initialTime
            if (stageOneStartTime - get_current_time())% service.pollingFrequency == 0:
                poll_Sensors()

        initialTime2 = get_current_time()
        timeDifference2 = 0 
        while timeDifference2 <= 3:
            output.Output_Sub_System(startStage+1)
            timeDifference2 = get_current_time() - initialTime2
            if (stageOneStartTime - get_current_time())% service.pollingFrequency == 0:
                poll_Sensors()


        initialTime3 = get_current_time()
        timeDifference3 = 0 
        while timeDifference3 <= 3:
            output.Output_Sub_System(startStage+2)
            timeDifference3 = get_current_time() - initialTime3
            if (stageOneStartTime - get_current_time())% service.pollingFrequency == 0:
                poll_Sensors()

    elif startStage == 4:

        stageFourStartTime = get_current_time()

        # implemented a seperate output sequnce to make sure there is a smooth transistion between the red lights to green lights
        initialTime0 = get_current_time()
        timeDifference0 = 0 
        while timeDifference0 <= 1.5:
            output.Output_Sub_System(3.5)
            timeDifference0 = get_current_time() - initialTime0 
            if (stageFourStartTime - get_current_time())% service.pollingFrequency == 0:
                poll_Sensors()

        initialTime = get_current_time()
        timeDiffrerence = 0 
        while timeDiffrerence <= 30.0:
            output.Output_Sub_System(startStage)
            timeDiffrerence = get_current_time() - initialTime
            if (stageFourStartTime - get_current_time())% service.pollingFrequency == 0:
                poll_Sensors()

        initialTime2 = get_current_time()
        timeDifference2 = 0 
        while timeDifference2 <= 3:
            output.Output_Sub_System(startStage+1)
            timeDifference2 = get_current_time() - initialTime2
            if (stageFourStartTime - get_current_time())% service.pollingFrequency == 0:
                poll_Sensors()

        initialTime3 = get_current_time()
        timeDifference3 = 0 
        while timeDifference3 <= 3:
            output.Output_Sub_System(startStage+2)
            timeDifference3 = get_current_time() - initialTime3
            if (stageFourStartTime - get_current_time())% service.pollingFrequency == 0:
                poll_Sensors()
    
    elif startStage == 0:

        stageZeroStartTime = get_current_time()

        initialTime = get_current_time()
        timeDiffrerence = 0 
        while timeDiffrerence <= 30.0:
            output.Output_Sub_System(startStage+1)
            timeDiffrerence = get_current_time() - initialTime
            if (stageZeroStartTime - get_current_time())% service.pollingFrequency == 0:
                poll_Sensors()

        initialTime2 = get_current_time()
        timeDifference2 = 0 
        while timeDifference2 <= 3:
            output.Output_Sub_System(startStage+2)
            timeDifference2 = get_current_time() - initialTime2
            if (stageZeroStartTime - get_current_time())% service.pollingFrequency == 0:
                poll_Sensors()


        initialTime3 = get_current_time()
        timeDifference3 = 0 
        while timeDifference3 <= 3:
            output.Output_Sub_System(startStage+3)
            timeDifference3 = get_current_time() - initialTime3
            if (stageZeroStartTime - get_current_time())% service.pollingFrequency == 0:
                poll_Sensors()






# used to store the number of times condition 1 and condition 2 are run and change the task run accordingly
conditionState1Count = 0
conditionState2Count = 0

def check_conditions(buttonInput, SensorInput,mode):

    """
        Function checks the conditions based on the sensor 
        2 parameters are taken in named buttonInput and sensorInput. Both of type list
    """

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
    """
        Function that returns the current time
    """
    return time.time()



# Test light sequence function that doesnt require 30 seconds of printing similar to the main function
def light_sequence_test(startStage):

    """
        Function thats the exact same as the light_sequence just a shortened version for ease of functionality when printing outputs in the console
        Same parameters would be used
    """
    if startStage == 1:
        output.Output_Sub_System(0)
        print("runs for 3 seconds")
        print("")

        output.Output_Sub_System(startStage)
        print("runs for 30 seconds")
        print("")

        output.Output_Sub_System(startStage+1)
        print("runs for 3 seconds")
        print("")

        output.Output_Sub_System(startStage+2)
        print("runs for 3 seconds")
        print("")

    if startStage == 4:
        output.Output_Sub_System(3.5)
        print("runs for 3 seconds")
        print("")

        output.Output_Sub_System(startStage)
        print("runs for 30 seconds")
        print("")

        output.Output_Sub_System(startStage+1)
        print("runs for 3 seconds")
        print("")

        output.Output_Sub_System(startStage+2)
        print("runs for 3 seconds")
        print("")


    if startStage == 0:
        output.Output_Sub_System(startStage+1)
        print("runs for 30 seconds")
        print("")

        output.Output_Sub_System(startStage+2)
        print("runs for 3 seconds")
        print("")

        output.Output_Sub_System(startStage+3)
        print("runs for 3 seconds")
        print("")

           
def poll_Sensors():

    """
        Function thats polls the sensor and updates the lists.
        No parameters taken in
    """

    global sensorInput 
    global buttonInput
    sensorInput.append(input.Input_Sub_System(1)) 
    buttonInput.append(input.Input_Sub_System(2))