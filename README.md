# Password Management CLI Tool

A command-line password manager using GPG encryption for secure local storage. This is a prototype project done strictly for educational purposes, and should not be used in production. All passwords and/or email addresses which may appear in this document are used only for demonstration purposes and have no real usage.

The program uses a Python backend, in combination with SQLite, meant for storage of login information pertaining to multiple services.

## Usage

After installation, the Password Management Tool can be used from the terminal by running the following command:

`pgen --mode x`

where `x` is a whole number in the interval [1, 3].

Alternatively, the user can input `pgen` in order to get a guide instructing them about the usage of the command. This aspect has been documented in detail in the following section.

## Use Cases

The program has 3 main modes:

1. **Password generation** - this mode allows the user to generate a secure password. The user is first prompted to choose a number from 8 to 100. Afterwards, the program generates a password with a length based on the number which was input.

   If the input happens to not satisfy the mentioned criteria, the program throws an error and continues to ask for input. An example of this usage is shown below.

   <img width="963" height="776" alt="image" src="https://github.com/user-attachments/assets/b2e83256-620f-43c8-a075-c35898f0f907" />

2. **Password storage** - this mode allows the user to store the login information to a variety of services. The user will be prompted, in order, to provide the name of the service, the username and the password. After the password is encrypted, all the data is stored in a SQLite database. At this stage, the password input is hidden, as to not display it in the terminal. 
  
   In this database, the primary key is represented by the combination (Service, Username).

   <img width="1127" height="366" alt="image" src="https://github.com/user-attachments/assets/dca76ddd-8aea-46ec-b78e-06063fa9ea28" />

3. **Password retrieval** - this mode allows the user to retrieve password information from the database. At first, the program will ask the user to input the name of the service of which they are interested. Afterwards, if there are multiple entries of the same service, the program will ask the user to choose which one they want to retrieve.

   The program will prompt the user to input the master password. After the input has been validated, the program will copy the decrypted password to the user's clipboard.

   To properly demonstrate the capabilities of password retrieval, we will first introduce 2 accounts from the same service using the password storage mode (or mode 2).

   <img width="1100" height="517" alt="image" src="https://github.com/user-attachments/assets/838f0dbb-68ec-4ea6-89a7-3f222df771ef" />

## Conclusion

This project provided a huge amount of education value. It helped me gain hands-on experience with various cryptographic practices, such as symmetric encryption and secure hashing.

Furthermore, I was able to apply software design principles when building a Python project, while also learning more about SQL queries through the usage of the database engine SQLite.

WHile there is still room for improvement, this project gave me practical experience and helped me develop my understanding of key concepts.
