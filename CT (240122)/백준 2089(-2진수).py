import sys
f
def divide(n, ans):
  if n == 0:
    ans.append(0)
    return
  if n == 1:
    ans.append(1)
    return
  if n % 2 == 0:
    ans.append(0)
    divide(n // -2, ans)
  elif n < 0:
    ans.append(1)
    divide((n // -2) + 1, ans)
  else:
    ans.append(1)
    divide((n // -2) + 1, ans)
    
num = int(sys.stdin.readline().rstrip())
ans = []
divide(num, ans)
ans.reverse()
print(int(''.join(map(str,ans))))