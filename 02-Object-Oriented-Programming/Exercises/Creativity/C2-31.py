class Progression:
    """
    Iterator producing a generic progression.

    Default iterator produces the whole numbers 0, 1, 2
    """

    def __init__(self,start = 0):
        """Intialise current to the first value of progression."""
        self._current = start

    def _advance(self):
        """
        Update self._current to new value

        This should be overriden by a subclass to customize progression

        By convention, if current is set to None, this designates
        end of finite progression.
        """
        self._current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator"""
        return self

    def print_progression(self,n):
        """Print next n values of the progression"""
        print('->'.join(str(next(self)) for j in range(n)))

class ArithmeticProgression(Progression):
    """Iterator producing an AP"""

    def __init__(self,increment = 1, start = 0):
        """
        Create a new AP

        increment:  the fixed item to add to each term
        start:      the first term of the progression
        """
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        """Update current value by adding the fixed increment"""
        self._current += self._increment


class GeometricProgression(Progression):
    """Iterator producing GP"""

    def __init__(self, base = 2, start = 1):
        """
        Create a new GP

        base:       the fixed constant multiplied to each term
        start:      the first term of the progression
        """
        super().__init__(start)
        self._base = base

    def _advance(self):
        """Update current value by multiplying it by base"""
        self._current *= self._base

class FibonacciProgression(Progression):
    """Iterator producing FP"""

    def __init__(self, first = 0, second = 1):
        """
        Create a new FP

        first:      the first term of progression
        second:     the second term of progression
        """
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        """Update current value by taking sum of previous two"""
        self._prev, self._current = self._current, self._prev + self._current


class DifferenceProgression(Progression):
    """Iterator producing DP"""
    def __init__(self,first = 2, second = 200):
        """

        first:      first term of progression
        second:     second term of progression
        """
        super().__init__(first)
        self._prev = abs(second + first)

    def _advance(self):
        """Update current value by taking difference of previous two"""
        self._prev, self._current = self._current, abs(self._current - self._prev)

class SquareRootProgression(GeometricProgression):
    """Iterator producing SRP"""
    def __init__(self,start = 65536):
        """

        start:      initial term of progression
        """
        super().__init__(1/2,start)



# Testing phase
if __name__ == "__main__":
    #print('Fibonacci progression with default start values:' )
    #FibonacciProgression().print_progression(10)
    #print('Fibonacci progression with start values 4 and 6:' )
    FibonacciProgression(4, 6).print_progression(10)

    DifferenceProgression().print_progression(10)
    SquareRootProgression().print_progression(10)


