import sys

s = sys.stdin.readline().strip()
seq = [-1] * 26
index = []

for i in range(len(s)):
  index.append(i)

for i in s:
  if seq[ord(i) - ord('a')] == -1:
    seq[ord(i) - ord('a')] = index.pop(0)
  else:
    index.pop(0)

print(*seq)