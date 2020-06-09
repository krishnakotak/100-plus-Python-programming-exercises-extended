'''
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.
'''

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
mid_length = round(len(tup) / 2)
print(tup[0:mid_length])
print(tup[mid_length:])
