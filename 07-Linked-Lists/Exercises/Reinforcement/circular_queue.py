class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class CircularQueue:
    """Queue implementation using circularly linked list for storage."""

    # --------------- nested _Node class -----------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next


    # -------------------- queue methods ------------------

    def __init__(self):
        """Create an empty queue"""
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements"""
        return self._size

    def is_empty(self):
        """Return True if queue is empty"""
        return self._size == 0

    def first(self):
        """Return the first element of the queue.

        Raise Empty exception if stack is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head

    def dequeue(self):
        """ Return and remove the element at the front of the queue.

                Raise empty exception if queue is empty. 
                """
        if self.is_empty():
            raise Empty('Queue is empty.')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self,e):
        """Add an element to the back of queue"""
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next         # new node points to head
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        """Roate front element to back of queue"""
        if self._size > 0:
            self._tail = self._tail._next

    def __str__(self):
        """Return the string representation of elements"""
        elements = []
        for i in range(self._size):
            elements.append(str(self._tail._next._element))
            self._tail = self._tail._next
        return ''.join(elements)




