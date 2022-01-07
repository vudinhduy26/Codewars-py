def make_chocolates(small, big, goal):
    arr = []
    for i in range(0,small+1):
        for j in range(0,big+1):
            if i*2+j*5 == goal:
                arr.append(i)
    if len(arr) != 0:
        return arr[0]
    return -1

print(make_chocolates(100, 90, 35))
