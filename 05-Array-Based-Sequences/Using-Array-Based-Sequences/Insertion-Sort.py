def insertion_sort(A):
    """Sort list of comparable elements in non-decreasing order"""

    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur


# Testing
if __name__ == "__main__":
    data = [1,7,6,2,9,10,4,3,5]
    print(data)
    insertion_sort(data)
    print(data)