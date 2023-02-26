N=int(input())

kan=1
gap=0

while N>kan:
  gap+=1
  kan+=gap

kan-=gap
tap=N-kan
print(str(1+gap-tap)+"/"+str(1+tap))





