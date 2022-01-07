import math
def compare_powers(n1,n2):
    k1 = n1[1]*math.log(n1[0])
    k2 = n2[1]*math.log(n2[0])
    if k1 > k2:
        return -1
    elif k1 < k2:
        return 1
    elif k1 == k2:
        return 0

print(compare_powers([7,7],[5,8]))