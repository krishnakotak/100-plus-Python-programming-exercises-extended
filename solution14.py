'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:

Hello world!
Then, the output should be:

UPPER CASE 1
LOWER CASE 9
'''

sentence = input("Please enter a sentence: ")
lowercase = [c for c in sentence if c.islower()]
print(f'LOWER CASE {len(lowercase)}')
uppercase = [c for c in sentence if c.isupper()]
print(f'UPPER CASE {len(uppercase)}')
