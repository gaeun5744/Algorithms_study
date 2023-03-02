T=int(input())
result=[]

for i in range(T):
  k=int(input())
  n=int(input())
  
  peo=[i for i in range(1,n+1)]


  for _ in range(k):
    for j in range(1,n):
      peo[j]+=peo[j-1]

  result.append(peo[-1])

for i in range(T):
  print(result[i])





