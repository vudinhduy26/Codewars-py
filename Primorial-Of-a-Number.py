def ssnt(n):
    arr = [True]*(n*n)
    brr = []
    for i in range(2,n*n):
        if arr[i] == True:
            for j in range(i+i,n*n,i):
                arr[j] = False
    for z in range(len(arr)):
        if arr[z] == True:
            brr.append(z)
    
    return(brr[2::])

def num_primorial(n):
    i = 0
    k = 1
    arr = ssnt(n)
    while i != n:
        k *= arr[i]
        i +=1
    
    return k


print(num_primorial(9))