A, B, C = map(int,input().split())


if B>=C:
  print(-1)
else:
  n=int(A/(C-B))
  if A+B*n<C*n:
    print(n)
  else:
    print(n+1)


