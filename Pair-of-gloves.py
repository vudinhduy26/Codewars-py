def number_of_pairs(gloves):
    dictt = {}
    k = 0
    for i in gloves:
        if i in dictt:
            dictt[i] +=1
        else:
            dictt[i] = 1

    for j in dictt:
        k += dictt[j]//2

    return k
print(number_of_pairs(["red","green","blue"])) 