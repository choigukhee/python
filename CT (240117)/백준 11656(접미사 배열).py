import sys
s = sys.stdin.readline().rstrip()
word = []

word.append(s)

for _ in range(len(s)-1):
  s = s[1:]
  word.append(s)

for i in sorted(word):
  print(i)
