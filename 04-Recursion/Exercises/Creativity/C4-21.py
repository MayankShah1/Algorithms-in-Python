def pair_sum(S,k):
    if len(S) < 1 or S[0] > k:
        print(S)
        return False
    else:
        if k - S[0] in S[1:len(S)]:
            return (S[0],k - S[0])
        else:
            return pair_sum(S[1:len(S)],k)

# Testing

print(pair_sum([1,2,3,7],5))
print(pair_sum([1,2,3,4],5))
print(pair_sum([1,2,3,4],8))

