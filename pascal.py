def content(a):
    arr = []
    for i in range(a):
        brr = []
        for j in range(i+1):
            if j == 0 or j==i:
                brr.append(1)
            else:
                k = arr[i-1][j-1]+arr[i-1][j]
                brr.append(k)
        arr.append(brr)
    return arr


def main():
    n = 7

    crr = content(n)
    ####
    for z in range(n):
        for j in range(n-z-1):
            print(format(" ","<2"),end="")
        for j in range(z+1):
            print(format(content(n)[z][j],"<3"),end=" ")
        print()
    ####
    for z in range(n):
        for j in range(z+1):
            print(format(content(n)[z][j],"<3"),end=" ")
        print()
        



if __name__ == "__main__":
    main()