N, K=map(int, input().split())

peo=[]

for i in range(1,N+1):
  if N%i==0:
    peo.append(i)

  if len(peo)==K:
    break
  
if len(peo)<K:
  print(0)
else:
  print(peo[K-1])

