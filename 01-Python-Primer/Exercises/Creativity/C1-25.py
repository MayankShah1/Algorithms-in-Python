def remove_punctuations(input_string):
    punctuation_marks = [',','\'','.','?','!']
    ans = ''
    for char in input_string:
        if char not in punctuation_marks:
            ans += char
    return ans

print(remove_punctuations('Let\'s try, Mike.'))

