import math
"""
def solve(n):
    t = []
    for i in range(1,n):
        k = n+i**2
        if round(math.sqrt(k))**2 == k:
            t.append(i**2)
    if len(t) != 0:
        return t[0]
    return -1
"""
def solve(n):
    nn = 1
    next = 3
    k = -1
    while next <= n:
        sq = math.sqrt(n+nn)
        if math.floor(sq) == sq:
            k = nn
            break
        nn += next
        next += 2
    return k


print(solve(5))