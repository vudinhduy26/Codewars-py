import math
def check_prime(a):
    k = 0
    for i in range(2,round(math.sqrt(a))+1):
        if a%i!=0:
            k = a
    return k

def prime_primes(N):
    arr = [2]
    crr = []
    h = 0
    for i in range(1,N+1):
        if check_prime(i)!=0:
            arr.append(check_prime(i))
    
    for j in range(len(arr)):
        if arr[j] == arr[len(arr)-1]:
            break
        for z in range(j,len(arr)):
            if arr[j]/arr[z] < 1:
                crr.append(arr[j]/arr[z])
                h+=1
    
    return h,sum(crr)

print(prime_primes(130))
