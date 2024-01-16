import sys
str = sys.stdin.readline().rstrip()
word = []

for i in str:
  if i.isalpha():
    if i.isupper():
      word.append(chr((ord(i) - 65 + 13) % 26 + 65))
    else:
      word.append(chr((ord(i) - 97 + 13) % 26 + 97))
  else:
    word.append(i)
    
print(''.join(word))