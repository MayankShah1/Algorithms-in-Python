def power(x, n):
    """Compute the value x**n for integer n"""
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result

# Testing
print(power(2,100))