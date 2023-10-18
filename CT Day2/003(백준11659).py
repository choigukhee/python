import sys
input = sys.stdin.readline
dnum, qnum = map(int, input().split())
baseList = list(map(int, input().split()))
sumList = [0]
temp = 0

for i in baseList:
  temp += i
  sumList.append(temp)
  
for i in range(qnum):
  numI, numJ = map(int, input().split())
  print(sumList[numJ]-sumList[numI-1])