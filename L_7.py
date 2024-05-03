import math

R, S, V = map(int, input().split())

r = S * V

d = math.sqrt(R**2 + r**2)

t = d / V

print("{:.3f}".format(t))