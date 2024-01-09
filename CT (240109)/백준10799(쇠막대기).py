import sys

bar = sys.stdin.readline().strip()
stack = []
cnt = 0

for i in range(len(bar)):
  if bar[i] == "(":
    stack.append("(")
    
  else:
    if bar[i-1] == "(":
      stack.pop()
      cnt += len(stack)
    else:
      stack.pop()
      cnt += 1

print(cnt)