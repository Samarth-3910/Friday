n = int(input())

sum_sqr = 0

while n > 0:
    digit = n % 10
    sum_sqr = sum_sqr + digit**2
    n = n // 10

print(sum_sqr)