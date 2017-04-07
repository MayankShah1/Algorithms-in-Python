class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage"""

    # --------------- nested _Node class -----------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next


    # -------------------- stack methods ------------------

    def __init__(self):
        """Create an empty stack"""

        self._head = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in stack"""
        return self._size

    def is_empty(self):
        """Return True if stack is empty"""
        return self._size == 0

    def push(self,e):
        """Add element to the top of stack"""
        self._head = self._Node(e,self._head)
        self._size += 1

    def top(self):
        """Return the element at the top of the stack.
        
        Raise Empty exception if stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def pop(self):
        """ Return and remove the element at the top of the stack
         
        Raise empty exception if stack is empty. 
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


# Testing
if __name__ == "__main__":
    stack = LinkedStack()

    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack.top())
    stack.push(40)
    print(stack.pop())