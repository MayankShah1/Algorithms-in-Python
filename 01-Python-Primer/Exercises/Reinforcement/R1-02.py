def is_even(k):
    while k != 0 and k != 1:
        k -= 2
    if k == 0:
        return True
    else:
        return False

print(is_even(100))
print(is_even(23))

# Better interpretation
def is_even_better(k):
    return not k & 1

print(is_even_better(100))
print(is_even_better(23))
