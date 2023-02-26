N=int(input())
bang=0
gap=1


while True:
  if N>bang*6+1:
    bang+=gap
    gap+=1
  else:
    break

print(gap)



