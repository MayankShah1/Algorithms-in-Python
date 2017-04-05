class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._data = []

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if stack is empty."""
        return len(self._data) == 0

    def push(self,e):
        """Add element e to the top of the stack."""
        self._data.append(e)

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
        return self._data.pop()

    def __str__(self):
        """Prints the elements of stack"""
        result = ''.join(str(self._data[i]) + " " for i in range(len(self._data)))
        return result



# Testing
if __name__ == "__main__":
    S = ArrayStack()
    S.push(5)
    S.push(3)
    print(len(S))
    print(S.pop())
    print(S.is_empty())
    print(S.pop())
    print(S.is_empty())
    S.push(7)
    S.push(9)
    print(S.top())
    S.push(4)
    print(len(S))
    print(S.pop())
    S.push(6)