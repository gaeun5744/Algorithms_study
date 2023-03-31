N=int(input())
goal=[]
answer=[]

oneCount=0
twoCount=0

oneTime=[0,0] #min,sec
twoTime=[0,0]


def time(time1, time2):
  time1=time1.split(":")
  time2=time2.split(":")

  time=[0,0]

  time[0]=int(time2[0])-int(time1[0])
  time[1]=int(time2[1])-int(time1[1])

  if time[1]<0:
    time[0]-=1
    time[1]=int(time2[1])+60-int(time1[1])
    

  return time[0],time[1]



for i in range(N):
  goal.append(list(input().split()))

goal.append([0,"48:00"])

for i in range(N):
  if goal[i][0] == "1":
    oneCount+=1
  if goal[i][0] == "2":
    twoCount+=1

  if oneCount>twoCount:
    num1=goal[i][1]
    num2=goal[i+1][1]
    num1,num2=time(num1,num2)
    oneTime[0]+=num1
    oneTime[1]+=num2

  if oneCount<twoCount:
    num1=goal[i][1]
    num2=goal[i+1][1]
    num1,num2=time(num1,num2)
    twoTime[0]+=num1
    twoTime[1]+=num2


if oneTime[1]>60:
  oneTime[0]+=int(oneTime[1]//60)
  oneTime[1]=int(oneTime[0]%60)


if twoTime[1]>60:
  twoTime[0]+=int(twoTime[1]//60)
  twoTime[1]=int(twoTime[0]%60)


print(str(oneTime[0]).zfill(2)+":"+str(oneTime[1]).zfill(2))
print(str(twoTime[0]).zfill(2)+":"+str(twoTime[1]).zfill(2))

