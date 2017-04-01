class Matrix:
    """A class to perform basic matrix operations"""

    def __init__(self,matrix1, matrix2):
        """Initialise the rows and columns according to matrices"""

        self._matrix1 = matrix1
        self._row1 = len(matrix1)
        self._col1 = len(matrix1[0])

        self._matrix2 = matrix2
        self._row2 = len(matrix2)
        self._col2 = len(matrix2[0])

    def add_matrices(self):
        """Returns the sum of two matrices"""
        if not (self._row1 == self._row2 and self._col1 == self._col2):
            raise ValueError('Dimensions must agree')
        resultant = []
        for i in range(self._row1):
            inner = []
            for j in range(self._col1):
                inner.append(self._matrix1[i][j] + self._matrix2[i][j])
            resultant.append(inner)
        return resultant

    def mul_matrices(self):
        if not (self._col1 == self._row2):
            raise ValueError('Dimensions must agree')
        resultant = []
        for i in range(self._row1):
            inner = []
            for j in range(self._col2):
                product = 0
                for k in range(self._col1):
                    product += (self._matrix1[i][k] * self._matrix2[k][j])
                inner.append(product)
            resultant.append(inner)
        return resultant

# Testing
if __name__ == "__main__":
    mat = Matrix([[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]])
    sum = mat.add_matrices()
    prod = mat.mul_matrices()
    print(sum)
    print(prod)
