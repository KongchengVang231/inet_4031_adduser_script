#!/usr/bin/python3

# INET4031
# Kongcheng Vang
# 3/24/2025
# 3/24/2025

#import os for import operating system - allows for user interaction
#import re for import regular expressions - allows for pattern matching and text processing
#import sys for system - allows for system specific parameters and functions
import os
import re
import sys

def main():
    for line in sys.stdin:
	#This checks to see if a line is a comment hence the # character
	#Looking for a line that starts with # and it will equal the variable match
        match = re.match("^#",line)

        #This splits a line by : and acts as a seperator
        fields = line.strip().split(':')
 
        #This replicates user entry data to create a user, and has to not equal 5 fields
	#This checks if the length of the variables, match or fields is not equal to 5, the code continues to run
	#If the variables match and fields do have a length of 5 or is true, then the program will not continue with the next lines of code
 	#This if statement relies on the previous variables match and fields because if their line is equal to 5 the code will stop
        if match or len(fields) != 5:
            continue

        #variable fields is split up by : so in fields[0], that will be used for the username and after the : for fields[1], that will be set as the password and gecos formats fields 3 and 2 as the name of the user.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #This splits the fourth field by a , signifying the groups the user may be in
        groups = fields[4].split(',')

        #This shows that the users account is being created with their username they chose
        print("==> Creating account for %s..." % (username))
	#/usr/sbin/adduser is a command that adds a new user to the system, the users password is disabled and this specifies the users username
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #print cmd will print what cmd equals such as the fields of what gecos contains and the username
	#os.system(cmd) executes the command stored in cmd using the operating systems command line
        #print cmd
        os.system(cmd)

        #This prompts the user that their password is being created 
        print("==> Setting the password for %s..." % (username))
	#This executes and sets the password for the user. Echo repeats what it has been told such as getting the password of the user and dislays the visible output of the password for the user
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #print cmd will print what cmd and that is the password and username
	#os.system(cmd) executes the command stored in cmd using the operating systems command line
        #print cmd
        os.system(cmd)

        for group in groups:
	    #This if statement is looking for if the users group is assigned to a group. If the users group is assigned and not - (empty), it will run through the if statement.
	    #If the user is not assinged a group, they then will be assigned a group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()
