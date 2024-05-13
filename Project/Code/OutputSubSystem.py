# Function that handles all the outputs necessary system-wide. Mainly handles the sequential lightnings
# ENG-1013 - Project - A21
# Created By : Varon Nethan Rasiah 
# Created Date: 22/03/2024
# version ='1.0'
import ServicesSubSystem as service

board = service.board

ser = 2
rclk = 3
srclk = 4

stages = {
    "0": "00000000",
    "1": "00110010",
    "2": "01010010",
    "3": "10010010",
    "4": "10000101",
    "5": "10001001",
    "6": "10010010"
}


def output_sub_system(startStage):
    """
        Function that's controls the outputs as a whole. This also includes the light sequences.
        A single parameter is taken in named startStage that takes in what stage of the light sequence needs to be output
    """

    global board
    initialize_board()
    reset_shift()
    sequence = stages[str(startStage)]
    write_to_shift(sequence)


def write_to_shift(bit):
    """
        inverts bits taken in as a parameter and registers the data in the shift register for execution
        parameters : bit(string)
    """

    invert_bit = bit[::-1]
    for i in invert_bit:
        if i == '0':
            board.digital_pin_write(ser, 0)
            board.digital_pin_write(srclk, 1)
            board.digital_pin_write(srclk, 0)
        if i == '1':
            board.digital_pin_write(ser, 1)
            board.digital_pin_write(srclk, 1)
            board.digital_pin_write(srclk, 0)
    board.digital_pin_write(rclk, 1)
    board.digital_pin_write(rclk, 0)


def reset_shift():
    """
        Resets the bits stored in the shift register
        Parameters : None
    """
    board.digital_pin_write(rclk, 1)
    board.digital_pin_write(rclk, 0)


def initialize_board():
    """
        This function is used to initialize the board and the relevant pins necessary for the light sequence
        Parameters: None
    """
    global ser, rclk, srclk
    board.set_pin_mode_digital_output(ser)
    board.set_pin_mode_digital_output(rclk)
    board.set_pin_mode_digital_output(srclk)

