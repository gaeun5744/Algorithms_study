def solution(number, k):
    answer = ''
    arr=[]
    frontMax=0

    for i in number:
      arr.append(int(i))

    sortedArr=sorted(arr)

    while k>=0:

      while "" in arr:
        arr.remove("")
      frontMax=0

      for i in range(min(k,len(arr))):
        if arr[i]!="" and frontMax<arr[i]:
          frontMax=arr[i]
      
      for i in range(min(k,len(arr))): # 젤 왼쪽 숫자 정하기
        if frontMax==arr[i]:
          break
        else:
          arr[i]=""
          k-=1
      
      for i in range(len(arr)): # 젤 왼쪽 숫자 answer로 이동
        if arr[i] == frontMax:
          answer+=str(arr[i])
          arr[i]=""
        elif arr[i]=="":
          continue
        else:
          break
    
    for i in arr:
      answer+=str(i)

    return answer


print(solution("1924",2))