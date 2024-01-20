import sys
import math

n, s = map(int, sys.stdin.readline().split())
now = list(map(int, sys.stdin.readline().split()))

dist = []

for i in now:
  dist.append(abs(i - s))

ans = dist[0]

for i in dist:
  ans = math.gcd(ans, i)

print(ans)