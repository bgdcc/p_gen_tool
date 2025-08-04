from typing_extensions import Annotated
import typer

from .generation_tools import get_length, create_password, warm_welcome, get_user_data, extract_from_sql_table

def get_password(mode: Annotated[str, typer.Option(help='The mode the user wants to choose')] = ""):
    try:
        if mode == "1":
            password_length = get_length()
            password = create_password(password_length)

            print("You generated the following password:")
            print(" ")
            print(password)
            print(" ")
        elif mode == "2":
            get_user_data()
        elif mode == "3":
            extract_from_sql_table()
        elif mode == "":
            warm_welcome()
            print("Correct usage: pgen --mode '$@'")
        else:
            print("Use the guide")
    except typer.click.exceptions.MissingParameter as e:
        print("Usage:")
        print("")
        print("A. pgen --mode x")
        print("")
        print("Use this option to use a specific mode of the application. 'x' should be a whole number in the interval [1, 3].")
        print("")
        print("B. pgen")
        print("")
        print("Use this option to conjure a guide on usage.")
