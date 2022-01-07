def prime(z):
    l = 0
    for i in range(2,z+2):
        if z%i==0:
            l = i
            break
    return l

def prime_factors (n):
    k = n
    arr = []
    while k!=1:
        a = prime(k)
        arr.append(a)
        k //= a
    return arr

print(prime_factors(12))