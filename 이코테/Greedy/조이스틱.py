def solution(name):
    answer = 0
    rightAnswer=0
    leftAnswer=0
    A=""

    for i in range(len(name)//2):
      A+="A"

    alpha1=["A","B","C","D","E","F","G","H","I","J",
    "K","L","M"]
    alpha2=["N","O","P","Q","R","S","T","U","V","W",
    "X","Y","Z"]

    for al in name:
        if al in alpha1:
          answer+=alpha1.index(al)
        else:
          answer+=13-alpha2.index(al)


    # right
    rightAnswer=len(name)-1
    for i in range(1,len(name)):
      if name[-i]=="A":
        rightAnswer+=1
      else:
        break
    
    # else 예시 : JAAAAN
    # 왔다갔다
    nameCopy=name.copy()
    if A in nameCopy:
      nameCopy=nameCopy.split(A,"")
    rightleft= i
    



    return answer

print(solution("AAANAAA"))

