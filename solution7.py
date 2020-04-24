'''
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i * j.

Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5

Then, the output of the program should be:

[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
'''

import sys

#solution 1
x = int(sys.argv[1])
y = int(sys.argv[2])

two_dimension_array=[]

for i in range(x):
	inner_array=[]
	for j in range(y):
		inner_array.append(i*j)
	two_dimension_array.append(inner_array)

print(two_dimension_array)

#solution 2
# x,y = map(int,input().split(','))
# lst = [[(i*j) for j in range(y)] for i in range(x)]

# print(lst)
