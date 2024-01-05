import sys

st1 = ""
ans = ""
tag = False

for i in sys.stdin.readline().strip():
  
  if i == '<':
    tag = True
    ans += st1[::-1]
    st1 = ""
    ans += i
    continue
  elif i == '>':
    tag = False
    ans += i
    continue
  elif i == ' ':
    ans += st1[::-1]
    st1 = ""
    ans += i
    continue
    
  if tag:
    ans += i
  else:
    st1 += i
    
print(ans + st1[::-1])