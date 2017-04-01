def norm(vector, power = 2):
    sum = 0
    for coordinate in vector:
        sum += coordinate ** power
    return sum ** (1/power)

vector_1 = [3,4]
vector_2 = [1, 2, 3]

print(norm(vector_1))
print(norm(vector_1, 2))
print(norm(vector_1, 3))
print(norm(vector_2, 1))