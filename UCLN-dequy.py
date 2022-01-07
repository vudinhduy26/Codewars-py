def ucln(a,b):
    if b == 0:
        return a
    return ucln(b,a%b)

print(ucln(15,8))