p1 = int(input())
p2 = int(input())
p3 = int(input())
A = int(input())

total_price = p1 + p2 + p3

p_p1 = round(p1 / total_price, 3)
p_p2 = round(p2 / total_price, 3)
p_p3 = round(p3 / total_price, 3)

if A >= min(p1,p2,p3):
    print(p_p1)
    print(p_p2)
    print(p_p3)