import string 
import secrets
import sys
import os
import gnupg
import getpass
import sqlite3
from tabulate import tabulate

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
                error_text = "The input must be a number from 8 to 100."

            print(f"Input error: {error_text}")
            print(" ")

    return length

def get_user_data():
    service = input("Enter the name of the service: ")
    user_name = input("Enter the username/email address: ")

    password_1 = "1"
    password_2 = "2"

    while password_1 != password_2:
        password_1 = getpass.getpass("Enter the password: ")
        password_2 = getpass.getpass("Enter the password again: ")
        print("")

        if (password_1 != password_2):
            print("The password you just entered does not match the first one you entered.")

    password_2 = ""
    encrypted_password = encrypt_password(password_1)
    insert_in_sql_table(service, user_name, encrypted_password)

def encrypt_password(password):
    gpg = gnupg.GPG(gnupghome = os.path.expanduser('~/.gnupg'))
    gpg.encoding = 'utf-8'

    encrypted_password = gpg.encrypt(password, symmetric=True, recipients = 'alice@gmail.com', passphrase='your-password')

    return encrypted_password

def insert_in_sql_table(service, username, password):
    connection, cursor = establish_sql_connection()

    command_1 = """CREATE TABLE IF NOT EXISTS
    user_data(Service TEXT, Username TEXT, Password TEXT, PRIMARY KEY (Service, Username))"""

    command_2 =  "INSERT INTO user_data (Service, Username, Password) VALUES (?, ?, ?)"

    cursor.execute(command_1)
    connection.commit()
    cursor.execute(command_2, (service, username, str(password)))
    connection.commit()

    connection.close()


def extract_from_sql_table():
    connection, cursor = establish_sql_connection()
    results_number = 0

    while results_number == 0:
        service = input("Enter the name of the service for which you want to receive the password: ")

        cursor.execute("SELECT 1 FROM user_data WHERE Service = ? LIMIT 1", (service,))

        results = cursor.fetchall()
        results_number = len(results)

        if results_number == 0:
            print("There does not exist any service with this name within the database. Try again.")


    cursor.execute("SELECT * FROM user_data WHERE Service = ?", (service,))
    new_results = len(cursor.fetchall())

    print("The query has found the following results")
    print(" ")

    cursor.execute("SELECT Service, Username FROM user_data WHERE Service = ?", (service,))
    results_2 = cursor.fetchall()

    query_df = {'Service': [x[0] for x in results_2], 'Username': [x[1] for x in results_2]}

    print(
        tabulate(
            query_df,
            headers = 'keys',
            floatfmt = ".5f",
            showindex = True,
            tablefmt = "psql",
        )
    )

    print("")
    pw_index = ''

    while (not isinstance(pw_index, int)) or pw_index >= len(results_2) or pw_index < 0:
        try:
            pw_index = ""
            pw_index = int(input("Please select the index of the row denoting correct combination of service and username: "))

            if pw_index < 0:
                raise ValueError("Provided integer is too small.")
            if pw_index >= len(results_2):
                raise ValueError("Provided integer is too large.")
            
            break
        except ValueError as e:
            error_text = ""

            if isinstance(pw_index, int):
                if pw_index < 0:
                    error_text = f"Provided integer is too small."
                elif pw_index >= len(results_2):
                    error_text = f"Provided integer is too large."
            else:
                error_text = f"The input must be a value from 0 to {len(results_2) - 1}."

            print(f"Input error: {error_text}")
            print(" ")

    connection.close()

def create_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        if password[0] != '=':
            break

    return password

def establish_sql_connection():
    connection = sqlite3.connect("p_gen_tool.db")
    cursor = connection.cursor()

    return connection, cursor