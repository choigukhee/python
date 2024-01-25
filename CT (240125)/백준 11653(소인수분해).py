# import sys

# prime = []
# primeList = [0] * 1000001

# for i in range(2, 1000001):
#   if primeList[i] == 0:
#     prime.append(i)
#   for j in range(i*2, 1000001, i):
#     primeList[j] = 1
    
# n = int(sys.stdin.readline().rstrip())
# ans = []

# while n > 1:
#   for i in prime:
#     while n % i == 0:
#       n //= i
#       ans.append(i)
#   if n == 1:
#     break

# for i in ans:
#   print(i)

import sys

n = int(sys.stdin.readline().rstrip())
i = 2

while n != 1:
  if n % i == 0:
    print(i)
    n //= i
  else:
    i += 1
    