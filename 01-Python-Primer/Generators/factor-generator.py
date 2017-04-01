def factors(n):
    k = 1
    # k < sqrt(n)
    while k*k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1

    # if n is a perfect square
    if k*k == n:
        yield k

print('Factors of 100 and their double are :')
for i in factors(100):
    print('i : ',i, ' and 2 * i : ',2 * i)