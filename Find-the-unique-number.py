def find_uniq(arr):
    a, b = set(arr) #set does no contain duplicate values
    #c = set(arr)
    n = 0
    if arr.count(a) == 1:
        n = a
    else:
        n = b
    return n  # n: unique number in the array

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))