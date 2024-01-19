import sys

def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a

for _ in range(int(sys.stdin.readline())):
  sum = 0
  numlist = list(map(int, sys.stdin.readline().split()))
  len = numlist.pop(0)
  for i in range(len):
    for j in range(len):
      if i < j:
        sum += gcd(numlist[i], numlist[j])
  print(sum)