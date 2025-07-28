import string 
import secrets
import os

def get_password():
    alphabet = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(12))
        if password[0] != '=':
            break

    return password