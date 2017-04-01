def sum_squares(n):
    sum = 0
    k = 1
    while k*k <= n:
        sum += k*k
        k += 1
    return sum

print(sum_squares(25))
print(sum_squares(100))
print(sum_squares(72))