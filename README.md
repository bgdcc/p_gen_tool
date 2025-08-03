# Password Management CLI Tool

A command-line password manager using GPG encryption for secure local storage. This is a prototype project done strictly for educational purposes, and should not be used in production.

The program uses a Python backend, in combination with SQLite, utilized for password storage.

## Use Cases

The program has 3 main modes:

1. Password generation - this mode allows the user to generate a secure password. The user is first prompted to choose a number from 8 to 100. Afterwards, the program generates a password with a length based on the number which was input.

   If the input happens to not satisfy the mentioned criteria, the program throws an error and continues to ask for input.

2. Password storage - this mode allows the user to store the login information to a variety of services. The user will be prompted, in order, to provide the name of the service, the username and the password. After the password is encrypted, all the data is stored in a SQLite database. At this stage, the password input is hidden, as to not display it in the terminal. 
  
   In this database, the main key is represented by the tuple (Service, Username).

3. Password retrieval - this mode allows the user to retrieve password information from the database. At first, the program will ask the user to input the name of the service of which they are interested. Afterwards, if there are multiple entries of the same service, the program will ask the user to choose which one they want to retrieve.

   The program will prompt the user to input the master password. 
