import math
'''
def ssnt(a):
    arr = [True]*(a+2)
    brr = []
    can_n=int((a+2)**0.5)+1
    for i in range(2,can_n+1):
        for j in range(i+i,a+2,i):
            if arr[i] == True:
                arr[j] = False
            continue
    for i in range(len(arr)):
        if arr[i] == True:
            brr.append(i)
    return brr[2:]
'''
def isprime(k):
    if k < 2:
        return False
    check = True
    for i in range(2,round(math.sqrt(k))+1):
        if k%i==0:
            check = False
            break
    return check

def is_twinprime(n):
    c = isprime(n)
    a,b = isprime(n+2),isprime(n-2)
    if (a == True and b == True) and c == True:
        return True
    return False
print(is_twinprime(25))