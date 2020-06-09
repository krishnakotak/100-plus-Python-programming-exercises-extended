'''
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".
'''

input_string = input()

if input_string == 'yes' or input_string == 'Yes' or input_string == 'YES':
    print("Yes")
else:
    print("No")
