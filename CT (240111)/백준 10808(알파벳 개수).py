import sys

s = sys.stdin.readline().strip()
frequency = [0] * 26

for i in s:
  frequency[ord(i) - ord('a')] += 1

print(*frequency)