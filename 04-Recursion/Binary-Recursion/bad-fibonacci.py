def bad_fibonacci(n):
    """Return Nth fibonacci number."""
    if n <= 1:
        return 1
    else:
        return bad_fibonacci(n - 1) + bad_fibonacci(n - 2)

# Testing
print(bad_fibonacci(5))
print(bad_fibonacci(20))