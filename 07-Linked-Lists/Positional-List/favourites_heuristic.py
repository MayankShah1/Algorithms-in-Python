import favourites_sorted_list as FL

class FavouritesListMTF(FL.FavouritesList):
    """List of elements ordered with move-to-front heuristic"""

    # override _move_up to provide move-to-front semantics
    def _move_up(self, p):
        """Move accessed item at Position p to front of list"""
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))

    # override top because list is no longer sorted
    def top(self, k):
        """Generate sequence of top k elements in term of access count."""
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')

        # we begin by making the copy of the original list
        temp = FL.PositionalList()
        for item in self._data:
            temp.add_last(item)

        # we repeatedly find, report, and remove the element with largest count
        for j in range(k):
            # find and report next highest from temp
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element._count:
                    highPos = walk
                walk = temp.after(walk)
            # we have found the element with highest count
            yield highPos.element()._value
            temp.delete(highPos)

