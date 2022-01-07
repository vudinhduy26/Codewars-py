import re
def solve(a,b):
    k = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            k+=1  
    return k 

def pos_average(s):
    pattern = re.compile(r"\d+")
    arr = pattern.findall(s)
    k = 0
    total = (len(arr)*(len(arr)-1))/2
    
    for i in range(len(arr)):
        if arr[i] == arr[len(arr)-1]:
            break
        for j in range(i+1,len(arr)):
            k += solve(arr[i],arr[j])
            #brr.append(k)
    return k/(total*len(arr[0]))*100
print(pos_average("466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096"))