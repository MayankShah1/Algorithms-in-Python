def good_fibonacci(n):
    """Return a pair of fibonacci numbers,F(n) and F(n-1)"""

    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n - 1)
        return (a+b, a)

# Testing
print(good_fibonacci(5))
print(good_fibonacci(20))