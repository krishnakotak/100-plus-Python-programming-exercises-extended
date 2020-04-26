'''
Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320
'''

import sys

number = int(input('Type the number you want to calculate factorial of : '))

factorial = 1
while number > 0:
	factorial *= number
	number = number - 1
print(factorial)
