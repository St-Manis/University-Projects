import sys


# This is the function of the program.
def checkCard(number, type, option):
    counter = 0
    sum = 0

    # First we will check if the number is real. We reverse the number.
    for digit in str(number)[::-1]:
        # The first digit from the reversed number is our checksum.
        if counter == 0:
            checksum = int(digit)
        # Every even position, we multiply the digit by 2.
        elif (counter % 2) != 0:
            temp = int(digit) * 2
            # If the number that was created is more than one digit,
            # we add the digits to the sum.
            if len(str(temp)) > 1:
                for temp_digit in str(temp):
                    sum += int(temp_digit)
            # In every other case we simply add the digit to the sum.
            else:
                sum += temp
        else:
            sum += int(digit)
        counter += 1

    # If this equation is true then the credit card number is real. Otherwise
    # we return that the credit card number is fake without checking for the
    # type (if it was the option).
    if 10 - (sum % 10) == checksum:
        if option.lower() == 'number':
            return('The credit card number is real.')
        else:
            # Here is the code we implement if the option was to check the
            # type also.
            if option.lower() == 'both':

                real_type = ''
                counter = 0
                temp = []
                firstfourdigits = []

                # We create a list with the first four digits of the number.
                for digit in str(number):
                    temp.append(digit)

                for digit in temp:
                    digit = int(digit)
                    # First we check if the first digit is one of the legit
                    # ones.
                    if counter == 0 and (digit == 4 or digit == 3 or
                                         digit == 5 or digit == 6):
                        if digit == 4:
                            # Check if the length of the number matches the
                            # visa cards length.
                            if len(str(number)) == 13 or len(str(number)) == \
                               16:
                                real_type = 'visa'
                                break
                            else:
                                break
                        # If its not a visa, we add the digit to the
                        # firstfourdigits list that we will use to continue.
                        # We keep that logic to the rest of the loop also.
                        else:
                            firstfourdigits.append(digit)
                    elif counter == 1:
                        # If the elif is activated, we create the first two
                        # digits number and continue with the checking.
                        # We continue with this logic until the end of the
                        # loop.
                        firsttwodigits = int(str(firstfourdigits[0])
                                             + str(digit))

                        if firsttwodigits == 35:
                            if len(str(number)) == 15:
                                real_type = 'jcb'
                                break
                            else:
                                break
                        elif firsttwodigits == 37:
                            if len(str(number)) == 15:
                                real_type = 'amex'
                                break
                            else:
                                break
                        elif firsttwodigits == 36 or firsttwodigits == 38:
                            if len(str(number)) == 14:
                                real_type = 'diners'
                                break
                            else:
                                break
                        elif firsttwodigits == 65:
                            if len(str(number)) == 16:
                                real_type = 'discover'
                                break
                            else:
                                break
                        elif firsttwodigits in range(50, 56):
                            if len(str(number)) == 16:
                                real_type = 'mastercard'
                                break
                            else:
                                break
                        elif digit == 0:
                            firstfourdigits.append(digit)
                        else:
                            print('The credit card type doesnt exist.')
                            break
                    elif counter == 2:
                        firstthreedigits = int(str(firstfourdigits[0]) +
                                               str(firstfourdigits[1])
                                               + str(digit))

                        if firstthreedigits in range(299, 306):
                            if len(str(number)) == 14:
                                real_type = 'diners'
                                break
                            else:
                                break
                        elif firstfourdigits[0] == 6 and digit == 1:
                            firstfourdigits.append(digit)
                        else:
                            break
                    else:
                        fourdigits = int(str(firstfourdigits[0]) +
                                         str(firstfourdigits[1]) +
                                         str(firstfourdigits[2])
                                         + str(digit))

                        if fourdigits == 6011:
                            if len(str(number)) == 16:
                                real_type = 'discover'
                                break
                            else:
                                break
                        else:
                            break
                    counter += 1
                # Here we do our final check. If the type the user entered
                # matches the one that the loop produced, the credit card
                # is real.
                if type.lower() == real_type:
                    return('The credit card is real.')
                else:
                    return('The credit card is fake.')

    else:
        return('the number is fake')


print("*****************************************************************\n \
THIS IS A PROGAM THAT TAKES CREDIT CARD INFORMATION FROM THE USER AND \n\
 CHECKS IF THE CREDIT CARD IS REAL OR NOT.\n************************\
***************************************** \n")

option = input('Do you want to validate only the card number (number),\
 or its type also (both)?: ')

if option.lower() == 'exit':
    sys.exit()

while option.lower() not in ['number', 'both', 'exit']:
    option = input('Please enter a valid option: ')
    if option.lower() == 'exit':
        sys.exit()

# We format the number so that it doesnt contain whitespaces or lines
# if the user entered them.
number = input('Give the credit card number: ')
number = number.replace(' ', '')
number = number.replace('-', '')

# We check if the length of the number is real.
if len(number) not in [13, 14, 15, 16]:
    number = input('Invalid number, please try again: ')
    if type.lower() == 'exit':
        sys.exit()

if option.lower() == 'both':
    type = input('Please enter the credit card type: ')
    # We format the type input to the needs of the program.
    if type.lower() in ['amex', 'american express', 'americanexpress']:
        type = 'amex'
    elif type.lower() in ['diners', 'diners club', 'dinersclub']:
        type = 'diners'
    elif type.lower() in ['mastercard', 'master card']:
        type = 'mastercard'
    elif type.lower() not in ['visa', 'discover', 'jcb']:
        type = input('Invalid card type. Please try again: ')
        if type.lower() == 'exit':
            sys.exit()

msg = checkCard(number, type, option)
print(msg)
