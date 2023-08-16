coffee = 10
money = 500

while True:
  if money == 300:
    print("커피를 줍니다")
    money = money -300
    coffee = coffee - 1
  elif money > 300:
    print("거스름돈 %d를 주고 커피를 줍니다" %(money - 300)) 
    money = money -300
    coffee = coffee - 1
  else:
    print("커피를 주지 않습니다")
    print("남은 커피의 개수는 %d개 입니다." %coffee)
    break