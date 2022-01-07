import math
def check(z):
    h = True
    for i in range(2,round(math.sqrt(z)+1)):
        if z%i==0:
            h = False
            break
    return h
def next_prime(n):
    k = 0
    if n == 1 or n == 0:
        return  2
    for i in range(n+1,n+100):
        if check(i) == True:
            k = i
            break
    return k

print(next_prime(0))        