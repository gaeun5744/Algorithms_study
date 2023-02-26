N=int(input())

kan=1
gap=0

while N>=kan:
  gap+=1
  kan+=gap

kan-=gap
tap=N-kan

print(kan,gap)


if gap%2==0:
  print(str(1+tap)+"/"+str(gap-tap))
else:
  print(str(gap-tap)+"/"+str(1+tap))




