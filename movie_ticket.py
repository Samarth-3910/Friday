age = int(input("Enter your age: "))
day = input("Enter the day of the week: ").lower()

if age >= 65:
    print("You qualify for a senior discount of 10%!")
elif day == "tuesday":
    print("It's Tuesday! You qualify for a 15% discount.")
else:
    print("You don't qualify for a discount today, but enjoy the movie!")
