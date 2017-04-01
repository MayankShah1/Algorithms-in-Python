def reverse_string(S):
    if len(S) <= 1:
        return S[0]
    else:
        return ''.join(S[len(S) - 1]) + reverse_string(S[:len(S)-1])


def palindrome(S):
    temp = S
    if S == reverse_string(temp):
        return True
    else:
        return False


# Testing
print(reverse_string('hello'))
print(reverse_string('pots&pans'))
print(palindrome('racecar'))
print(palindrome('hello'))