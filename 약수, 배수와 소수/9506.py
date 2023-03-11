N=int(input())
nums=list(map(int,input().split()))

for num in nums:
  if num==1 or num==2:
    N-=1
    continue
  for i in range(2,num):
    if num%i==0:
      N-=1
      break

print(N)



