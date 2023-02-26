N=int(input())
list=[]

for i in range(N):
  list.append(input())

alSet=set(list)

for word in list:
  after=" "
  for i in word:
    if after[-1]!=i and i in after:
      N-=1
      break
    else:
      after+=i

print(N)