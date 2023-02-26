N=int(input())
total=0

for number in range(1,N+1):
  number=str(number)
  if len(number)<=2:
    total+=1
  elif len(number)==3:
    if int(number[1])-int(number[0])==int(number[2])-int(number[1]):
      total+=1
  elif len(number)==4:
    if int(number[1])-int(number[0])==int(number[2])-int(number[1]) and int(number[2])-int(number[1])==int(number[3])-int(number[2]):
      total+=1

print(total)






