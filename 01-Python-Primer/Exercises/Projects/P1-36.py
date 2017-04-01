def count_occurrences(data):
    word_counter = {}
    for word in data:
        if word not in word_counter:
            word_count = 1
            word_counter[word] = word_count
        else:
            word_counter[word] += 1

    return word_counter

print(count_occurrences(['hello','world','we','are','in','world','world','rocks']))
