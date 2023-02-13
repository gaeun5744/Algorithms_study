n=int(input())

if n==1:
  print(1)
else:
  n=n/6
  a=0
  tap=1

  while a<n:
    a+=tap
    tap+=1

  print(tap)




