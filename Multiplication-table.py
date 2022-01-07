def multiplication(array):
    arr = []
    brr = []
    for i in range(len(array)):
        for j in range(len(array)):
            arr.append(array[i]*array[j])
        brr.append(arr)
        arr = []
    return(brr)

def multiplication_table(size):
    brr = [i for i in range(1,size+1)]
    return multiplication(brr)

print(multiplication_table(3))