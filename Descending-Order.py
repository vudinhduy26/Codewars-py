def descending_order(num):
    arr = [int(i) for i in str(num)]
    d = True
    while d:
        d = False
        for i in range(0,len(arr)-1):
            if arr[i] < arr[i+1]:
                arr[i],arr[i+1]= arr[i+1],arr[i]
                d = True
    return int(''.join([str(i) for i in arr]))

print(descending_order(123948)) 