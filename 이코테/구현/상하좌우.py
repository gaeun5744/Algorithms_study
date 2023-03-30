num = int(input())

arr=list(input().split())

man=[1,1]

for i in arr:
  if i=="L":
    if man[1]==1:
      continue
    man[1]=-1

  elif i=="R":
    if man[1]==num:
      continue
    man[1]+=1
  
  elif i=="U":
    if man[0]==1:
      continue
    man[0]-=1

  elif i=="D":
    if man[0]==num:
      continue
    man[0]+=1

for i in man:
  print(i, end=" ")