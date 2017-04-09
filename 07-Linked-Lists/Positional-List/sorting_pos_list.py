import positional_list as List

def insertion_sort(L):
    """Sort PositionalList of comparable elements in non-decreasing order."""

    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value > marker.element():        # pivot is already sorted
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(walk)
                L.add_before(walk, value)