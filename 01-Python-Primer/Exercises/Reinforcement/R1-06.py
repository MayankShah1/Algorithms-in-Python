def sum_squares_odd(n):
    return sum(k*k for k in range(1,n + 1) if k % 2 != 0)

print(sum_squares_odd(7))
print(sum_squares_odd(10))
print(sum_squares_odd(12))