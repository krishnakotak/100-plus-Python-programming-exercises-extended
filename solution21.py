'''
Question:
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:

UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program:

UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:

2
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.Here distance indicates to euclidean distance.Import math module to use sqrt function.

'''
import math

x, y = 0, 0

while True:
    command = input("Give the command: \n").split()
    if not command:
        break
    direction, steps = command[0], int(command[1])
    if direction == 'UP':
        y += steps
    if direction == 'DOWN':
        y -= steps
    if direction == 'RIGHT':
        x += steps
    if direction == 'LEFT':
        x -= steps

distance = round(math.sqrt(x**2 + y**2))
print(distance)
