def subsets(Set):
    if len(Set) <= 1:
        return Set[0]
    else:
        subset = []
        subset.append(Set[0])
        subset.append(Set[1:len(Set)])
        return subset

# Testing
print(subsets([1,2,3,4]))