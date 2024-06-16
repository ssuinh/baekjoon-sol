import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = []
visited = [[0]*n for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

di = [0, 1, -1, 0]
dj = [1, 0, 0, -1]

def bfs(a, b):
    Q = deque()
    Q.append((a, b))
    visited[a][b] = 'x'

    while Q:
        r, c = Q.popleft()
        for k in range(4):
            ni = r + di[k]
            nj = c + dj[k]
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 'o':
                Q.append((ni, nj))
                visited[ni][nj] = 'x'

result = 0
visited = [[0]*n for _ in range(n)]
for rain in range(101):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= rain:
                visited[i][j] = 'x'
            else:
                visited[i][j] = 'o'

    for a in range(n):
        for b in range(n):
            if visited[a][b] == 'o':
                visited[a][b] = 'x'
                cnt += 1
                bfs(a, b)

    if cnt > result:
        result = cnt

    if cnt == 0:
        print(result)
        break