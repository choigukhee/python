n = input()
mylist = list(map(int, input().split()))
M = max(mylist)
sum = sum(mylist)

print(sum*100/M/int(n))