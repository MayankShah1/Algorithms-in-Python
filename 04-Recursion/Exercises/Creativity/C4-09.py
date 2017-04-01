def maximum_miniumum(S,n):
    """Return the maximum of n elements in S"""
    if n >= 1:
        max = min = S[n - 1]
        other_element,other = maximum_miniumum(S, n-1)
        if other_element > max:
            max = other_element
        if other_element < min:
            min = other_element
    else:
        max = min = S[n]
    return max,min

# Testing
maxm, minm = maximum_miniumum([1,2,3,4],4)
print('maxm: ',maxm, ' minm:', minm)
print()
#print(maximum_miniumum([4,3,2,1],4))
#print(maximum_miniumum([1,2,4,3],4))
