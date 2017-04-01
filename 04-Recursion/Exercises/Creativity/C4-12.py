def mul(m, n):
    if n <= 0:
        return 0
    else:
        return m + mul(m, n - 1)

# Testing
print(mul(6,4))
print(mul(4,6))