N=int(input())
result=[]

three=N//3
five=N//5

for i in range(three+1):
  for j in range(five+1):
    if 3*i+5*j==N:
      result.append(int(i+j))

result=sorted(result)

if len(result)>=1:
  print(result[0])
else:
  print(-1)


