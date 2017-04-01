from abc import ABCMeta,abstractmethod

class Sequence(metaclass= ABCMeta):

    """Our own version of collections.Sequence abstract base class"""

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence."""

    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j of the sequence"""

    def __contains__(self, val):
        """Return True if val found in the sequence; False otherwise"""

        for j in range(len(self)):
            if self[j] == val:      # found match
                return True
        return False

    def index(self, val):
        """Return leftmost index at which val is found (or raise ValueError)"""
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('value not in sequence')

    def count(self, val):
        """Return the number of elements equal to given value."""
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k

    def __eq__(self, other):
        """Return True if sequences are equal; False otherwise"""
        if len(self) != len(other):
            return False
        else:
            count = 0
            for i in range(len(self)):
                if self[i] == other[i]:
                    count += 1
                else:
                    return False
            if count == len(self):
                return True

    def __lt__(self, other):
        """Return True if seq1 < seq2 lexicographically; False otherwise"""
        if len(self) != len(other):
            raise ValueError('Cannot be compared!')
        else:
            count = 0
            for i in range(len(self)):
                if self[i] <= self[j]:
                    count += 1
                else:
                    return False
            if count == len(self):
                return True