N=int(input())
nums=list(map(int,input().split()))
count=0

for num in nums:
  c=0
  if num==1:
    continue
  for i in range(2,num):
    if num%i==0:
      c+=1
  if c==0:
    count+=1

print(count)

