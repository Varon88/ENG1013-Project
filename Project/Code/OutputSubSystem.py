# Function that handles all the outputs necessary system wide. Mainly handles the sequential lightings
# ENG-1013 - Project - A21
# Created By : Varon Nethan Rasiah 
# Created Date: 22/03/2024
# version ='1.0'
import ServicesSubSystem as service

board = service.board

MR = 13
MY = 12
MG = 11

SR = 10 
SY = 9 
SG = 8 

PR = 7 
PG = 6


def Output_Sub_System(startStage):

    """
        Function thats controls the outputs as a whole. This also includes the light sequenences.
        A single parameter is taken in named startStage that takes in what stage of the light sequnce needs to be output
    """

    global board
    initialize_board()

    if startStage == 1:
        # print lights for stage 1 and follow for all.
        board.digital_write(MG,1)
        board.digital_write(SR,1)
        board.digital_write(PR,1)
        # print(f"Traffic light stage = {startStage}")
        

    elif startStage == 2:
        board.digital_write(MY,1)
        board.digital_write(SR,1)
        board.digital_write(PR,1)
        # print(f"Traffic light stage = {startStage}")
    
    elif startStage == 3:
        board.digital_write(MR,1)
        board.digital_write(SR,1)
        board.digital_write(PR,1)
        # print(f"Traffic light stage = {startStage}")
    
    elif startStage == 4:
        board.digital_write(MR,1)
        board.digital_write(SG,1)
        board.digital_write(PG,1)
        print(f"Traffic light stage = {startStage}")

    elif startStage == 5:
        board.digital_write(MR,1)
        board.digital_write(SY,1)
        board.digital_write(PG,1)
        print(f"Traffic light stage = {startStage}")
    
    elif startStage == 6:
        board.digital_write(MR,1)
        board.digital_write(SR,1)
        board.digital_write(PR,1)
        print(f"Traffic light stage = {startStage}")

    elif startStage == 0:
        print("Main Road Traffic Light --> yellow")
        print("Side Road Traffic Light --> Red")
        print("Pedestrian Lights --> Red")

    elif startStage == 3.5:
        print("Main Road Traffic Light --> Red")
        print("Side Road Traffic Light --> Yellow")
        print("Pedestrian Lights --> Yellow")       



def turn_off_sequnce(stage):
    """
        This function can be used to turn off relevant light stages 
        Parameters: startStage(int) - holds the start stage
    """
    global board
    initialize_board()

    if stage == 1:
        board.digital_write(MG,0)
        board.digital_write(SR,0)
        board.digital_write(PR,0)
            

    elif stage == 2:
        board.digital_write(MY,0)
        board.digital_write(SR,0)
        board.digital_write(PR,0)   
    
    elif stage == 3:
        board.digital_write(MR,0)
        board.digital_write(SR,0)
        board.digital_write(PR,0)
    
    elif stage == 4:
        board.digital_write(MR,0)
        board.digital_write(SG,0)
        board.digital_write(PG,0) 

    elif stage == 5:
        board.digital_write(MR,0)
        board.digital_write(SY,0)
        board.digital_write(PG,0)
    
    elif stage == 6:
        board.digital_write(MR,0)
        board.digital_write(SR,0)
        board.digital_write(PR,0)

def initialize_board():
    """
        This function is used to initialize the board and the relevant pins necessary for the light sequnce
        Parameters: None
    """
    global MR,MY,MG,SR,SY,SG,PR,PG


    board.set_pin_mode_digital_output(MR)
    board.set_pin_mode_digital_output(MY)
    board.set_pin_mode_digital_output(MG)
    board.set_pin_mode_digital_output(SR)
    board.set_pin_mode_digital_output(SY)
    board.set_pin_mode_digital_output(SG)
    board.set_pin_mode_digital_output(PR)
    board.set_pin_mode_digital_output(PG)



    