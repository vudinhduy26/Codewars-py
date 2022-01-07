"""
def solve(arr): 
    brr = arr
    crr = arr
    k = True
    while k:
        k = False
        for i in range(len(brr)):
            for j in range(i+1,len(brr)):
                if brr[i] == brr[j]:
                    crr.pop(i)
                    k = True
                    break

        hrr = crr
        brr = hrr
        
            
    return brr
"""
def solve(arr): 
    re = []
    for i in arr[::-1]:
        if i not in re:
            re.append(i)
    return re[::-1]
print(10**1%13)
