'''
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:

1,2,3,4,5,6,7,8,9
Then, the output should be:

1,9,25,49,81
'''

user_input = input()
input_list = user_input.split(',')

# output_list = []
# for item in input_list:
#     if int(item) % 2 != 0:
#         output_list.append(int(item) ** 2)
# print(output_list)

output_list = [str(int(item)**2) for item in input_list if int(item) % 2 != 0]
print(','.join(output_list))
