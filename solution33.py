'''
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
'''


def printList():
    my_list = [number**2 for number in range(1, 21)]
    print(my_list)

printList()
