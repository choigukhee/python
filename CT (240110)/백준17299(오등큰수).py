import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
stack =[]
frequency = {}
NGE = [-1] * n

for num in l:
  if num in frequency:
    frequency[num] += 1
  else:
    frequency[num] = 1
    
for i in range(n):
  while stack and frequency[l[stack[-1]]] < frequency[l[i]]:
    NGE[stack.pop()] = l[i]
  stack.append(i)
  
print(*NGE)