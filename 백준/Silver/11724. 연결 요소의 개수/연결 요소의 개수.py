from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    Q = deque()
    Q.append(start)
    visited[start] = 1   # 방문 표시

    while Q:
        val = Q.popleft()
        for node in graph[val]:
            if visited[node] == 0:
                Q.append(node)
                visited[node] = 1


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
result = 0

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    if visited[i] == 0:  # 방문하지 않은 노드가 있다면 bfs 호출
        bfs(i)
        result += 1
print(result)