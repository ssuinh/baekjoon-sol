import sys
from collections import deque

di = [1,-1,0,0]
dj = [0, 0, 1, -1]
def bfs(x, y, cnt):
    global ans
    Q = deque()
    Q.append((x, y, cnt))

    if x == n-1 and y == m-1:
        ans = min(ans, cnt)

    while Q:
        tmp = Q.popleft()
        for i in range(4):
            ni = tmp[0] + di[i]
            nj = tmp[1] + dj[i]
            if 0 <= ni < n and 0 <= nj < m:
                if graph[ni][nj] == 1:
                    if ni == n-1 and nj == m-1:
                        ans = tmp[2]+1
                    Q.append((ni, nj, tmp[2]+1))
                    graph[ni][nj] = 3


n, m = map(int, input().split())
graph = [[int(i) for i in input()] for _ in range(n)]
ans = 99999999999999
bfs(0, 0, 1)
print(ans)
