'''
Define a class, which have a class parameter and have a same instance parameter.
'''


class Car:
    doors = 2

    def __init__(self, doors):
        self.doors = doors

myCar = Car(4)
print(myCar.doors)
