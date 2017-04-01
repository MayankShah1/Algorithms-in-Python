import random

def shuffle(data):
    for i in range(len(data)):
        swap_index = random.randint(0, len(data) - 1)
        data[i], data[swap_index] = data[swap_index], data[i]

    return data

test_a = [1, 2, 3, 4, 5]
print(shuffle(test_a))