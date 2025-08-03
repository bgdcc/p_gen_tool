import string 
import secrets
import sys
import os
import gnupg
import getpass
import sqlite3

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

def get_user_data():
    service = input("Enter the name of the service: ")
    user_name = input("Enter the username: ")
    email_address = input("Enter the email address: ")

    password_1 = "1"
    password_2 = "2"

    while password_1 != password_2:
        password_1 = getpass.getpass("Enter the password: ")
        password_2 = getpass.getpass("Enter the password again: ")
        print("")

        if (password_1 != password_2):
            print("The password you entered does not match the first one you entered.")

    password_2 = ""
    encrypted_password = encrypt_password(password_1)
    insert_in_sql_table(service, user_name, email_address, encrypted_password)

def encrypt_password(password):
    gpg = gnupg.GPG(gnupghome = os.path.expanduser('~/.gnupg'))
    gpg.encoding = 'utf-8'

    encrypted_password = gpg.encrypt(password, symmetric=True, recipients = 'alice@gmail.com', passphrase='your-password')

    return encrypted_password

def insert_in_sql_table(service, username, email_address, password):
    connection = sqlite3.connect("p_gen_tool.db")
    cursor = connection.cursor()

    command_1 = """CREATE TABLE IF NOT EXISTS
    user_data(Service TEXT, Username TEXT, Email TEXT, Password TEXT, PRIMARY KEY (Service, Email))"""

    command_2 =  "INSERT INTO user_data (Service, Username, Email, Password) VALUES (?, ?, ?, ?)"
    
    cursor.execute(command_1)
    cursor.execute(command_2, (service, username, email_address, str(password)))

def create_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        if password[0] != '=':
            break

    return password