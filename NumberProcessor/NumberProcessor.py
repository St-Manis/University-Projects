import sys


# This is the function of the program.
def numberProcessor(number):
    # Here we execute the required operations.
    number *= 3
    number += 1
    # We use an iterator which is basically our number in a string format
    # so that we can iterate through its digits and add them to the new_number
    # that we will return.
    iterator = str(number)
    new_number = 0

    # Here we add each of the numbers digits.
    for digit in iterator:
        new_number += int(digit)

    return(new_number)


print("*****************************************************************\n \
THIS IS A PYTHON PROGRAM THAT TAKES A NUMBER, MULTIPLIES IT BY 3\n\
 THEN ADDS 1 TO IT, AND ADDS THE DIGITS OF THE NUMBER.THIS IS\n REPEATED\
 UNTIL THE NUMBER GENERATED IS ONE DIGIT.\n************************\
***************************************** \n")

number = input('Enter the required number: ')

# Simple input checks. If the input in any case is exit, then the program is
# terminated. If its not, then it must be a number.
if number.lower() == 'exit':
    sys.exit()

while True:
    try:
        number = int(number)
        break
    except ValueError:
        number = input('Please, enter a number(or exit): ')
        if number.lower() == 'exit':
            sys.exit()

output = numberProcessor(number)

# Here we check if the number is finally 1 digit. If its not, then we call
# the numberProcessor function again, with the previously returned number.
# We do this until the number is 1 digit.
while len(str(output)) > 1:
    number = output
    output = numberProcessor(number)

print(output)
