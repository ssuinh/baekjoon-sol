def back(result):
    if len(result) == 6:
        print(*result)
        return
    
    for i in range(k):
        if len(result) != 0:
            if visit[i] == 0 and result[-1] < s[i]:
                result.append(s[i])
                visit[i] = 1
                back(result)
                result.pop()
                visit[i] = 0
        else:
                result.append(s[i])
                visit[i] = 1
                back(result)
                result.pop()
                visit[i] = 0
cnt = 0

while True:
    s = list(map(int, input().split()))
    k=s.pop(0)
    visit = [0] * k
    if k == 0:
        break

    if cnt != 0:
        print('')

    back([])
    cnt +=1
