# Function that holds the polling loop and all intermediary functionality
# ENG-1013 - Project - A21
# Created By : Varon Nethan Rasiah 
# Created Date: 22/03/2024
# version ='1.0'


import time as time
import InputSubSystem as inputSub
import OutputSubSystem as output
import ServicesSubSystem as service
import matplotlib.pyplot as plt

# light_sequence() parameters; 1 - start from start stage 1 and go on until stage 3; 4 - start from start stage 4 to stage 6

sensorInput = []
buttonInput = []
temps = []

def control_sub_system(mode):
    
    global sensorInput
    global buttonInput
    global temps
    """
        Function houses the main functionality of the control subsystem
        Takes in a parameter named mode that houses the mode.
    """

    if mode == 1:
        try:
            light_sequence(0) # <-- to be used in the real scenario where output should be maintained for prolonged periods of time
            # light_sequence_test(0) # <-- test function with similar functionaly is used, similar ones used below
            while True:

                pollingLoopStartTime = time.time()

                conditionState = check_conditions(sensorInput,buttonInput,"t")
                sensorInput = [] 
                buttonInput = []
                if conditionState == 1:
                    light_sequence(1)
                    # light_sequence_test(1)
                elif conditionState == 2:
                    light_sequence(4)
                    # light_sequence_test(4)
                elif conditionState == 3:
                    light_sequence(1)
                    # light_sequence_test(1)
                

                print(f"polling loop time : {get_current_time() - pollingLoopStartTime}\n")

        except KeyboardInterrupt:
            print("")
            for i in range(1,7):
                output.turn_off_sequnce(i)
            print("Polling loop terminated")

    elif mode == 2:

        try:
            while True:
                while True:
                    data_observation_mode_menu()
                    try:
                        selection = int(input("Enter selected data viewing mode --> "))
                        break
                    except ValueError:
                        print("Enter the numbers specified in the menu")
                    except KeyboardInterrupt:
                        print("Enter 4 to exit data observation mode")

                if selection == 1:
                    if len(inputSub.ultra_sonic_distance_input) >= round(20 / service.pollingFrequency):
                        distance = inputSub.ultra_sonic_distance_input
                        correspondingTime = inputSub.ultra_sonic_time_input
                        elementCount = round(20/service.pollingFrequency)
                        distancesLast20Seconds = distance[-elementCount:]
                        timeLast20Seconds = correspondingTime[-elementCount:]
                        formated_last20Seconds = format_times(timeLast20Seconds)
                        plt.ion()
                        plt.gca().cla()
                        plt.plot(formated_last20Seconds, distancesLast20Seconds)
                        plt.legend("Last 20 seconds")
                        plt.title("Distance against Time (last 20 seconds)")
                        plt.xlabel("Time is seconds")
                        plt.ylabel("Distances in cm")
                        plt.draw()
                        plt.savefig("/Users/varonrasiah/Documents/Moansh/ENG1013-Project/Project/plots/disp_plot.png")
                        plt.pause(0.001)

                        generate_averge_rate_of_change(distancesLast20Seconds, timeLast20Seconds)

                    else:
                        print("Insufficient data to generate graphs.")
                        service.display("Err")

                elif selection == 3:
                    if len(inputSub.temperature_readings) != 0:
                        temperature = inputSub.temperature_readings
                        times = format_times(inputSub.temp_time_readings)
                        plt.ion()
                        plt.gca().cla()
                        plt.plot(times, temperature)
                        plt.legend("Last run Normal operation")
                        plt.title("Temperature against Time ")
                        plt.xlabel("Time is seconds")
                        plt.ylabel("Temperature in celsius")
                        plt.draw()
                        plt.savefig("/Users/varonrasiah/Documents/Moansh/ENG1013-Project/Project/plots/temp_plot.png")
                        plt.pause(0.001)

                    else:
                        print("Insufficient data to generate graphs.")
                        service.display("Err")

                elif selection == 2:
                    if len(inputSub.ultra_sonic_distance_input) >= round(20 / service.pollingFrequency):
                        distance = inputSub.ultra_sonic_distance_input
                        correspondingTime = inputSub.ultra_sonic_time_input
                        elementCount = round(20/service.pollingFrequency)
                        distancesLast20Seconds = distance[-elementCount:]
                        timeLast20Seconds = correspondingTime[-elementCount:]
                        formated_last20Seconds = format_times(timeLast20Seconds)
                        velocityLast20Seconds = generate_averge_rate_of_change(distancesLast20Seconds, timeLast20Seconds, 2)
                        plt.ion()
                        plt.gca().cla()
                        plt.plot(formated_last20Seconds, velocityLast20Seconds)
                        plt.legend("Last 20 seconds")
                        plt.title("Velocity against Time (last 20 seconds)")
                        plt.xlabel("Time is seconds")
                        plt.ylabel("Velocity in cm/s")
                        plt.draw()
                        plt.savefig("/Users/varonrasiah/Documents/Moansh/ENG1013-Project/Project/plots/velocity_plot.png")
                        plt.pause(0.001)
                    else:
                        print("Insufficient data to generate graphs.")
                        service.display("Err")

                elif selection == 4:
                    break
        
        except KeyboardInterrupt:
            print("")
            print("Data Observation mode terminated.")




def light_sequence(startStage):

    """
        Controls how the whole lighting sequence with periodic sensor polls based on the polling rate set Stages of the light sequenes are implemented with the required time delay.
        Takes in 1 parameter named startStage of that holds the stage sequence this is an integer
    """

    if startStage == 1:

        # check for the start time of the sequence to check and append sensor polls within the output sequnces - has to be done for all the below implementations
        stageOneStartTime = get_current_time()
        
        print(f"Traffic light stage = {startStage}")
        initialTime = get_current_time()
        timeDiffrerence = 0 
        while timeDiffrerence <= 30.0:
            output.output_sub_system(startStage)
            if (round(get_current_time() - stageOneStartTime))% service.pollingFrequency == 0:
                poll_Sensors()
                print(f"Time after which sensors are polled after the start of stage 1 : {round(get_current_time() - stageOneStartTime,1)}\n")
            if (round(get_current_time() - stageOneStartTime))% 2 == 0:
                print_nearest_distance()
            timeDiffrerence = get_current_time() - initialTime
        output.turn_off_sequnce(startStage)

        print(f"Traffic light stage = {startStage+1}")
        initialTime2 = get_current_time()
        timeDifference2 = 0 
        while timeDifference2 <= 3:
            output.output_sub_system(startStage+1)
            if (round(get_current_time() - stageOneStartTime))% service.pollingFrequency == 0:
                poll_Sensors()
                print(f"Time after which sensors are polled after the start of stage 1 : {round(get_current_time() - stageOneStartTime,1)}\n")
            if (round(get_current_time() - stageOneStartTime))% 2 == 0:
                print_nearest_distance()
            timeDifference2 = get_current_time() - initialTime2
        output.turn_off_sequnce(startStage+1)

        
        total_number_presses()
        print(f"Traffic light stage = {startStage+2}")
        initialTime3 = get_current_time()
        timeDifference3 = 0 
        while timeDifference3 <= 3:
            output.output_sub_system(startStage+2)
            if (round(get_current_time() - stageOneStartTime))% service.pollingFrequency == 0:
                poll_Sensors()
                print(f"Time after which sensors are polled after the start of stage 1 : {round(get_current_time() - stageOneStartTime,1)}\n")
            if (round(get_current_time() - stageOneStartTime))% 2 == 0:
                print_nearest_distance()
            timeDifference3 = get_current_time() - initialTime3
        output.turn_off_sequnce(startStage+2)

    elif startStage == 4:

        stageFourStartTime = get_current_time()

        print(f"Traffic light stage = {startStage}")
        initialTime = get_current_time()
        timeDiffrerence = 0 
        while timeDiffrerence <= 30.0:
            output.output_sub_system(startStage)
            if (round(get_current_time() - stageFourStartTime))% service.pollingFrequency == 0:
                poll_Sensors()
                print(f"Time after which sensors are polled after the start of stage 3 : {round(get_current_time() - stageFourStartTime,1)}\n")
            if (round(get_current_time() - stageFourStartTime))% 2 == 0:
                print_nearest_distance()
            timeDiffrerence = get_current_time() - initialTime
        output.turn_off_sequnce(startStage)

        print(f"Traffic light stage = {startStage+1}")
        initialTime2 = get_current_time()
        timeDifference2 = 0 
        while timeDifference2 <= 3:
            output.output_sub_system(startStage+1)
            if (round(get_current_time() - stageFourStartTime))% service.pollingFrequency == 0:
                poll_Sensors()
                print(f"Time after which sensors are polled after the start of stage 3 : {round(get_current_time() - stageFourStartTime,1)}\n")
            if (round(get_current_time() - stageFourStartTime))% 2 == 0:
                print_nearest_distance()
            timeDifference2 = get_current_time() - initialTime2
        output.turn_off_sequnce(startStage+1)

        print(f"Traffic light stage = {startStage+2}")
        initialTime3 = get_current_time()
        timeDifference3 = 0 
        while timeDifference3 <= 3:
            output.output_sub_system(startStage+2)
            if (round(get_current_time() - stageFourStartTime))% service.pollingFrequency == 0:
                poll_Sensors()
                print(f"Time after which sensors are polled after the start of stage 1 : {round(get_current_time() - stageFourStartTime,1)}\n")
            if (round(get_current_time() - stageFourStartTime))% 2 == 0:
                print_nearest_distance()
            timeDifference3 = get_current_time() - initialTime3
        output.turn_off_sequnce(startStage+2)
    
    elif startStage == 0:

        stageZeroStartTime = get_current_time()

        print(f"Traffic light stage = {startStage+1}")
        initialTime = get_current_time()
        timeDiffrerence = 0 
        while timeDiffrerence <= 30.0:
            output.output_sub_system(startStage+1)
            if (round(get_current_time() - stageZeroStartTime))% service.pollingFrequency == 0:
                poll_Sensors()
                print(f"Time after which sensors are polled after the start of stage 1 : {round(get_current_time() - stageZeroStartTime,1)}\n")
            if (round(get_current_time() - stageZeroStartTime))% 2 == 0:
                print_nearest_distance()
            timeDiffrerence = get_current_time() - initialTime
        output.turn_off_sequnce(startStage+1)

        print(f"Traffic light stage = {startStage+2}")
        initialTime2 = get_current_time()
        timeDifference2 = 0 
        while timeDifference2 <= 3:
            output.output_sub_system(startStage+2)
            if (round(get_current_time() - stageZeroStartTime))% service.pollingFrequency == 0:
                poll_Sensors()
                print(f"Time after which sensors are polled after the start of stage 1 : {round(get_current_time() - stageZeroStartTime,1)}\n")
            if (round(get_current_time() - stageZeroStartTime))% 2 == 0:
                print_nearest_distance()
            timeDifference2 = get_current_time() - initialTime2
        output.turn_off_sequnce(startStage+2)

        print(f"Traffic light stage = {startStage+3}")
        initialTime3 = get_current_time()
        timeDifference3 = 0 
        while timeDifference3 <= 3:
            output.output_sub_system(startStage+3)
            if (round(get_current_time() - stageZeroStartTime))% service.pollingFrequency == 0:
                poll_Sensors()
                print(f"Time after which sensors are polled after the start of stage 1 : {round(get_current_time() - stageZeroStartTime,1)}\n")
            if (round(get_current_time() - stageZeroStartTime))% 2 == 0:
                print_nearest_distance()
            timeDifference3 = get_current_time() - initialTime3
        output.turn_off_sequnce(startStage+3)






# used to store the number of times condition 1 and condition 2 are run and change the task run accordingly
conditionState1Count = 1
conditionState2Count = 1

def check_conditions(buttonInput, SensorInput,mode):

    """
        Function checks the conditions based on the sensor 
        3 parameters are taken in named buttonInput, sensorInput and mode. Of type list, list and string correspondingly
        mode is used to put the check conditions in to a test stage or non-functional stage
    """
    global conditionState1Count 
    global conditionState2Count 

    if mode == "t":

        if conditionState1Count%2 == 1:
            conditionState1Count += 1
            return 1
        else:
            conditionState1Count += 1
            return 2
        
        


    # these assigments are just test assignemnet proper conditions should be implemented in the future under the else section
    elif mode == "n":
        if buttonInput >= 3 and SensorInput >= 100:
            if conditionState2Count <= 1:
                conditionState = 2
                conditionState2Count += 1
            else:
                conditionState = 1
                conditionState2Count = 0
            
        elif buttonInput <= 3 and SensorInput <= 50:
            if conditionState1Count <= 2:
                conditionState = 1
                conditionState1Count += 1
            else:
                conditionState = 2
                conditionState1Count = 0
    
        return conditionState
        



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
        output.output_sub_system(0)
        print("runs for 3 seconds")
        print("")

        output.output_sub_system(startStage)
        print("runs for 30 seconds")
        print("")

        output.output_sub_system(startStage+1)
        print("runs for 3 seconds")
        print("")

        output.output_sub_system(startStage+2)
        print("runs for 3 seconds")
        print("")

    if startStage == 4:
        output.output_sub_system(3.5)
        print("runs for 3 seconds")
        print("")

        output.output_sub_system(startStage)
        print("runs for 30 seconds")
        print("")

        output.output_sub_system(startStage+1)
        print("runs for 3 seconds")
        print("")

        output.output_sub_system(startStage+2)
        print("runs for 3 seconds")
        print("")


    if startStage == 0:
        output.output_sub_system(startStage+1)
        print("runs for 30 seconds")
        print("")

        output.output_sub_system(startStage+2)
        print("runs for 3 seconds")
        print("")

        output.output_sub_system(startStage+3)
        print("runs for 3 seconds")
        print("")

           
def poll_Sensors():

    """
        Function that's polls the sensor and updates the lists.
        No parameters taken in
    """

    global sensorInput 
    global buttonInput
    global temps
    sensorInput.append(inputSub.input_sub_system(2))
    buttonInput.append(inputSub.input_sub_system(1))
    temps.append(inputSub.input_sub_system(3))




def print_nearest_distance():

    """
        Function prints to the console the distance to the nearest vehicle on demand
        Parameters : None
    """
    global sensorInput

    minDistance = sensorInput[-1]

    print(f"Distance to the nearest vehicle {round(minDistance,2)}")



def total_number_presses():
    """
        displays the number of button presses at the current state
    """
    global buttonInput

    print(f"Number of button presses : {buttonInput.count(0)}")


def generate_averge_rate_of_change(distance,time,mode = 1):
    velocityList = []
    for i in range(len(time)):
        velocityList.append(distance(i)/time(i))

    if mode == 1:
        averageVelocity = sum(velocityList)/len(velocityList)
        print(f"Average velocity over the last 20 seconds is {round(averageVelocity,2)} ms^-1")
    elif mode == 2:
        return velocityList


def data_observation_mode_menu():

    """
        Function that prints in the formatted data_observation menu
        No parameters taken in
    """

    print()
    print("================================================================================")
    print("=========================== Data_Observation_Mode ==============================")
    print("================================================================================")
    print()
    print("Modes Available --> ")
    print()
    print("       1 : Distance against Time for the last 20 seconds of the polling loop")
    print("       2 : Velocity against Time for the last 20 seconds of the polling loop")
    print("       3 : Temperature against time throughout the whole run")
    print("       4 : Exit data observation mode")
    print()
    print("================================================================================")
    print("================================================================================")


def format_times(time):
    formattedTime = [0]
    for i in range(1, len(time)):
        timeDiff = time[i]-time[0]
        formattedTime.append(timeDiff)

    return formattedTime










