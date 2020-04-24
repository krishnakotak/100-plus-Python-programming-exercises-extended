'''
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:

without,hello,bag,world
Then, the output should be:

bag,hello,without,world
'''

args = input()
lst = args.split(',')
print(','.join(sorted(lst)))

# sort vs sorted
# The primary difference between the list sort() function and the sorted() function is that the sort() function will modify the list it is called on. The sorted() function will create a new list containing a sorted version of the list it is given

