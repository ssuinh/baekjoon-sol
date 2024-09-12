from collections import deque

t = int(input())
ans_lst = []

for _ in range(t):
    ans = 0

    n, m = map(int, input().split())
    Q = list(map(int, input().split()))

    r = Q[m]
    idx = m

    while(True):
        if idx == 0:   # 찾는 값의 순서일 때
            if Q[idx] < max(Q):    # 우선 순위가 아닐 경우
                w = Q.pop(0)
                Q.append(w)
                idx = n-ans-1
            else:
                ans+=1
                break

        elif Q[0] < max(Q):   # 뽑힐 값의 우선순위가 아닐경우
            w = Q.pop(0)
            Q.append(w)
            idx -= 1
        
        elif Q[0] >=max(Q):  # 뽑힐 값이 우선순위일 경우
            Q.pop(0)
            idx -= 1
            ans += 1

    ans_lst.append(ans)

for i in ans_lst:
    print(i)