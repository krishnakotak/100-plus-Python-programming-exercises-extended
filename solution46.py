'''
Define a class named American and its subclass NewYorker.
'''


class American:

    def __init__(self):
        print("American")


class NewYorker(American):

    def __init__(self):
        print("NewYorker")

american = American()
newYorker = NewYorker()

print(american)
print(newYorker)
