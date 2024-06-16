import sys
from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(start):
    global result
    Q = deque()
    Q.append(start)
    while Q:
        a, b = Q.popleft()
        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            if 0 <= ni < m and 0 <= nj < n and graph[ni][nj] == 0:
                graph[ni][nj] = 1
                Q.append((ni, nj))
                if ni == m-1:
                    result = 'YES'
                    return

m, n = map(int, input().split())
graph = []
result = 'NO'
for _ in range(m):
    arr = []
    for i in input():
        arr.append(int(i))
    graph.append(arr)

for i in range(n):
    if graph[0][i] == 0:
        graph[0][i] = 1
        bfs((0, i))
print(result)