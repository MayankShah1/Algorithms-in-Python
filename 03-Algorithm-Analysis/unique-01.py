def unique(S):
    """Return True if there are no duplicate elements in sequence S."""
    for j in range(len(S)):
        for k in range(j+1, len(S)):
            if S[j] == S[k]:
                return False
    return True

# Testing
print(unique([1,2,3,4,5]))
print(unique([1,2,3,4,1,2]))