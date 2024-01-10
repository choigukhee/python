import sys

word = sys.stdin.readline().strip()
ans = ''
stack = []

for i in word:
  if i.isalpha():
    ans += i
  else:
    if i == '(':
      stack.append(i)
    elif i == '*' or i == '/':
      while stack and (stack[-1] == '*' or stack[-1] == '/'):
        ans += stack.pop()
      stack.append(i)
    elif i == '+' or i == '-':
      while stack and stack[-1] != '(':
        ans += stack.pop()
      stack.append(i)
    elif i == ')':
      while stack and stack[-1] != '(':
        ans += stack.pop()
      stack.pop()
      
while stack:
  ans += stack.pop()
  
print(ans)