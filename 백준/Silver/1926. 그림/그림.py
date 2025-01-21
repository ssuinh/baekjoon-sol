import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
from collections import deque

def dfs(r, c):
    global square, ans

    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    if graph[r][c] == 1:
        square += 1
        graph[r][c] = 7
        for i in range(4):
            ni = r+di[i]
            nj = c+dj[i]
            if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] == 1:
                dfs(ni, nj)

        else:
            ans = max(square, ans)   # 그림 면적
            return

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ans = 0   # 그림 면적 최댓 값
count = 0   # 그림 수

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            square = 0   # 탐색하고 있는 영역의 넓이
            count += 1
            dfs(i, j)

print(count)
print(ans)