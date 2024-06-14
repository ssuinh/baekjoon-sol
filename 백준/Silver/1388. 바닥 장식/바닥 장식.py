from collections import deque

def dfs(visited, row, col):
    global cnt
    visited[row][col] = 1

    if graph[row][col] == '-':
        if col < m-1:
            if graph[row][col+1] == '-' and visited[row][col+1] == 0:
                dfs(visited, row, col+1)
            else:
                cnt += 1
        else:
            cnt += 1
    else:
        if row < n-1:
            if graph[row+1][col] == '|' and visited[row+1][col] == 0:
                dfs(visited, row+1, col)
            else:
                cnt += 1
        else:
            cnt += 1
    return

n, m = map(int, input().split())
graph = []
for i in range(n):
    val = input()
    arr = []
    for j in val:
        arr.append(j)
    graph.append(arr)
visited = [[0]*m for _ in range(n)]
cnt = 0

for r in range(n):
    for c in range(m):
        if visited[r][c] == 0:
            dfs(visited, r, c)

print(cnt)