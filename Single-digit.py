def single_digit(n):
    while len(str(n)) != 1:
        c = 0
        k = '{0:08b}'.format(n)
        for i in str(k):
            c += int(i)
        n = c
    return n

print(single_digit(5665))