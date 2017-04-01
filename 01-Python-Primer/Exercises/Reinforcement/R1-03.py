from math import inf

def minmax(data):
    min = inf
    max = data[0]

    for item in data:
        if item <= min:
            min = item
        if item >= max:
            max = item

    return min, max

input_list = [10, 2, -1, 100, 48, 0]
ans_min, ans_max = minmax(input_list)
print(ans_min, " and ", ans_max)