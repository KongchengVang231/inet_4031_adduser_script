#!/usr/bin/python3

# INET4031
# Kongcheng Vang
# 3/24/2025
# 3/24/2025

#import os for operating system interaction
#import re for regular expressions
#import sys for system-specific parameters and functions
import os
import re
import sys

def main():
    #Prompt user to select dry-run mode
    #upper case or lower case for yes or no does not matter hence the strip().lower()
    dry_run = input("Would you like to run in dry-run mode? (Y/N): ").strip().lower()

    #If the user does not pick y or picks n, user will be asked again
    if dry_run not in ['y', 'n']:
        print("Invalid input. Please enter 'Y' for dry-run or 'N' to run normally.")
        dry_run = input("Would you like to run in dry-run mode? (Y/N): ").strip().lower()

    #Iterate through each line in the input file
    for line in sys.stdin:
        #Check if line is a comment (starts with #)
        match = re.match("^#", line)

        #Split the line by : into fields
        fields = line.strip().split(':')

        #If a line is less than 5 fields or commented out, it will skip it
        if match or len(fields) != 5:
            if dry_run == 'y':
                print("==> Skipping line: Invalid field count or comment.")
            continue

        #Extract user information from fields
	#Consist of 5 fields
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])
        groups = fields[4].split(',')

        #This prints what would happen in dry-run mode
        if dry_run == 'y':
            print(f"==> Dry-run: Creating account for {username}...")
            print(f"==> Dry-run: Command: /usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}")
            print(f"==> Dry-run: Setting password for {username}...")
            print(f"==> Dry-run: Command: /bin/echo -ne '{password}\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}")
            for group in groups:
                if group != '-':
                    print(f"==> Dry-run: Assigning {username} to the {group} group...")
                    print(f"==> Dry-run: Command: /usr/sbin/adduser {username} {group}")
        else:
            #These are the commands to add the user and set their password
            print(f"==> Creating account for {username}...")
            cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
            os.system(cmd)

            print(f"==> Setting the password for {username}...")
            cmd = f"/bin/echo -ne '{password}\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"
            os.system(cmd)

	    #If the groups field is - (empty) they will not be assigned to a group
	    #If the groups field has an input and not - (empty) then it will prompt the user the group they are assigned to
            for group in groups:
                if group != '-':
                    print(f"==> Assigning {username} to the {group} group...")
                    cmd = f"/usr/sbin/adduser {username} {group}"
                    os.system(cmd)

if __name__ == '__main__':
    main()
