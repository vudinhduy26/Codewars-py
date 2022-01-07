import math
 
def primeFactors(n):
    arr = []
    # Print the number of two's that divide n
    while n % 2 == 0:
        arr.append(2)
        n = n / 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
         
        # while i divides n , print i and divide n
        while n % i== 0:
            if i in arr:
                n = n / i
                continue
            else:
                arr.append(i)
                n = n / i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        arr.append(int(n))
    return arr

def solve(a,b):
    arr = primeFactors(b)
    brr = []
    for i in arr:
        if a%i==0:
            brr.append(True)
        else:
            brr.append(False)
    if brr.count(False) == 0:
        return True
    return False

print(solve(9,315))