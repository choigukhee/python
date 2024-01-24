# import sys

# n, b = sys.stdin.readline().split()
# b = int(b)

# print(int(n, b))

import sys

arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n, b = sys.stdin.readline().split()
n = n[::-1]
b = int(b)
ans = 0

for i, a in enumerate(n):
  ans += (arr.index(a)) * (b**i)

print(ans)