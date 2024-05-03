#str_input = input()
# if str_input in 'aeiouAEIOU':
#     print("VOWELS")
# else:
#     print("Consonats")

num_str = int(input())
strings = []

for i in range(num_str):
    strings.append(input())

for string in strings:
    vowels = 0
    consonants =0
    for char in string:
        if char in 'aeiouAEIOU':
            vowels += 1
        elif char.isalpha():
            consonants += 1
    print(vowels,consonants)