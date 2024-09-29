from collections import deque

# f: 건물 층수, s: 현재 위치, g: 이동하려는 층
f, s, g, u, d = map(int, input().split())

MAX = 10**6
visit = [0]*(MAX+1)

def bfs():
    Q = deque()
    Q.append(s)
    visit[s] = 1

    while Q:
        c = Q.popleft()

        if c == g:
            return visit[c]-1

        for i in (c+u, c-d):
            if 1 <= i <= f and visit[i] == 0:
                Q.append(i)
                visit[i] = visit[c]+1
            
    return "use the stairs"

print(bfs())