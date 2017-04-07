class _DoublyLinkedBase:
    """ A base class providing a doubly linked list representation."""

    class _Node:
        """lightweight, nonpublic class for storing a doubly linked node."""

        __slots__ = '_element', '_next', '_prev'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Create an empty doubly linked list"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        """Return the number of elements in list"""
        return self._size

    def is_empty(self):
        """Return True if list is empty"""
        return self._size == 0

    def _insert_between(self,e, predecessor, successor):
        """Add an element e between two existing nodes and return new node"""
        newest = self._Node(e, predecessor,successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete a nonsenitel node from the list and return the element"""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

