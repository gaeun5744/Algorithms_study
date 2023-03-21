N,M,K=map(int,input().split())
arr=[]
total=0
count=0


arr=list(map(int,input().split()))

arr=sorted(arr)

while(True):
    for i in range(K):
      total+=arr[-1]
      count+=1
      if count==M:
        break
    total+=arr[-2]
    count+=1
    if count==M:
      break

print(total)