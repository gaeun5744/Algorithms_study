
result=[]

for _ in range(4):
    bar=[]
    N=input()
    for i in range(8):
        bar.append(int(N[i]))
    result.append(bar)


N = int(input())

for _ in range(N):
    n, m=map(int,input().split())
    n-=1
    if n == 0: #첫번재일 경우
        if m == 1: #시계방향
            if result[n][2] != result[n+1][6]:
                tmp=result[n+1].pop(0)
                result[n+1].append(tmp)
            tmp=result[n].pop()
            result[n].insert(0,tmp)

        else:
            if result[n][2] != result[n+1][6]:
                tmp=result[n+1].pop()
                result[n+1].insert(0,tmp)
            tmp=result[n].pop(0)
            result[n].append(tmp)

    elif n==3:
        if m == 1: #시계방향
            if result[n][6] != result[n-1][2]:
                tmp=result[n-1].pop(0)
                result[n-1].append(tmp)
            tmp=result[n].pop()
            result[n].insert(0,tmp)

        else:
            if result[n][6] != result[n-1][2]:
                tmp=result[n-1].pop()
                result[n-1].insert(0,tmp)
            tmp=result[n].pop(0)
            result[n].append(tmp)
    
    else:
        if m==1:
            if result[n][2] != result[n+1][6]:
                tmp=result[n+1].pop(0)
                result[n+1].append(tmp)
            

            elif result[n][6] != result[n-1][2]:
                tmp=result[n-1].pop(0)
                result[n-1].append(tmp)
            tmp=result[n].pop()
            result[n].insert(0,tmp)

        else:
            if result[n][2] != result[n+1][6]:
                tmp=result[n+1].pop()
                result[n+1].insert(0,tmp)
            elif result[n][6] != result[n-1][2]:
                tmp=result[n-1].pop()
                result[n-1].insert(0,tmp)
            tmp=result[n].pop(0)
            result[n].append(tmp)


print(1*result[0][0]+2*result[1][0]+4*result[2][0]+8*result[3][0])
print(result)