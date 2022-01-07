def dequycan(n):
    if n == 0:
        return 1
    else:
        return dequycan(n-1)

print(dequycan(10))