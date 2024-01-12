import sys

while True:
  word = sys.stdin.readline().rstrip('\n')

  if not word:
    break
    
  lower, upper, num, space = 0, 0, 0, 0
    
  for i in word:
    if i.islower():
      lower += 1
    elif i.isupper():
      upper += 1
    elif i.isnumeric():
      num += 1
    elif i.isspace():
      space += 1

  print(lower, upper, num, space)