'''
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''

class Simple:

	def getString(self):
		str = input("Please enter the string you want to print : ")
		self.str = str

	def printString(self):
		print(self.str)

def testSimple():
	obj = Simple()
	obj.getString()
	obj.printString()

testSimple()