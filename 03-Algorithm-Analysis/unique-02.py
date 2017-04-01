def unique(S):
    """Return True if there are no duplicate elements in sequence S."""
    temp = sorted(S)
    for j in range(1, len(temp)):
        if temp[j-1] == temp[j]:
            return False
    return True

# Testing
print(unique([1,2,3,4,5]))
print(unique([1,2,3,4,1,2]))