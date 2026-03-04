n = int(input())
graph = [0]
result = [0]

for i in range(n):
    graph.append(int(input()))
    
def dfs(start):
    visit[start] = True
    if not visit[graph[start]]:
        dfs(graph[start])
        
for i in range(1, n+1):
    visit = [False] * (n+1)
    dfs(i)
    result.append(visit.count(True))
    
print(result.index(max(result)))