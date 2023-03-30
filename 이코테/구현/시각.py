num=int(input())
tap=15*60+15*60-15*15
answer=0

for i in range(num+1):
  if "3" in str(i) or "6" in str(i) or "9" in str(i):
    print(i)
    answer+=60*60

  else:
    answer+=tap


print(answer)

