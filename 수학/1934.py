num = int(input())
result=[]

for i in range(num):

  a,b=map(int,input().split())
  k=[]
  total=1

  
  for j in range(1,max(a+1,b+1)):
    if((a%j==0) and (b%j==0)):
      k.append(j)
      a = a//j
      b = b//j
      
  for l in range(len(k)):
    total*=k[l]
  
  total*=a*b

  result.append(total)

for i in range(len(result)):
  print(result[i])