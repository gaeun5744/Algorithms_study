call=["0","0","0","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]

word=input()

total=0
for i in word:
  for j in call:
    if i in j:
      total+=call.index(j)

print(total)

