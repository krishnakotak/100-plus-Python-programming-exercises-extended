'''
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

hello world! 123
Then, the output should be:

LETTERS 10
DIGITS 3
'''
LETTERS=0
DIGITS=0

arg = input()
for alpha_num in arg:
	if alpha_num.isdigit():
		DIGITS+=1
	elif alpha_num.isalpha():
		LETTERS+=1

print(f'LETTERS {LETTERS}')
print(f'DIGITS {DIGITS}')

