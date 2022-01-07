def count_inversions(array):
    k = 0
    swap = True
    while swap:
        swap = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]
                swap = True
                k +=1
    
    return k

print(count_inversions([4, 3, 2, 1]))