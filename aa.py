n = 7
for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(1,i+1):
        print('Iu Iu',end='.')
    for j in range(i+1):
        print('Iu Iu',end='.')
    print()
