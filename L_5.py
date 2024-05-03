t_c = int(input())
test_cases = []

for i in range(t_c):
    x, y = map(int, input().split())
    test_cases.append((x, y))

def is_prime(n):
    if n <= 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True

results = []

for x, y in test_cases:
    sum_potatoes = x + y
    min_potat_third_f = 1
    while not is_prime(sum_potatoes + min_potat_third_f):
        min_potat_third_f += 1
    results.append(min_potat_third_f)

for result in results:
    print(result)
