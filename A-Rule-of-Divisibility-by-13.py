def tenmodthirteen(array):
    crr = []
    for i in range(len(array)):
        crr.append((10**i)%13)
    return crr

def thirt(n):
    arr = [int(i) for i in str(n)[::-1]]
    brr = []
    result = 0
    k = True
    while k:
        for i in range(len(arr)):
            brr.append(arr[i]*tenmodthirteen(arr)[i])
        if len(str(sum(brr))) <= 2:
            result = sum(brr)
            k = False
        hrr = sum(brr)
        arr = [int(i) for i in str(hrr)[::-1]]
        brr = []
    return result

print(thirt(1111111111))