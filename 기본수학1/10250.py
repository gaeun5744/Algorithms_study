Num=int(input())
result=[]

for i in range(Num):
  num=""
  H,W,N=map(int,input().split())

  if N%H==0:
    num="6"
  else:
    num=str(N%H)

  if N/H<=9:
    if N%H==0:
      num+="0"+str(int(N//H))
    else:
      num+="0"+str(N//H+1)
  else:
    if N%H==0:
      num+=str(int(N//H))
    else:
      num+=str(N//H+1)
    
  result.append(num)


for i in range(Num):
  print(result[i])



