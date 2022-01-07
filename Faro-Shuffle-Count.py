import math
def faro_cycles(deck_size):
    k,i = 0,1
    if deck_size == 2:
        return 1
    while k != 1:
        i +=1
        k = (2**i)%(deck_size-1)
    return i

print(faro_cycles(1000))
