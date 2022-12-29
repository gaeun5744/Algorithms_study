A, B, C = map(int,input().split())

n=0

if B>=C:
  print(-1)

while A+B*n>=C*n:
  n+=1

print(n)
