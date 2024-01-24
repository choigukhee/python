import sys

n, b = map(int, sys.stdin.readline().split())
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = []

while n :
  ans.append(arr[n%b])
  n //= b

print(''.join(ans[::-1]))