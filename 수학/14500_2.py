result=[]

for _ in range(4):
    bar=[]
    N=input()
    for i in range(8):
        bar.append(int(N[i]))
    result.append(bar)


N = int(input())

for _ in range(N):
    n, m=map(int,input().split())
    n-=1
    if m==1:
      for i in range(n,3):
        if result[i][2]!=result[i+1][6]:
          tmp=result[i+1].pop(0)
          result[i+1].append(tmp)

        else:
          break
      
      if n>=1:
        for i in range(n-1,-1,-1):
          if result[i][6]!=result[i-1][2]:
            tmp=result[i-1].pop(0)
            result[i-1].append(tmp)
            
          else:
            break
      tmp=result[i].pop()
      result[i].insert(0,tmp)
    
    else:
      for i in range(n,3):
        if result[i][2]!=result[i+1][6]:
          tmp=result[i+1].pop()
          result[i+1].insert(0,tmp)

        else:
          break
      
      if n>=1:
        for i in range(n,-1,-1):
          if result[i][6]!=result[i-1][2]:
            tmp=result[i-1].pop()
            
            result[i-1].insert(0,tmp)
          
          else:
            break
      
      tmp=result[i].pop(0)
      result[i].append(tmp)


print(1*result[0][0]+2*result[1][0]+4*result[2][0]+8*result[3][0])
