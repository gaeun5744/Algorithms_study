M=int(input())
N=int(input())
result=[]

for num in range(M,N+1):
  if num>1:
    cnt=0
    for i in range(2,num):
      if num%i==0:
        cnt+=1
        break
    if cnt==0:
      result.append(num)

if len(result)==0:
  print(-1)
else:
  total=0
  for i in result:
    total+=i
  print(total)
  print(sorted(result)[0])

