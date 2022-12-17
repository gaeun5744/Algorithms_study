n=int(input())
N=list(map(int,input().split()))
N.sort()


if N[n-1]%2==0:
  print(N[n-1]*2)
else:
  print(N[n-1]*N[n-2])
  

