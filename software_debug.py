"""
Author: Daniel Monzon
Version: version 12
Description: Lab 06: Software Debugging
Date: 03/07/23
"""


def print_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit ')
    print()


while True:
    print_menu()
    option = input('Please enter an option: ')
    if option == '1':
        password = (input('Please enter your password to encode: '))
        new_password = ""
        for digit in password:
            encoded_password = (int(digit) + 3)
            encoded_password %= 10
            encoded_password = str(encoded_password)
            new_password += encoded_password
        print('Your password has been encoded and stored!\n')
    elif option == '2':
        num = 0
        for digit in str(new_password):
            digit = int(digit)
            digit += 7
            digit %= 10
            num *= 10
            num += digit
        print(f"The encoded password is {new_password}, and the original password is {num}")
    elif option == '3':
        break
    else:
        print('Invalid option! Select an input option given.')

