import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
stack = []
NGE = [-1] * n

for i in range(n):
  while stack and l[stack[-1]] < l[i]:
    NGE[stack.pop()] = l[i]
  stack.append(i)

print(*NGE)