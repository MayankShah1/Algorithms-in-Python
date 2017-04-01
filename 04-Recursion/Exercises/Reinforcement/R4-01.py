def maximum(S,n):
    """Return the maximum of n elements in S"""
    if n >= 1:
        max = S[n - 1]
        other_element = maximum(S, n-1)
        if other_element > max:
            max = other_element
    else:
        max = S[n]
    return max

# Testing
print(maximum([1,2,3,4],4))
print(maximum([4,3,2,1],4))
print(maximum([1,2,4,3],4))
