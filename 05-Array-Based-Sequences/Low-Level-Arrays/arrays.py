import array
import sys

primes = array.array('i',[2,3,5,7,11])
print(primes)
print(sys.getsizeof(primes))
print(primes.itemsize)