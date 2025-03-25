# inet_4031_adduser_script
# This is an automation user management program

# Program Description
This Python program automates the process of adding new users. Instead of using the command line to run commands such as adduser, passwd, sudo, etc, the program automates that and makes it easier and friendly for people to create user accounts.

# Program User Operation
This is a automation python program that creats user accounts. It reads user information from and input file line by line to extract details such as the username, password, last name, first name, and group.

# Input File Format
In the input file, in each line, there are semicolons (:) that act as separators and for each input before the semicolon they are fields. Putting a # (comment) will skip a line. If you do not want a user to be added to any group, add a - or leave it empty to indicate it as not wanting it to be added.

# Command execution
To run the code: 
./create-users.py < create-users.input
or
sudo python3 create-users.py < create-users.input

# Dry Run
