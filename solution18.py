'''
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

Following are the criteria for checking the password:

At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

Example

If the following passwords are given as input to the program:

ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:

ABd1234@1

'''

'''
As the characters/digits can be anywhere within the string, we require lookaheads. Lookaheads are of zero width meaning they do not consume any string. In simple words the position of checking resets to the original position after each condition of lookahead is met
'''
import re

passwords = input("Provide list of passwords you want to verify-\n")

pattern = "^(?=.{6,12}$)(?=.+[a-z])(?=.+[0-9])(?=.+[A-Z])(?=.+[$#@]).*$"

password_list = passwords.split(",")

valid_passwords = []

for password in password_list:
    if re.search(pattern, password):
        valid_passwords.append(password)

print(",".join(valid_passwords))
