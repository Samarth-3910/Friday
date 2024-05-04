message = input("Enter the message to encrypt: ")
key = int(input("Enter the encryption key (a number between 1 and 25): "))
encrypted_message = ""

for char in message:
    if char.isalpha():
        if char.isupper():
            encrypted_message += chr((ord(char) - 65 + key) % 26 + 65)
        else:
            encrypted_message += chr((ord(char) - 97 + key) % 26 + 97)
    else:
        encrypted_message += char

print("Encrypted message:", encrypted_message)
