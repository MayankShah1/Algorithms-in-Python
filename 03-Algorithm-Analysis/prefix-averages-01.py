def prefix_averages(S):
    """Returns list such that, for all j,A[j] equals average of S[0],...,S[j]"""
    n = len(S)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += S[i]
        A[j] = total / (j + 1)
    return A

# Testing
if __name__ == "__main__":
    S = [1, 2, 3, 4]
    print(prefix_averages(S))