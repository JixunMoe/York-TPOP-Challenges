#!/usr/bin/env python3

def main():
  n = int(input())

  if n < 2 or n > 49:
    print ('Please use a number between 2 and 49.')
    return

  # Generate a list of prime up to 49
  base_prime = [2, 3, 5, 7]
  for x in range(2, 49):
    x_is_prime = True
    for p in base_prime:
      if x % p == 0:
        x_is_prime = False
        break

    if x_is_prime:
      base_prime.append(x)

  if n in base_prime:
    print ('Yes, %d is a prime.' % n)
  else:
    print ('No, %d is not a prime.' % n)

if __name__ == '__main__':
  main();