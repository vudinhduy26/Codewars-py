import math


def check(a):
    if a == 0 or a == 1:
        return False
    for i in range(2, round(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True


def main():
    n, m = int(input()), int(input())
    arr = []
    z = []
    k = 0
    while k != n:
        h = map(int, input().split())
        for i in h:
            if check(i):
                z.append(0)
            else:
                z.append(1)
        arr.append(z[:3])
        z = []
        k += 1
    print(arr)


if __name__ == "__main__":
    main()
