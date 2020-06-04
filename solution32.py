'''
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

'''


def printDictKeys():
    my_dict = {number: number**2 for number in range(1, 21)}
    print(my_dict.keys())

printDictKeys()
