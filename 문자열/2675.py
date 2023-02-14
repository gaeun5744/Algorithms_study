case=int(input())
num=list()

for i in range(case):
  total=""
  a,b=input().split()
  for j in b:
    total+=j*int(a)
  num.append(total)


for i in num:
  print(i)