import sys

n = sys.stdin.readline().rstrip()

new = oct(int(n, 2))

print(new[2:])