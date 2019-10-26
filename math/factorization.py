'''
Optimized algorithm for finding the factors for a number
Runtime: O(sqrt(n))
'''

import math

def factors_of_num(num):
  factors = []
  sqrt_num = int(math.sqrt(num))

  for factor in range(1, sqrt_num + 1):
    if (num % factor == 0):
      if num == sqrt_num:
        factors.append(factor, factor)
      else:
        factors.append((factor, num // factor))
  return factors


if __name__ == '__main__':
  num = 36
  print("factors of %s: %s" % (num, factors_of_num(num)))
