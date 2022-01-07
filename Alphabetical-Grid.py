
##########
def grid(k):
    a = 97
    b = a + k
    crr = [[] for i in range(k)]
    drr = []
    for row in crr:
        for col in range(a,b):
            row.append(chr(col))
        if b == 122 & a > b:
            a = 97
            b = a + k
        else:
            a +=1
            b +=1
    for i in crr:
        drr.append(str(i))
    return "\n".join(drr)
        
#i = 0
print(grid(4))
"""
def main():
    for i in grid(5):
        print(' '.join(i))
if __name__ == "__main__":
    main()
"""
"""
while n <= 13:
    try:
        brr.append(arr[i])
        i+=1
        n+=1
    except:
        i=0
"""
"""
arr = [1,2,3,4]
brr = []
z = 0
for i in range(0,13+1):
    if z > len(arr)-1:
        z = 0
        brr.append(arr[z])
    else:
        brr.append(arr[z])
    z +=1
print(brr)
"""   