import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()
cnt = 0
def dfs(node):
    global cnt
    cnt += 1
    visit[node] = cnt
    
    for i in graph[node]:
        if visit[i] == 0:
            dfs(i)
            
dfs(r)
for i in range(1, n+1):
    print(visit[i])