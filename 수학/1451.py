depArr=input().split("-")
calArr=[]

for i in depArr:
  if '+' in i:
    plusTotal=0
    plusArr=i.split("+")
    for j in plusArr:
      plusTotal+=int(j)
    calArr.append(plusTotal)

  else:
    calArr.append(int(i))

sum=calArr.pop()
for k in calArr:
  sum-=k

print(sum)
  


