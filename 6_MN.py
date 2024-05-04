number = int(input("Enter an integer: "))

power_of_two = 2
while power_of_two <= number:
    power_of_two *= 2
    
if power_of_two - 1 == number:
    print(f"{number} is a Mersenne number.")
else:
    print(f"{number} is not a Mersenne number.")
