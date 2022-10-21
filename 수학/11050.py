a,b=map(int,input().split())

def fac(num):
  total=1
  for i in range(1,num+1):
    total*=i
  return total

print(fac(a)//(fac(b)*fac(a-b)))
