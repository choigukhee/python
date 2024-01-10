import sys

n = int(sys.stdin.readline())
word = sys.stdin.readline().strip()
num_lst = [0] * n
stack = []

for i in range(n):
  num_lst[i] = int(sys.stdin.readline())

for i in word:
  if 'A' <= i <= 'Z':
    stack.append(num_lst[ord(i) - ord('A')])
  else:
    str2 = stack.pop()
    str1 = stack.pop()
    
    if i == '+':
      stack.append(str1 + str2)
    elif i == '-':
      stack.append(str1 - str2)
    elif i == '*':
      stack.append(str1 * str2)
    elif i == '/':
      stack.append(str1 / str2)  
      
print('%.2f' % stack[0])