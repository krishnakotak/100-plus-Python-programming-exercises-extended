'''
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.
'''


def skipFirstFiveElementOfList():
    my_list = [number**2 for number in range(1, 21)]
    print(my_list[5:])

skipFirstFiveElementOfList()
