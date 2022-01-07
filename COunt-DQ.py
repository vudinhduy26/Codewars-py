def count(n):
    k = 0
    if n >= 100:
        return n
    return count(n+n)

print(count(10))