from collections import deque

import sys
input = sys.stdin.readline

di = [-1, 1, 0, 0, -1, -1, 1, 1]
dj = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(v):
    Q.append(v)
    mapp[v[0]][v[1]] = 0
    while Q:
        r, c = Q.popleft()
        for i in range(8):
            ni = r + di[i]
            nj = c + dj[i]
            if 0 <= ni < h and 0 <= nj < w and mapp[ni][nj] == 1:
                Q.append((ni, nj))
                mapp[ni][nj] = 0

result = []
while True:
    cnt = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    mapp = [list(map(int, input().split())) for _ in range(h)]

    Q = deque()
    for i in range(h):
        for j in range(w):
            if mapp[i][j] == 1:
                bfs((i, j))
                cnt += 1
    result.append(cnt)

for i in result:
    print(i)