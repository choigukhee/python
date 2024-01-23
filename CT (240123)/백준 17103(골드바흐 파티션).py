import sys

primelist = [0] * 1000001
prime = []

for i in range(2, 1000001):
  if primelist[i] == 0:
    prime.append(i)
    for j in range(i * 2, 1000001, i):
      primelist[j] = 1
      
for _ in range(int(sys.stdin.readline().rstrip())):
  count = 0
  n = int(sys.stdin.readline().rstrip())
  for i in prime:
    if i >= n:
      break
    if primelist[n - i] == 0 and i <= n-i:
      count += 1
  print(count)
    
