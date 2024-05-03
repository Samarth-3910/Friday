c = int(input())
s = int(input())

p_l = s - c

if p_l > 0:
    print("Profit")
else:
    print("Loss")

p_l_percentage = (p_l / c) * 100

print("{:.2f}%".format(p_l_percentage))