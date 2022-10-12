num=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))

A=sorted(A)
B=sorted(B)
B=list(reversed(B))

total=0

for i in range(num):
  total+=A[i]*B[i]

print(total)
