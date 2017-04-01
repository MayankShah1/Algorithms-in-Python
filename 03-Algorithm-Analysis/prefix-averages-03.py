def prefix_averages(S):
    """Returns list such that, for all j,A[j] equals average of S[0],...,S[j]"""
    n = len(S)
    A = [0] * n
    total = 0
    for j in range(n):
        total += S[j]
        A[j] = total / (j + 1)
    return A

# Testing
if __name__ == "__main__":
    S = [1, 2, 3, 4]
    print(prefix_averages(S))