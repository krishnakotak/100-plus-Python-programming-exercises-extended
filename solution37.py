'''
Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).
'''


def printTuple():
    my_list = [number**2 for number in range(1, 21)]
    print(tuple(my_list))

printTuple()
