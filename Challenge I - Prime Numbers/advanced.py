#!/usr/bin/env python3

import math

def main():
  n = int(input())

  if n < 2:
    print ('Please, enter a number greater than 2.')
    return

  # Not most effective (?)
  # But this works
  n_is_prime = True
  for x in range(2, math.ceil(math.sqrt(n))):
    if n % x is 0:
      n_is_prime = False
      break

  if n_is_prime:
    print ('Yes, %d is a prime.' % n)
  else:
    print ('No, %d is not a prime.' % n)

if __name__ == '__main__':
  main();