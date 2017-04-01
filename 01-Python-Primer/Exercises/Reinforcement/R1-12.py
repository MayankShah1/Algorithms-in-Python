import random

def choice_own(data):
    index = random.randrange(len(data))
    return data[index]

input_list = [10, 2, -1, 100, 48, 0]
print(choice_own(input_list))