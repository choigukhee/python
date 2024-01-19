import sys

def two(n):
  cnt = 0
  while n >= 2:
    n //= 2
    cnt += n
  return cnt

def five(n):
  cnt = 0
  while n >= 5:
    n //= 5
    cnt += n
  return cnt

a, b = map(int, sys.stdin.readline().split())

twozero = two(a) - two(a - b) - two(b)
fivezero = five(a) - five(a - b) - five(b)

print(min(twozero, fivezero))