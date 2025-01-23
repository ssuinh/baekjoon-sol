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
            # 익은 토마토 주위 토마토가 먼저 익어야함으로 익은 토마토 좌표를 큐에 먼저 다 넣어야함.
            if graph[i][j][k] == 1:
                    Q.append((i, j, k))
                    graph[i][j][k] = 2
bfs()

val = 0
# 탐색 끝난 그래프 순회하여 값 판단.
for i in graph:
    for j in i:
        if 0 in j:   # 안익은 토마토 존재
            flag = True
        else:    # 안익은 토마토 없음. 최소 날짜 저장.
            val = max(max(j), val)

if flag:   # 안익은 토미토 존재
    print(-1)
else:    # 안익은 토마토 없음. 모두 익히는데 필요한 최소 날짜 출력.
    print(val-2)
