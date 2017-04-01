def factorial(n):
    if n < 0:
        return
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Testing
print(factorial(0))
print(factorial(1))
print(factorial(23))
print(factorial(-2))