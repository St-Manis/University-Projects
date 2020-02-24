import pickle
import sys


# This is the function of the program. We take as inputs the pickled list
# and the number the user gave us.
def NumberChecker(number, numbers, option):
    numbers_output = []

    if option.lower() == 'digits':
        # We iterate through each value of the pickled numbers.
        for key in numbers:
            # We make the number iteratable by making it a string.
            iterator = str(number)
            counter = 0
            # For each digit in the 6 digit number, we check if it exists
            # in the pickled 4 digit number.
            for digit in iterator:
                if digit in str(key):
                    # If it does, we raise this counter by one.
                    counter += 1
            # If the condition is met and all 6 digits are present in the
            # 4 digit number then we add it to the output.
            if counter == 6:
                numbers_output.append(key)
        return(numbers_output)

    if option.lower() == 'whole':

        # We check if a 4 digit number is a subset of the 6 digit number.
        for key in numbers:
            if str(key) in str(number):
                # If it does, we add it to the output.
                numbers_output.append(key)

        return(numbers_output)


print("*****************************************************************\n \
THIS IS A 6 DIGIT NUMBER FROM THE USER AND SOME 4 DIGIT NUMBERS THAT \n\
 ARE PRESENT IN A FILE.THEN IT PRINTS OUT THE 4 DIGIT NUMBERS\n THAT HAVE\
 ALL THEIR DIGITS PRESENT IN THE USERS NUMBER.\n************************\
***************************************** \n")

# Here we load our pickled number list.
with open('pickle_data.pkl', 'rb') as pickle_file:
    numberlist = pickle.load(pickle_file)

number = input('Enter the number: ')
# Input requirements checking.
if number.lower() == 'exit':
    sys.exit()

while True:
    try:
        number = int(number)
        break
    except ValueError:
        number = input('Please enter a number: ')
        if number.lower() == 'exit':
            sys.exit()

while len(str(number)) != 6:
    number = input('The number needs to be 6 digits: ')
    while True:
        try:
            number = int(number)
            break
        except ValueError:
            number = input('Please enter a number: ')
            if number.lower() == 'exit':
                sys.exit()

msg = """Do you want the entire 4 digit number to be present in the
 6 digit number in the same specific format (whole), or only the digits
 to be present (digits)?: """
option = input(msg)

if option.lower() == 'exit':
    sys.exit()

while option.lower() not in ['whole', 'digits', 'exit']:
    option = input('Invalid option. Please try again: ')
    if option.lower() == 'exit':
        sys.exit()

numbers_output = NumberChecker(number, numberlist, option)

# We check if no number matched the requirements.
if len(numbers_output) == 0:
    print('No 4 digit number matched with the digits of the number you\
 entered!')
else:
    print('The numbers that matched the requirements are: '
          + str(numbers_output)[1:-1])
