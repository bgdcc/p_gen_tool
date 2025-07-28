import string 
import secrets
import os

from .generation_tools import get_length, create_password

def get_password():
    password_length = get_length()
    password = create_password(password_length)

    print(" ")
    print("You generated the following password:")
    print(" ")
    print(password)
    print(" ")