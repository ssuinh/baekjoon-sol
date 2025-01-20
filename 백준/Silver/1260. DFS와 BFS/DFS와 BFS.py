import sys
input = sys.stdin.readline
from collections import deque

def dfs(start, visited):
    if graph[start]:
        for i in graph[start]:
            if not visited[i]:
                visited[i] = 1
                dfs_r.append(i)
                dfs(i, visited)
            else:
                continue
    else:
        return
    return

def bfs(start):
    visited= [0] * (n+1)
    Q = deque()
    Q.append(start)
    visited[start] = 1

    while Q:
        tmp = Q.popleft()
        bfs_r.append(tmp)

        for i in graph[tmp]:
            if not visited[i]:
                Q.append(i)
                visited[i] = 1
    print(*bfs_r)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [0] * (n+1)
dfs_r = [v]
bfs_r = []
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()
visit[v] = 1
dfs(v, visit)
print(*dfs_r)
bfs(v)