def ones_counter(inp):
    arr = ''.join([str(i) for i in inp]).split('0')
    brr = []
    for i in arr:
        if len(i) > 0:
            brr.append(len(i))
    return brr

print(ones_counter([1, 1, 1, 0, 0, 1, 0, 1, 1, 0]))