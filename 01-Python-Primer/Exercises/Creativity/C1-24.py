def count_vowels(input_string):
    count = 0
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for char in input_string:
        if char in vowels:
            count += 1
    return count

print(count_vowels('Hello world, I\'m here'))