def dot_product(a, b):
    product = []
    for index in range(len(a)):
        product.append(a[index]*b[index])

    return product

test_a = [1, 2, 3, 4, 5]
test_b = [6, 7, 8, 9, 10]
print(dot_product(test_a,test_b))