def sum_squares(n):
    return sum(k*k for k in range(1,n+1) if k*k <= n)

print(sum_squares(25))
print(sum_squares(100))
print(sum_squares(72))