def disjoint(A, B, C):
    """Return True if there is no element common to all 3 lists."""
    combined = []
    for j in range(len(A)):
        combined.append(A[j])
    for j in range(len(B)):
        combined.append(B[j])
    for j in range(len(C)):
        combined.append(C[j])
    temp = sorted(combined)
    for j in range(1,len(temp)-1):
        if temp[j-1] == temp[j] == temp[j+1]:
            return False
    return True


# Testing
print(disjoint([1,2,3,4],[5,6,7,2],[8,9,0,1]))
print(disjoint([2,3,4,9],[2,3,6,5,9],[4,5,2,3,6,8,1,9]))