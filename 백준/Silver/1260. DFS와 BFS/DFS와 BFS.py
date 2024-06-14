from collections import deque

def dfs(q):
    global result_dfs
    visited[q] = 1
    result_dfs.append(q)
    for w in graph[q]:
        if visited[w] == 0:
            dfs(w)

def bfs(q):
    global result_bfs
    while Q:
        c = Q.popleft()
        result_bfs.append(c)
        for w in graph[c]:
            if visited[w] == 0:
                Q.append(w)
                visited[w] = 1

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
result_dfs = []
result_bfs = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:   # 숫자가 작은 노드부터 방문하므로 오름차순 정렬.
    i.sort()

dfs(v)
print(*result_dfs)

visited = [0] * (n+1)
visited[v] = 1
Q = deque([v])
bfs(v)
print(*result_bfs)