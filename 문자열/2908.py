a, b=input().split()
a1=""
b1=""

for i in range(len(a)):
  a1+=a[len(a)-1-i]
  b1+=b[len(b)-1-i]

if int(a1)>int(b1):
  print(a1)
else:
  print(b1)
