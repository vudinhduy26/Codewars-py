def even_fib(m):
    a,b = 0,1
    total = 0
    arr = []
    while a <= m:
        if a%2==0:
            total += a
        a,b = b,a+b
    return total

def even_fib_sum(m):
    fn_2, fn_1, fn = 1, 1, 0
    even_sum = 0
    while fn < m:
        fn_2, fn_1, fn = fn_1, fn, fn_1 + fn_2
        if fn%2 == 0:
            even_sum += fn
    return even_sum
print(even_fib_sum(10))