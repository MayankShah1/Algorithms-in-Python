import general_tree

class BinaryTree(general_tree.Tree):
    """Abstract base class representing a binary structure"""

    #------------additional abstract methods ------------------

    def left(self, p):
        """
        Return a position representing p's left child

        Return None if p doesn't have a left child
        """
        raise NotImplementedError('must be implemented by the subclass')

    def right(self, p):
        """
        Return a position representing p's right child

        Return None if p doesn't have a right child
         """
        raise NotImplementedError('must be implemented by the subclass')

    #-----------conncrete methods implemented by the class --------------------

    def sibling(self, p):
        """Return a Position representing p's sibling( or None if no sibling). """
        parent = self.parent(p)
        if parent is None:                          # p must be root
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def inorder(self):
        """Generate a inorder iteration of positions in the tree"""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """Geneate a inorder iteration of positions subrooted at p"""
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

    # override inhertied version to make inorder default
    def positions(self):
        """Generate an iteration of tree's positions."""
        return self.inorder()
