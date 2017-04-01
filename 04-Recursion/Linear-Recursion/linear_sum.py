def linear_sum(S, n):
    """Return sum of the first n numbers of S"""
    if n == 0:
        return 0
    else:
        return linear_sum(S, n - 1) + S[n-1]


# Testing
if __name__ == "__main__":
    print(linear_sum([1,2,3,4,5,6,7],5))