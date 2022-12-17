
n=int(input())
N=[0,1]


for i in range(n-1):
  N.append(N[i]+N[i+1])

print(N[n])