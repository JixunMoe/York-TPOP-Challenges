#!/usr/bin/env python3

def main():
  token = ' × '

  raw_n = int(input())
  n = raw_n

  if n <= 1 or n >= 1000000:
    print('%d is out of range (1 < n < 1000000)' % n)
    return

  # Find all prime factors.

  lst_prime = {}
  x = 2
  while n is not 1 and x <= n:
    if n % x == 0:
      n /= x

      if x in lst_prime:
        lst_prime[x] += 1
      else:
        lst_prime[x] = 1
      continue
    x += 1

  sResult = ''
  for p in lst_prime:
    sResult += token + str(p)
    if lst_prime[p] > 1:
      sResult += '^' + str(lst_prime[p])
  sResult = sResult[len(token):]

  print('%d = %s' % (raw_n, sResult))

if __name__ == '__main__':
  main()
