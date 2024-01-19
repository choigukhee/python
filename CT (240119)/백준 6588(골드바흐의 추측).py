import sys

prime = []
primeList = [0] * 1000001

for i in range(2, 1000001):
  if primeList[i] == 0:
    prime.append(i)
    for j in range(i*2, 1000001, i):
      primeList[j] = 1
      
while True:
  n = int(sys.stdin.readline())
  if n == 0:
    break
  for i in range(1,len(prime)):
    if primeList[n - prime[i]] == 0:
      print(f'{n} = {prime[i]} + {n - prime[i]}')
      break