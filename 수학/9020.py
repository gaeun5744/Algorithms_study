N=int(input())
result=[]

def i(n):
  for i in range(2,n):
    if n%i==0:
      return 0
  
  return 1

for _ in range(N):
  n=int(input())
  a=int(n/2)
  b=int(n/2)
  while i(a)!=1 or i(b)!=1:
    a-=1
    b+=1
  result.append([a,b])


for k in range(N):
  print(result[k][0],result[k][1])

