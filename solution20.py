'''
Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use class, function and comprehension.

'''


class Generator:

    def divisibleBySeven(self, n):
        for i in range(n + 1):
            if i % 7 == 0:
                yield i


generator = Generator()
for i in generator.divisibleBySeven(int(input("please provide a number: "))):
    print(i)
