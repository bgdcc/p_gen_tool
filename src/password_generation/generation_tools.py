import string 
import secrets
import sys

def warm_welcome():
    print("Welcome to Password Generation Tool! ")
    print("This is a simple tool for the creation of safe passwords.")

def get_length():
    length = ''

    while (not isinstance(length, int)):
        try:
            length = int(input("Input a length for your password: "))

            if length < 8:
                raise ValueError("Length must be equal to or greater than 8.")
            if length > 100:
                raise ValueError("Length must be equal to or smaller than 100.")
            
            break
        except ValueError as e:
            print("Input error.")

    return length

def create_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        if password[0] != '=':
            break

    return password

