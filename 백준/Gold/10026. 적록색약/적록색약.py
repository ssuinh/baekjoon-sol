import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
from collections import deque

# 정상인 판단 로직 & 색맹 그래프로 변환
def dfs(r, c, val):
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    if graph[r][c] != 2 and graph[r][c] != 1:
        if val == 'B':
            graph[r][c] = int(2)  # 방문 표시 ( B 표시 )
        else:
            graph[r][c] = int(1)  # 방문 표시 ( R, G 표시 )

        for i in range(4):
            ni = r + di[i]
            nj = c + dj[i]
            if 0 <= ni < n and 0 <= nj < n:
                if graph[ni][nj] != 2 and graph[ni][nj] != 1:
                    if graph[ni][nj] == val:
                        dfs(ni, nj, graph[ni][nj])

# 생맹 판단 로직
def dfs2(r, c, val):
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    if graph[r][c] != 0:
        graph[r][c] = int(0)

        for i in range(4):
            ni = r + di[i]
            nj = c + dj[i]
            if 0 <= ni < n and 0 <= nj < n and graph[ni][nj] != 0:
                if graph[ni][nj] == val:
                    dfs2(ni, nj, graph[ni][nj])

n = int(input())
graph = [list(input().strip()) for _ in range(n)]
ans1 = 0  # 정상
ans2 = 0  # 색맹

# 정상인 판단
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R' or graph[i][j] == 'G' or graph[i][j] == 'B':  # 방문 하지 않음
            val = graph[i][j]
            ans1 += 1
            dfs(i, j, graph[i][j])

# 색맹 판단
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 or graph[i][j] == 2:  # 방문 하지 않음
            ans2 += 1
            dfs2(i, j, graph[i][j])

print(ans1, ans2)