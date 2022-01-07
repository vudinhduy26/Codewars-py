def ucln(a,b):
    if b == 0:
        return a
    return ucln(b,a%b)

arr = sorted(list(map(int,input("Nhap day N : ").split(" "))))
brr = arr[2::]
k = len(brr)
z = ucln(arr[0],arr[1])
c = 0
for i in brr:
    c = ucln(z,i)
    h = c
    z = h
print(brr)
