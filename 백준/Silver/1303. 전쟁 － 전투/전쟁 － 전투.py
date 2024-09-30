n, m = map(int, input().split())
graph = []
for k in range(m):
    a = [i for i in input()]
    graph.append(a)
    a = []

visited = [[0] * n for _ in range(m)]
result = {'W':0, 'B':0}

di = [1,0,-1,0]
dj = [0, 1, 0, -1] # 우, 하, 좌, 상

def dfs(r, c, val):
    global cnt
    for k in range(4):
        ni = r + di[k]
        nj = c + dj[k]
        if 0 <= ni < m and 0 <= nj < n:
            if val == graph[ni][nj] and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                cnt += 1
                dfs(ni, nj, val)
    return cnt

for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            cnt = 1
            visited[i][j] = 1
            dfs(i, j, graph[i][j])
            result[graph[i][j]] += cnt **2
print(result['W'], result['B'])