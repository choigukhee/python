import sys

a, b = map(int, sys.stdin.readline().split())
num = int(sys.stdin.readline())
word = list(map(int, sys.stdin.readline().split()))
ans = 0

word.reverse()

for i, n in enumerate(word):
  ans += n * (a ** i)
  
final = []

while ans:
  final.append(ans%b)
  ans //= b

final.reverse()
for i in final:
  print(i, end = " ")