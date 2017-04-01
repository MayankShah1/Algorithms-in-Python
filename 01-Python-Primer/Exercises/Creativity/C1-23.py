import random

test_a = [1, 2, 3, 4, 5]

while True:
    try:
        index = random.randrange(len(test_a) + 1)
        print(test_a[index])
    except IndexError:
        print('Don’t try buffer overflow attacks in Python!')
        break