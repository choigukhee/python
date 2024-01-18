import sys
a, b = map(int, sys.stdin.readline().split())

for num in range(a,b+1):
  if num > 1:
    for i in range(2, int(num**0.5)+1):
      if num % i == 0:
        break
    else:
      print(num)