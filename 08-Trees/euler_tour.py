class EulerTour:
    """
    Abstract base class for performing Euler tour of a tree

    _hook_previsit and _hook_postvisit may be overriden by subclasses.
    """

    def __init__(self, tree):
        """
        Prepare a Euler template for given tree.
        """
        self._tree = tree

    def tree(self):
        """
        Return reference to the tree being traversed.
        """
        return self._tree

    def execute(self):
        """Perform the tour and return any result from post visit of root."""
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])

    def _tour(self, p, d, path):
        """
        Perform tour of subtree rooted at Position p

        p:      Position of current node being visited
        d:      depth of p in tree
        path:   list of indices of children on path from root to p

        """
        self._hook_previsit(p, d, path)
        results = []
        path.append(0)
        for c in self._tree.children(p):
            results.append(self._tour(c, d+1, path))
            path[-1] += 1
        path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer

    def _hook_previsit(self, p, d, path):
        pass

    def _hook_postvisit(self, p, d, path, results):
        pass


class PreorderPrintIndentTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        print(2 * d * ' ' + str(p.element()))

class PreorderPrintIndentedLabeledTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        label = '.'.join(str(j+1) for j in path)
        print(2 * d * ' ' + label, str(p.element()))

class ParenthesizeTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        if path and path[-1] > 0:           # p follows a sibling
            print(', ', end='')
        print(p.element(), end='')
        if not self.tree().is_leaf(p):
            print(' (', end='')

    def _hook_postvisit(self, p, d, path, results):
        if not self.tree().is_leaf(p):
            print(')', end='')

class DiskSpaceTour(EulerTour):
    def _hook_postvisit(self, p, d, path, results):
        return p.element().space() + sum(results)

