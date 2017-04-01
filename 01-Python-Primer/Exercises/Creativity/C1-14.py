def product_odd(data):
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j and data[i]% 2 != 0 and data[j]%2 != 0:
                return True
    return False

input_list = [10, 2, -1, 100, 48, 0]
print(product_odd(input_list))
test_2 = [100,3, 4 , 5, 2]
print(product_odd(test_2))

# Better implementation
# check if there are 2 odd numbers or not
def product_odd_better(data):
    count = 2
    for item in data:
        if item % 2 != 0:
            count -= 1
            if count == 0:
                return True
    return False

input_list = [10, 2, -1, 100, 48, 0]
print(product_odd_better(input_list))
test_2 = [100,3, 4 , 5, 2]
print(product_odd_better(test_2))
