str_input = input()
list_input = str_input.split()
my_list = [int(x) for x in list_input]

# max_num = max(my_list)
# print("Largest number in the list:",max_num)

largest_num = float('-inf')
for num in my_list:
    if num > largest_num:
        largest_num = num

print(largest_num)