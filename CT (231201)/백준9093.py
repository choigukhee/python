import sys
n = int(sys.stdin.readline())

for i in range(n):
  text = sys.stdin.readline().split()
  for j in text:
    print(j[::-1], end = ' ')