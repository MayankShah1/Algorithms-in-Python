import doubly_linked_list as DLL

class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class LinkedDeque(DLL._DoublyLinkedBase):
    """Double-ended queue implementation based on doubly linked list."""

    def first(self):
        """Return the element at the front of deque"""
        if self.is_empty():
            raise Empty('Deque is empty.')
        return self._header._next._element

    def last(self):
        """Return the element at the end of the deque"""
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._trailer._prev._element

    def insert_first(self, e):
        """Add an element e to the front of the deque"""
        self._insert_between(e, self._header,self._header._next)

    def insert_last(self, e):
        """Add an element e to the end of the deque"""
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delet_first(self):
        """Remove and the return the first element of deque.
        
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._header._next)

    def delet_last(self):
        """Remove and the return the first element of deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._trailer._prev)
