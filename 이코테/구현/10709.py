H,W=map(int,input().split())
sky=[]
arr=[]
answer=[[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
  cl=input()
  for j in range(W):
    arr.append(cl[j])
  sky.append(cl)


for i in range(H):
  cnt=1
  cloud=False
  for j in range(W):
    if not cloud and sky[i][j]==".": # 가로줄에 구름이 없을 경우
      answer[i][j]=-1

    elif sky[i][j]=="c":
      cloud=True # 가로줄에 구름이 존재한다고 표시
      answer[i][j]=0
      cnt=1

    elif cloud and sky[i][j]==".": # 가로줄에 구름이 있고, . 일 경우
      answer[i][j]=cnt
      cnt+=1


for i in answer:
    print(*i, end=' ')
    print()






