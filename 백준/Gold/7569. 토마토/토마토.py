import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
from collections import deque

def bfs():
    global flag

    di = [0, 0, -1, 1, 0, 0]
    dj = [-1, 1, 0, 0, 0, 0]
    dk = [0, 0, 0, 0, 1, -1]

    while Q:
        r, c, v = Q.popleft()

        for i in range(6):
            ni = r + di[i]
            nj = c + dj[i]
            nk = v + dk[i]
            if 0 <= ni < h and 0 <= nj < n and 0 <= nk < m:
                if graph[ni][nj][nk] == 0:
                    Q.append((ni, nj, nk))
                    graph[ni][nj][nk] = graph[r][c][v] + 1

m, n, h = map(int, input().split())

graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

flag = False
Q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:  # 방문하지 않고 익은 토마토가 있는 곳이라면 bfs 호출
                Q.append((i, j, k))
                graph[i][j][k] = 2
bfs()

val = 0
for i in graph:
    for j in i:
        if 0 in j:
            flag = True
        else:
            val = max(max(j), val)

if flag:
    print(-1)
else:
    print(val-2)