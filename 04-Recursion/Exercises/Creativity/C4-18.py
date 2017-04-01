def vowels_more(S):
    vowels = ['a','e','i','o','u']
    vowels_count = 0
    if len(S) <= 1:
        if S[0] in vowels:
            return 1
        else:
            return -1
    else:
        print('string: ',S)
        print('vowels count: ',vowels_count)
        if S[0] in vowels:
            print('Reached')
            vowels_count += 1
        else:
            vowels_count -= 1
        print('vowels count: ', vowels_count)
        vowels_count += vowels_more(S[1:len(S)])
        if vowels_count > 0:
            return True
        else:
            return False

# Testing
print(vowels_more('abcd'))
print(vowels_more('aeioud'))
