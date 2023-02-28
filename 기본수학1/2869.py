A,B,V=map(int,input().split())

# V<=(A-B)*n+A
# V-A<=(A-B)*n
# (A-B)*n<=A
# n <=A/(A-B)

n = (V-A)/(A-B)
if int(n)<n:
  n=int(n)+1
else:
  n=int(n)

if (A-B)*n+A>=V:
  n+=1
else:
  n+=2

print(n)



