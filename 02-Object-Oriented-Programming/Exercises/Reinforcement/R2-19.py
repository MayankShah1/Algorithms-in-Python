class Progression:
    """
    Iterator producing a generic progression.

    Default iterator produces the whole numbers 0, 1, 2
    """

    def __init__(self,start = 0):
        """Intialise current to the first value of progression."""
        self._current = start
        # FOR question
        self._count = 0

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
        elif self._current >= pow(2,63):
            print('\nReached!!')
            return self._count
        else:
            answer = self._current
            self._advance()
            self._count += 1
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


# Testing phase
from math import inf
if __name__ == "__main__":
    print('Default progression:' )
    Progression().print_progression(10)

    print('Arithmetic progression with increment 5:' )
    ArithmeticProgression(128,0).print_progression(50000)
    print('Arithmetic progression with increment 5 and start 2:' )
    ArithmeticProgression(5, 2).print_progression(10)

    print('Geometric progression with default base:' )
    GeometricProgression().print_progression(10)
    print('Geometric progression with base 3:' )
    GeometricProgression(3).print_progression(10)

    print('Fibonacci progression with default start values:' )
    FibonacciProgression().print_progression(10)
    print('Fibonacci progression with start values 4 and 6:' )
    FibonacciProgression(4, 6).print_progression(10)


