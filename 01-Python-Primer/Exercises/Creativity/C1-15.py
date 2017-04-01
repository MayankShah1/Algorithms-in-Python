def distinct(data):
    temp = data
    for item in data:
        temp.remove(item)
        if item in temp:
            return False
    return True

input_list = [10, 2, -1, 100, 48, 0]
print(distinct(input_list))
test_2 = [100,3, 4 , 5, 2]
print(distinct(test_2))
test_3 = [1, 1, 1, 1, 1]
print(distinct(test_3))