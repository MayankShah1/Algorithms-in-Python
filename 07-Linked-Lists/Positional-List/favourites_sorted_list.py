import positional_list as List

class FavouritesList:
    """List of elements ordered from most frequently accessed to least frequently accessed"""

    # --------------------- nested _Item class --------------------
    class _Item:
        __slots__ = '_value', '_count'
        def __init__(self, e):
            self._value = e
            self._count = 0

    # ---------------- non public utilities ----------------

    def _find_position(self, e):
        """Search for element e and return its Position(or None if not found)"""
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        """Move item at Position p earlier in the list based on access count."""
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element._count:
                while (walk != self._data.first() and cnt > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))

    # ---------------------- public methods -------------------

    def __init__(self):
        """Create an empty list of favourites"""
        self._data = List.PositionalList()

    def __len__(self):
        """Return the number of entries in favourites list"""
        return len(self._data)

    def is_empty(self):
        """Return True if list is empty"""
        return len(self._data) == 0

    def access(self, e):
        """Access element e, thereby increasing its count"""
        p = self._find_position(e)
        if p is None:
            p = self._data.add_last(self._Item(e))
        p.element()._count += 1
        self._move_up(p)

    def remove(self, e):
        """Remove element e from the list of favourites"""
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)

    def top(self, k):
        """Generates sequence of top k elements in terms of access count."""
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        walk = self._data.first()
        for j in range(k):
            item = walk.element()
            yield item._value
            walk = self._data.after(walk)