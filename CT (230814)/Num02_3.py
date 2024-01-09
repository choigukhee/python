# 02_3 리스트 자료형

a = [1,2,['a','b',['life','is']]]
print(a[2][2][0])
print(a[0:2])

A = [1,2,3,4,5]
print(A[1:3])
print(len(A))
print(str(A[0]))
print(A)
A[3] = 8
print(A)
del A[3]
print(A)
A.append(9)
A.append(4)
print(A)
A.sort()
print(A)
A.reverse()
print(A)
print(A.index(1))
A.insert(0,3)
print(A)
A.remove(3)
print(A)
A.pop()
print(A)
print(A.count(3))