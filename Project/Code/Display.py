import ServicesSubSystem as service
import time as time
import numpy as np


lookupDictionary = {
    "0": "01111110",
    "1": "00110000",
    "2": "01101101",
    "3": "01111001",
    "4": "00110011",
    "5": "01011011",
    "6": "01011111",
    "7": "01110000",
    "8": "01111111",
    "9": "01111011",
    "N": "00000000",

    "A": "01110111",
    "B": "01111111",
    "C": "01001110",
    "D": "01111110",
    "E": "01001111",
    "F": "01000111",
    "G": "01101111",
    "U": "00111110",

    "g": "01111011",
    "o": "00011101",
    "r": "00000101",
    "t": "00001111",
    "y": "00111011",
    "n": "00010101",
    "h": "00010111",
    "i": "00010000",

    "=": "00001001"
}

select_segment1 = {
    "1" : "01110000",
    "2" : "10110000",
    "3" : "11010000",
    "4" : "11100000"
}

select_segment2 = {
    "1" : "00000111",
    "2" : "00001011",
    "3" : "00001101",
    "4" : "00001110"
}

ser = 7
rclk = 8
srclk = 9

board = service.board

def display(string,mode,displayNumber = 1):

    """
        Function is used to display Alphanumeric characters to necessary locations
        Parameters : string of type string that contains the chain of characters that are to be displayed
    """
    initialize_display_pins()
    startTime = time.time()
    currentTime = time.time()
    starter = True
    displayList = initialize_display_list(string)

    innerDisplayTime = 0.90
    if mode == 1:
        displayTime = 2
    elif mode == 2:
        displayTime = 8
    elif mode == 3:
        displayTime = 2


    if mode != 3:
        while currentTime - startTime <= displayTime:

            if starter == True:
                starter = False
            else:
                if displayNumber == 1:
                    displayList = roll_display_list(displayList)

            chosen_elements = currently_displayed_elements(string, displayList)

            innerStart = time.time()
            innerCurrent = time.time()
            while innerCurrent - innerStart <= innerDisplayTime:
                for i in range(len(chosen_elements)):
                    bits = get_bits_to_be_written(chosen_elements[i], (i + 1), displayNumber)
                    reset_shift_register()
                    write_to_shift(bits)

                innerCurrent = time.time()

            currentTime = time.time()
    else:
        chosen_elements = currently_displayed_elements(string, displayList)
        for i in range(len(chosen_elements)):
            bits = get_bits_to_be_written(chosen_elements[i], (i + 1), displayNumber)
            reset_shift_register()
            write_to_shift(bits)
        reset_shift_register()


def initialize_display_list(displayedCharacters):
    arrayLength = len(displayedCharacters)
    displayedCharacters = []
    if arrayLength > 4:
        for i in range(1, 5):
            displayedCharacters.append(i)

        remainingIndexes = arrayLength - 4
        for j in range(remainingIndexes):
            displayedCharacters.append(0)

    else:
        for i in range(1, (arrayLength + 1)):
            displayedCharacters.append(i)

    displayedCharacters = np.array(displayedCharacters)
    return displayedCharacters


def roll_display_list(displayList):
    displayList = np.roll(displayList, 1, axis=0)
    return displayList


def currently_displayed_elements(displayedCharacters, displayList):
    firstLetter = displayedCharacters[np.where(displayList == 1)[0][0]]
    secondLetter = displayedCharacters[np.where(displayList == 2)[0][0]]
    thirdLetter = displayedCharacters[np.where(displayList == 3)[0][0]]
    fourthLetter = displayedCharacters[np.where(displayList == 4)[0][0]]
    lettersDisplayed = firstLetter + secondLetter + thirdLetter + fourthLetter
    return lettersDisplayed


def get_bits_to_be_written(displayElement, index, displayNumber):
    if displayElement == "z":
        elemenetBit = lookupDictionary["N"]
    else:
        elemenetBit = lookupDictionary[str(displayElement)]

    if displayNumber == 1:
        segmentBit = select_segment1[str(index)]
        finalBit = elemenetBit + segmentBit + lookupDictionary["N"]
    elif displayNumber == 2:
        segmentBit = select_segment2[str(index)]
        finalBit = lookupDictionary["N"] + segmentBit + elemenetBit



    finalBitReversed = finalBit[::-1]
    return finalBitReversed


def reset_shift_register():
    global ser, rclk, srclk

    board.digital_pin_write(rclk, 1)
    board.digital_pin_write(rclk, 0)


def write_to_shift(bits):
    global ser, rclk, srclk

    for i in bits:
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


def initialize_display_pins():

    """
        Function initialises pin numbers and specifies the function of each pin
    """

    global ser, rclk, srclk

    board.set_pin_mode_digital_output(ser)
    board.set_pin_mode_digital_output(rclk)
    board.set_pin_mode_digital_output(srclk)



def turn_off_display():
    """
        Function is used to clear all elements being displayed.
    """

    display("zzzz", 1)

