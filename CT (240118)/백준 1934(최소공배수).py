import sys

def gcd(a,b):
  while b:
    a, b = b, a % b
  return a

def lcm(a,b):
  return int(a * b / gcd(a,b))

for _ in range(int(sys.stdin.readline())):
  a, b = map(int, sys.stdin.readline().split())
  print(lcm(a,b))
  