import sys

def fact(n):
  result = 1
  if n > 0:
    result = n * fact(n-1)
  return result

num = int(sys.stdin.readline())
print(fact(num))