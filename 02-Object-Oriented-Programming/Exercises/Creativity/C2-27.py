class Range:
    """A class that mimic's the built-in range class """

    def __init__(self, start, stop = None, step = 1):
        """
        Initialize a Range instance

        Semantics is similar to built-in range class
        """
        if step == 0:
            raise ValueError('step cannot be zero')

        if stop is None:    # special case of range(n)
            start,stop = 0,start    # should be as range(0,n)

        # calculate the effective length once
        self._length = max(0, (stop - start + step - 1) // step)

        # need acknowledge of start and step
        self._start = start
        self._step = step

    def __len__(self):
        """Return the number of entries in the range"""
        return self._length

    def __getitem__(self, k):
        """Return entry at index k"""

        # attempt to convert negative index
        if k < 0:
            k += len(self)

        if not 0 <= k < self._length:
            raise IndexError('index out of range')

        return self._start + k * self._step

    def __contains__(self, item):
        """Return True if item in range; False otherwise"""
        if (item - self._start) % self._step == 0:
            return True
        else:
            return False

# Testing
r = range(8, 140, 5)
print(len(r))
print(r[15])
for i in r:
    print(i)

print()

r = Range(8, 140, 5)
print(len(r))
print(r[15])
for i in r:
    print(i)