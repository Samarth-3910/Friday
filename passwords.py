password = input()

minimum_length = 8

symbols = "!@#$%^&*()?><:|"

has_uppercase = any(char.isupper() for char in password)
has_lowercase = any(char.islower() for char in password)
has_digit  = any(char.isdigit() for char in password)
has_symbols = any(char in symbols for char in password)
has_length = len(password) >= minimum_length

if has_uppercase and has_lowercase and has_length and has_digit and has_symbols:
    print("Strong")
elif (has_uppercase or has_lowercase) and (has_digit or has_symbols) and has_length:
    print("Medium")
else:
    print("Weak")