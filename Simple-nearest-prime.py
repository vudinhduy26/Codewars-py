from gmpy2 import is_prime
from itertools import count

def solve(n):
    for i in count():
        if n > i and is_prime(n-i): return n-i
        if i > 0 and is_prime(n+i): return n+i

print(solve(4))