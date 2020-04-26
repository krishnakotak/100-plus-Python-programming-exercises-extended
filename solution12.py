'''
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line
'''

my_list=[]
for num in range(1000,3001):
	add_number=True
	for letter in str(num):
		if(int(letter)%2!=0):
			add_number=False
			break
	if add_number:
		my_list.append(str(num))

print(','.join(my_list))

# def check(item):
# 	return all(int(letter)%2==0 for letter in item)

# my_list=[str(num) for num in range(1000,3001)]
# print(','.join(list(filter(check,my_list))))

# my_list=[str(num) for num in range(1000,3001)]
# print(','.join(list(filter(lambda item: all(int(letter)%2==0 for letter in item),my_list))))





