def data_reverse(data):
    data = [str(k) for k in data]
    arr = []
    i = 0
    j = 8
    l = len(data)//8
    while l > 0:
        arr.append(''.join(data[i:j]))
        i += 8
        j += 8
        l -=1
    return [int(i) for i in ''.join(arr[::-1])]


data1 = [0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1]
print(data_reverse(data1))