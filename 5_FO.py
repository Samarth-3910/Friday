#+-/*%

A = int(input())
B = int(input())
R = int(input())

if A + B == R :
    print("+")
elif A - B == R:
    print("-")
elif A / B == R or A // B == R:
    print("/")
elif A * B == R:
    print("*")
elif A % B == R or B % A == R:
    print("%")