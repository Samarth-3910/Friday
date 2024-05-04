n = int(input())

binary = bin(n)[2:]
count_ones = 0

for digits in binary:
    if digits == '1':
        count_ones += 1

if count_ones % 2 == 0:
    print(f"{n} is an evil number")
else:
    print(f"{n} is not an evil number")





#     # Get a non-negative integer as input from the user
# n = int(input("Enter a non-negative integer: "))

# # Convert the number to its binary representation
# binary = bin(n)[2:]

# # Count the number of '1's in the binary representation
# count_ones = binary.count('1')

# # Check if the count of '1's is even to determine if the number is evil
# if count_ones % 2 == 0:
#     print(f"{n} is an evil number.")
# else:
#     print(f"{n} is not an evil number.")

