num = int(input())
case =[]

for i in range(num):
  case.append(list(map(int,input().split())))
  

for i in range(num):
  total_up=1
  total_down=1
  total=0
  for j in range(case[i][0]):
    total_up*=case[i][1]-j
    total_down*=case[i][0]-j
    
  total=total_up/total_down
  print(total)


