# Password Management CLI Tool

A command-line password manager using GPG encryption for secure local storage. This is a prototype project done strictly for educational purposes, and should not be used in production.

The program uses a Python backend, in combination with SQLite, utilized for password storage.

## Usage

After installation, the Password Management Tool can be used from the terminal by running the following command:

`pgen --mode x`

where x is a whole number in the interval [1, 3].

Alternatively, the user can input `pgen` in order to get a guide instructing them about the usage of the command. This aspect has been documented in detail in the following section.

## Use Cases

The program has 3 main modes:

1. **Password generation** - this mode allows the user to generate a secure password. The user is first prompted to choose a number from 8 to 100. Afterwards, the program generates a password with a length based on the number which was input.

   If the input happens to not satisfy the mentioned criteria, the program throws an error and continues to ask for input. An example of this usage is shown below.

   <img width="3497" height="2118" alt="image" src="https://github.com/user-attachments/assets/b38fe1e1-f706-49ce-a1b1-5f9e062f4729" />


3. **Password storage** - this mode allows the user to store the login information to a variety of services. The user will be prompted, in order, to provide the name of the service, the username and the password. After the password is encrypted, all the data is stored in a SQLite database. At this stage, the password input is hidden, as to not display it in the terminal. 
  
   In this database, the main key is represented by the tuple (Service, Username).

   <img width="3516" height="2109" alt="image" src="https://github.com/user-attachments/assets/847565d1-5fce-453b-a9e9-798a34e4fc68" />


5. **Password retrieval** - this mode allows the user to retrieve password information from the database. At first, the program will ask the user to input the name of the service of which they are interested. Afterwards, if there are multiple entries of the same service, the program will ask the user to choose which one they want to retrieve.

   The program will prompt the user to input the master password. After the input has been validated, the program will copy the decrypted password to the user's clipboard.
