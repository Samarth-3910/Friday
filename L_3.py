num = int(input())

for i in range(1,num+1):
    if i % 400 == 0 and i % 100 == 0 or i % 4 == 0:
        print(i, end = ' ')
        