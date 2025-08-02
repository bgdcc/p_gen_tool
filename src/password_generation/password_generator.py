import string 
import secrets
import os
from typing_extensions import Annotated
import typer

from .generation_tools import get_length, create_password

# def get_password():
#     password_length = get_length()
#     password = create_password(password_length)

#     print("You generated the following password:")
#     print(" ")
#     print(password)
#     print(" ")

def get_password(mode: Annotated[str, typer.Option(help='The mode the user wants to choose')] = ""):
    if mode == "1":
        password_length = get_length()
        password = create_password(password_length)

        print("You generated the following password:")
        print(" ")
        print(password)
        print(" ")
    else:
        print("Use the guide")