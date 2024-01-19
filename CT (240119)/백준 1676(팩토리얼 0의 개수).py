import sys

def factzero(n):
  cnt = 0
  while n >= 5:
    n //= 5
    cnt += n
  return cnt

num = int(sys.stdin.readline())
print(factzero(num))
