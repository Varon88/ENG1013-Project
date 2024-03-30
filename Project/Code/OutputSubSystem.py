# Function that handles all the outputs necessary system wide. Mainly handles the sequential lightings
# ENG-1013 - Project - A21
# Created By : Varon Nethan Rasiah 
# Created Date: 22/03/2024
# version ='1.0'

def OutputSubSystem(startStage):

    if startStage == 1:
        # print lights for stage 1 and follow for all.
        print("Main Road Traffic Light --> Green")
        print("Side Road Traffic Light --> Red")
        print("Pedestrian Lights --> Red")

    elif startStage == 2:
        print("Main Road Traffic Light --> Yellow")
        print("Side Road Traffic Light --> Red")
        print("Pedestrian Lights --> Red")
    
    elif startStage == 3:
        print("Main Road Traffic Light --> Red")
        print("Side Road Traffic Light --> Red")
        print("Pedestrian Lights --> Red")
    
    elif startStage == 4:
        print("Main Road Traffic Light --> Red")
        print("Side Road Traffic Light --> Green")
        print("Pedestrian Lights --> Green")

    elif startStage == 5:
        print("Main Road Traffic Light --> Red")
        print("Side Road Traffic Light --> Yellow")
        print("Pedestrian Lights --> Flashing green")
    
    elif startStage == 6:
        print("Main Road Traffic Light --> Red")
        print("Side Road Traffic Light --> Red")
        print("Pedestrian Lights --> Red")

    elif startStage == 0:
        print("Main Road Traffic Light --> yellow")
        print("Side Road Traffic Light --> Red")
        print("Pedestrian Lights --> Red")

    elif startStage == 3.5:
        print("Main Road Traffic Light --> Red")
        print("Side Road Traffic Light --> Yellow")
        print("Pedestrian Lights --> Yellow")       







    