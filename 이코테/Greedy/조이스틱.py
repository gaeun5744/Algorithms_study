def solution(name):
    answer = 0
    A=""

    alpha1=["A","B","C","D","E","F","G","H","I","J",
    "K","L","M"]
    alpha2=["N","O","P","Q","R","S","T","U","V","W",
    "X","Y","Z"]

    after=0
    before=0

    for i in range(1,len(name)):
      if name[i]=="A":
        after+=1
      else:
        break

    for i in range(1,len(name)):
      if name[-i]=="A":
        before+=1
      else:
        break

    if after>before: #start left
      for al in name:
        if al in alpha1:
          answer+=alpha1.index(al)
        else:
          answer+=13-alpha2.index(al)

      answer+=len(name)-1-after

    else:
      for al in name:
        if al in alpha1:
          answer+=alpha1.index(al)
        else:
          answer+=13-alpha2.index(al)
      answer+=len(name)-1
    
    for i in range(1,len(name)+1):
        if name[-i]=="A":
          answer-=1
        else:
          break

    return answer

print(solution("AAANAAA"))

