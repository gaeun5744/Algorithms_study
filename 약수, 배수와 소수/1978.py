In=[]
result=[]
while True:
  n=int(input())
  if n==-1:
    break
  else:
    In.append(n)

for num in In:
  peo=[]
  total=0
  for i in range(1,num):
    if num%i==0:
      peo.append(i)
  for j in peo:
    total+=j
  if total==num:
    print(num,"=", end=" ")
    for i in range(len(peo)-1):
      print(peo[i],"+",end=" ")
    print(peo[-1])
  else:
    print(num,"is NOT perfect.")