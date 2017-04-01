def binary_sum(S, start, stop):
    """Return the sum of elements in slice S[start:stop]"""
    if start >= stop:
        return 0
    elif start == stop - 1:
        return S[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)

# Testing
print(binary_sum([1, 2,3,4, 5], 0 , 5))