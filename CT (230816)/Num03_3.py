test_list = ['one', 'two', 'three']

for i in test_list:
  print(i)
  
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
  number += 1
  if mark >= 60:
    print("%d번 학생은 합격입니다" %number)
  else:
    print("%d번 학생은 불합격입니다" %number)
    

add = 0
for i in range(1, 11):
  add += i
print(add)
  
for number in range(len(marks)):
  if marks[number] >= 60:
    print("%d번 학생은 합격입니다" %(number+1))
    
num = 0
for i in range(1,101):
  num += i
print(num)


for i in range(2, 10):
  for j in range(1, 10):
    num = i * j
    print ("%d * %d = %d" %(i, j, num))
    
