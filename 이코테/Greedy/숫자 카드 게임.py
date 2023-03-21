N,M=map(int,input().split())
card=[]
result=[]

for i in range(N):
  card.append(list(map(int,input().split())))

for i in range(N):
  card[i]=sorted(card[i])

for i in range(N):
  result.append(card[i][0])

print(sorted(result)[-1])
