N = int(input())
Q = int(input())

result = N

for i in range(Q):
    operator, number = input().split()
    numbers = int(number)

    if operator == '+':
        result += numbers
    elif operator == '-':
        result -= numbers
    elif operator == '/':
        result //= numbers
    elif operator == '*':
        result *=  numbers
    elif operator == '%':
        result %= numbers
    elif operator == '&':
        result &= numbers
    elif operator == '^':
        result ^= numbers
    elif operator == '|':
        result |= numbers

print(result)