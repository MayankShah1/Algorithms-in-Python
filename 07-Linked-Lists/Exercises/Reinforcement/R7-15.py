import doubly_linked_list as DLL


class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass


class PositionalList(DLL._DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    # ------------- nested Position Class --------------
    class Position:
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)

    # ------------- utility methods --------------------------

    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type.')
        if p._container is not self:
            raise ValueError('p does not belong to this container.')
        if p._node._next is None:  # deprecated nodes
            raise ValueError('p is no longer valid.')
        return p._node

    def _make_position(self, node):
        """Return position instance for given node."""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    # ------------------- accessors --------------------------

    def first(self):
        """Return the first position in the list."""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last position in the list."""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return the position just before Position p"""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Return the position just after Position p"""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of elements in the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def __reversed__(self):
        """Generate a backward iteration of elements in the list."""
        cursor = self.last()
        while cursor is not None:
            yield cursor.element()
            cursor = self.before(cursor)

    # ----------------------- mutators ---------------------------

    # override to return Position instead of node
    def _insert_between(self, e, predecessor, successor):
        """Add an element e between two existing nodes and return Position of new node"""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element at the front of the list and return new Position"""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Insert element at the last of the list and return new Position"""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Insert element into list before Postion p and return new Position"""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element into list after Postion p and return new Position"""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at position P"""
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        """Replace the element at positon p with e

        Return the element formerly at position p
        """
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value


# Testing
if __name__ == "__main__":
    position_list = PositionalList()

    position_list.add_last(8)
    for element in position_list:
        print(element)

    pos = position_list.first()
    pos2 = position_list.add_after(pos, 5)
    for element in position_list:
        print(element, end=' ')

    print()
    pos3 = position_list.add_before(pos2, 3)
    for element in position_list:
        print(element, end=' ')

    print()
    print(pos3.element())
    print(position_list.after(pos) == pos3)



