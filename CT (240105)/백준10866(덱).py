import sys
from collections import deque

st1 = deque()

for _ in range(int(sys.stdin.readline())):
  command = list(sys.stdin.readline().split())
  
  if command[0] == 'push_front':
    st1.appendleft(command[1])
  elif command[0] == 'push_back':
    st1.append(command[1])
  elif command[0] == 'pop_front':
    if st1:
      print(st1[0])
      st1.popleft()
    else:
      print(-1)
  elif command[0] == 'pop_back':
    if st1:
      print(st1[-1])
      st1.pop()
    else:
      print(-1)
  elif command[0] == 'size':
    print(len(st1))
  elif command[0] == 'empty':
    if st1:
      print(0)
    else:
      print(1)
  elif command[0] == 'front':
    if st1:
      print(st1[0])
    else:
      print(-1)
  else:
    if st1:
      print(st1[-1])
    else:
      print(-1)