def disjoint(A, B, C):
    """Return True if there is no element common to all 3 lists."""
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True

# Testing
print(disjoint([1,2,3,4],[5,6,7,2],[8,9,0,1]))