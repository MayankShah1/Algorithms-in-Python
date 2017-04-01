def reverse_list(data):
    reversed_list = []
    for index in range(len(data) - 1, -1, -1):
        reversed_list += [data[index]]

    return reversed_list

input_list = [10, 2, -1, 100, 48, 0]
print(reverse_list(input_list))