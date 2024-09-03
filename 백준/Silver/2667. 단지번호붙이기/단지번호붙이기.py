import sys
from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(start):
    global cnt
    Q = deque()
    Q.append(start)

    while Q:
        a, b = Q.popleft()
        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            if 0 <= ni < n and 0 <= nj < n and graph[ni][nj] == 1:
                graph[ni][nj] = 0
                Q.append((ni, nj))
                cnt += 1

n = int(input())
graph = []
result = []
danji = 0
for _ in range(n):
    arr = []
    for i in input():
        arr.append(int(i))
    graph.append(arr)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt = 1
            danji += 1
            graph[i][j] = 0
            bfs((i, j))
            result.append(cnt)

result.sort()
print(danji)
for i in result:
    print(i)