class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class Full(Exception):
    """Error attempting to push an element to a full container."""
    pass

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self, maxlen = None):
        """Create an empty stack."""
        self._maxlen = maxlen
        if self._maxlen is not None:
            self._data = [None] * self._maxlen
        self._n = 0

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._n

    def is_empty(self):
        """Return True if stack is empty."""
        return self._n == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        if self._maxlen is not None and (self._maxlen == self._n):
            raise Full('Stack is full')
        if self._data[self._n] is None:
            self._data[self._n] = e
        self._n += 1

    def top(self):
        """Return the element at the top of the stack.

        Raise empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._data[-1]

    def pop(self):
        """Remove and return the element from the top of the Stack.

        Raise empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty.')
        answer = self._data[self._n-1]
        self._data[self._n-1] = None
        self._n -= 1
        return answer

    def __str__(self):
        """Prints the elements of stack"""
        result = ''.join(str(self._data[i]) + " " for i in range(len(self._data)) if self._data[i] is not None)
        return result


# Testing
if __name__ == "__main__":
    S = ArrayStack(3)
    S.push(5)
    S.push(3)
    print(len(S))
    print(S)
    S.push(7)
    print(len(S))
    print(S)
    print(S.is_empty())
    print(S.pop())
    print(S.is_empty())
    print(S)
    S.push(9)
    print(S.top())
    print(S)
    print(len(S))
    print(S.pop())
    S.push(6)
    print(S)
