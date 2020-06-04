'''
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
'''


def printDictionary():

    my_dict = dict()
    for number in range(1, 21):
        my_dict[number] = number**2
    print(my_dict)

printDictionary()
