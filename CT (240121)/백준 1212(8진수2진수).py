import sys

n = sys.stdin.readline().rstrip()
new = bin(int(n, 8))

print(new[2:])