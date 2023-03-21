def solution(n, lost, reserve):
    answer = 0

    lostCopy=lost.copy()
    reserveCopy=reserve.copy()
    for i in lostCopy:
        for j in reserveCopy:
            if i==j:
                lost.remove(i)
                reserve.remove(i)

    lostCopy=sorted(lost.copy())
    reserveCopy=sorted(reserve.copy())



    for i in lostCopy:
        for j in reserveCopy:
            if i == j+1 or i == j-1:
                if i in lost and j in reserve:
                    reserve.remove(j)
                    lost.remove(i)


    answer=n-len(lost)
    
    
    return answer

print(solution(10,[1,2,3,4],[1,3,5,7]))