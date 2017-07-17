import euler_tour

class BinaryEulerTour(euler_tour.EulerTour):
    """ Abstract base class for performing Euler tour of a binary tree.

    This version includes an additional hook invisit that is called after the tour
    of the left subtree( if any), yet before the tour  of the right subtree( if any).

    Note: Right child is always assigned index 1 in path, even if no left sibling. """

    def _tour(self, p, d, path):
        results = [None, None]
        self._hook_previsit(p, d, path)
        if self._tree.left(p) is not None:
            path.append(0)
            results[0] = self._tour(self._tree.left(p), d + 1, path)
            path.pop()
        self._hook_invisit(p, d, path)
        if self._tree.right(p) is not None:
            path.append(1)
            results[1] = self._tour(self._tree.left(p), d + 1, path)
            path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer

    def _hook_invisit(self, p, d, path):
        pass


class BinaryLayout(BinaryEulerTour):
    """Class for computing (x, y) coordinates for node of a binary tree"""

    def __init__(self, tree):
        super().__init__(tree)
        self._count = 0

    def _hook_invisit(self, p, d, path):
        p.element().setX(self._count)
        p.element().setY(d)
        self._count += 1