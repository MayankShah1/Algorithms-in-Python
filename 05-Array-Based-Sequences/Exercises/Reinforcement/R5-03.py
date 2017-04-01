import sys

data = []

temp = 0

for k in range(26):
    a = len(data)
    b = sys.getsizeof(data)
    if b > temp:
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
        temp = b
    data.append(None)

print('\n\tShrinking \n')
for k in range(26):
    a = len(data)
    b = sys.getsizeof(data)
    if b < temp:
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
        temp = b
    data.pop()