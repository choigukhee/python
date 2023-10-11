#Q1
#shirt 출력

#Q2
result = 0
i = 1
while i <= 1000:
  if i % 3 ==0:
    result += i
  i+=1
print(result)

#Q3
i = 1 
while i<6:
  print("*" * i )
  i+=1
  
#Q4
for i in range(1,101):
  print(i)
  
#Q5
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
  total += score
avg = total / len(A)
print(avg)

#Q6
numbers = [1,2,3,4,5]
result = [n*2 for n in numbers if n%2 ==1]
print(result)

def solution(array):
    sorted(array)
    i = len(array) // 2 
    answer = array[i]
    return answer
  
array = [3,1,5]
print(solution(array))
