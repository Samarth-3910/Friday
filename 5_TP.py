def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False
    
n=int(input())
str_num=str(n)
rev_num=str_num[::-1]
if prime(n)and prime(int(rev_num)):
    print("it is twisted prime number.")
else:
    print("it is not twisted prime number.")