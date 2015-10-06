#!/usr/bin/env python3
import math
from os import path

prime_file = path.dirname(path.abspath(__file__)) + '/data/prime.txt'

class PrimeFinder():
  def __init__(self, prime_file):
    # Load primes
    self.file = open(prime_file, 'r+')
    self.base_prime = [2]
    line = self.file.readline()
    while line is not '':
      n = int(line.rstrip('\n'))
      self.base_prime.append(n)
      line = self.file.readline()

  def find_cache(self, n):
    return n in self.base_prime

  def check_is_prime(self, n, add_to_cache = True):
    print('>> No cache used for %d' % n)
    n_is_prime = True

    for x in range(2, math.ceil(math.sqrt(n))):
      if n % x is 0:
        n_is_prime = False
        break

    if n_is_prime and add_to_cache:
      self.base_prime.append(n)
      self.file.write('%d\n' % n)

  def check(self, n):
    return self.find_cache(n) or self.check_is_prime(n, True)


if __name__ == '__main__':
  pf = PrimeFinder(prime_file)
  n = int(input())
  if pf.check(n):
    print ('Yes, %d is a prime.' % n)
  else:
    print ('No, %d is not a prime.' % n)
