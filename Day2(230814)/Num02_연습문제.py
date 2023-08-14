#02_연습문제

#Q1
kor = 80
eng = 75
math = 55

avg = (kor + eng + math) / 3
print (avg)

#Q2
def cal(num):
  if num % 2 == 0:
    return '짝수'
  else :
    return '홀수'

result = cal(13)
print(result)

#03
pin = "881120-1068234"
yyyymmdd = pin[0:6]
num = pin[7:]
print(yyyymmdd)
print(num)

#04
pin = "881120-1068234"
print(pin[7])

#05
a = "a:b:c:d"
b = a.replace(":","#")
print(b)

#06
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

#07
a = ["Life", "is", "too", "short"]
result = a[0] + " " + a[1] + " " + a[2] + " " + a[3]
print(result)

print(f'{"or":=^10}')

result  = " ".join(a)
print(result)

#08
a = (1,2,3)
a = a+(4,)
print(a)

#09
#dictionary의 key값으로 list가 들어갈 수 없음 -> 정답 3번

#10
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

#11
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)

#12
a = b = [1,2,3]
a[1] = 4
print(b)
#[1,2,3]이 출력될 것으로 예상됨. 왜냐하면 a와 b의 주소값이 다르기 때문 => 틀림 ㅋㅋ 정답은 [1,4,3] 출력.
a = [1,2,3]
b = [1,2,3]
#이렇게 되어있을 때 a와 b의 주소값이 다름.


