import sys
input = sys.stdin.readline

def dfs(v):
    global visited
    if visited[v] == 0:
        visited[v] = 1

    for w in graph[v]:
        if visited[w] == 0:
            visited[w] = 1
            dfs(w)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
visited[0] = 1
cnt = 0

for i in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

while visited.count(0) > 0:
    cnt += 1
    dfs(visited.index(0))

print(cnt)