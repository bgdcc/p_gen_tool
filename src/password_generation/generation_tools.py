import string 
import secrets
import sys

def warm_welcome():
    print(" ")
    print("Welcome to Password Generation Tool! ")
    print(" ")

def get_length():
    warm_welcome()

    length = ''

    while (not isinstance(length, int)) or length < 8 or length > 100:
        try:
            length = ""
            length = int(input("Please input a length for your password: "))

            if length < 8:
                raise ValueError("Length must be equal to or greater than 8.")
            if length > 100:
                raise ValueError("Length must be equal to or smaller than 100.")
            
            break
        except ValueError as e:
            error_text = ""

            if isinstance(length, int):
                if length < 8:
                    error_text = f"The number {length} is smaller than 8."
                elif length > 100:
                    error_text = f"The number {length} is bigger than 100."
            else:
                error_text = "The input must be a number between 8 and 100."

            print(f"Input error: {error_text}")
            print(" ")

    return length

def create_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        if password[0] != '=':
            break

    return password

