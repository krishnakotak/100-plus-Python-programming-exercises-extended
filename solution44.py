'''
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
'''
lst = range(1, 21)
print(list(map((lambda x: x**2), lst)))
