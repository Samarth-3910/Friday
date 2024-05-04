#to remove duplicates from string
input_string = input()

result_string = ""

for char in input_string:
    if char not in result_string:
        result_string += char

print(result_string)