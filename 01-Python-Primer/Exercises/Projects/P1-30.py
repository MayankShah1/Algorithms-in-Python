def divide_two(n):
    count = 0
    while n > 2:
        count += 1
        n //= 2
    return count

print(divide_two(8))
print(divide_two(125))