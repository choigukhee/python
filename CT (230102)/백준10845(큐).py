import sys
n = int(sys.stdin.readline())
st1 = []

for _ in range(n):
  command = list(sys.stdin.readline().split())
  
  if command[0] == 'pop':
    if st1:
      print(st1.pop(0))
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
  
  elif command[0] == 'back':  
    if st1:
      print(st1[-1])
    else:
      print(-1)
      
  else:
    st1.append(command[1])
