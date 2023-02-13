def i(n):
  for i in range(2,n):
    if n%i==0:
      return 0
  
  return 1

print(i(8))