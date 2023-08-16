money = True
if money:
  print("택시를 타고 가라")
else:
  print("걸어 가라")
  
print(2>4)

money = 2000
if money >= 3000:
  print("택시를 타라")
else:
  print("걸어가라")
  
print(1 in [1,2,3])
print(4 not in [1,2,3])

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
  print("택시를 타고가라")
else:
  print("걸어가라")

if 'card' not in pocket:
  print("걸어가라")
else:
  print("버스를 타고 가라")
  
if 'cellphone' not in pocket:
  pass
else:
  print("전화해라")
  
if 'money' in pocket:
  print("택시를 타라")
elif 'card' in pocket:
  print("택시를 타라")
else:
  print("걸어가라")
  
  