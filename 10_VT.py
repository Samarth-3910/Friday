test_case = int(input())

for i in range(test_case):
    A, B, C = input().split()

    A = int(A)
    B = int(B)
    C = int(C)

    #if map works
    #A, B, C = map(int, input().split)
total_angle = A+B+C

if total_angle == 180:
    print("Yes")
else:
    print("No")