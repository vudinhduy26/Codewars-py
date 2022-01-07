def are_coprime(n,m):
    arr1 = [i for i in range(1,n+1) if n%i == 0]
    arr2 = [j for j in range(1,m+1) if m%j == 0]
    k = list(set(arr1) & set(arr2))
    if len(k) == 1 & k[0] == 1:
        return True
    return False

print(are_coprime(12,39))