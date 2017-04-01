class Vector:
    """Represent a vector in multidimensional space"""

    def __init__(self, d):
        """Create a d-dimensional vector of zeros."""
        if isinstance(d, int):
            self._cords = [0] * d
        else:
            try:
                self._cords = [val for val in d]
            except TypeError:
                raise TypeError('invalid type')

    def __len__(self):
        """Return the dimension of vector"""
        return len(self._cords)

    def __getitem__(self, j):
        """Return the jth coordinate of the vector"""
        return self._cords[j]

    def __setitem__(self, j, value):
        """Set jth coordinate of vector to given value."""
        self._cords[j] = value

    def __add__(self, other):
        """Return sum of two vectors"""
        if len(self) != len(other): # relies on __len__method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    # R2-11
    def __radd__(self, other):
        """Return sum of two vectors"""
        return self.__add__(other)


    # R2 - 09
    def __sub__(self, other):
        """Return difference of two vectors"""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    # R2 - 10
    def __neg__(self):
        """Returns the negative of each coordinate of the vector"""
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -1 * self[j]
        return result

    # R2 - 12
    def __mul__(self, other):
        """Returns the dot product or constant multiplication"""
        if isinstance(other, (int, float)):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * other
            return result
        elif isinstance(other,Vector):
            if len(self) != len(other):
                raise ValueError('dimensions must agree')
            else:
                dot_product = 0
                for j in range(len(self)):
                    dot_product += self[j]*other[j]
                return dot_product


    def __rmul__(self, other):
        """Returns the dot product or constant multiplication"""
        return self.__mul__(other)

    def __eq__(self, other):
        """Return True if vector has same coordinates"""
        return self._cords == other._cords

    def __ne__(self, other):
        """Return True if vectors differ from each other"""
        return not self == other

    def __str__(self):
        """Produce string representation of Vector"""
        return '<' + str(self._cords)[1:-1] + '>' # adapt list-representation


# Testing
v = Vector(5)
print(v)

v[1] = 23
v[-1] = 45
print('v : ',v)
print(v[4])

u = v + v
print('u: ',u)
u = u + [5, 3, 10, -2, 1]
print('u: ',u)
u = [5, 3, 10, -2, 1] + u
print('u: ',u)

a = Vector(5)
for i in range(len(a)):
    a[i] = i + 1

b = u - a
print('b: ', b)

c = -b
print('c: ', c)

c = b * (-2)
print('c: ',c)

c = -3 * c
print('c: ',c)

c = u * b
print('c: ',c)

x = Vector([12, 23, 34, 45, 56])
print('x: ',x)

total = 0
for entry in v:
    total += entry
print(total)