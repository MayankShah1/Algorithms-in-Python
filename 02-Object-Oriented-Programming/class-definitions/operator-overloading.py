class Vector:
    """Represent a vector in multidimensional space"""

    def __init__(self, d):
        """Create a d-dimensional vector of zeros."""
        self._cords = [0] * d

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
print(v)
print(v[4])

u = v + v
print(u)

total = 0
for entry in v:
    total += entry
print(total)