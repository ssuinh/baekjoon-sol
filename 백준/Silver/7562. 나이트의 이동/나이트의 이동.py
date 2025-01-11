import sys
input = sys.stdin.readline
from collections import deque

def back(r, c):
    Q = deque()
    Q.append([r, c])

    while Q:
        r, c = Q.popleft()
        if r == end_r and c == end_c:
            print(visited[r][c] - 1)
            return

        dx = [1,-1,1,-1,2,-2,2,-2]
        dy = [-2,2,2,-2,1,-1,-1,1]
        for i in range(8):
            nx = r + dx[i]
            ny = c + dy[i]
            if 0<=nx<l and 0<=ny<l:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[r][c] + 1
                    Q.append([nx, ny])


t = int(input())
for _ in range(t):
    l = int(input())
    start_r, start_c = map(int, input().split())
    end_r, end_c = map(int, input().split())
    visited = [[0] * l for _ in range(l)]
    if start_r == end_r and start_c == end_c:
        print(0)
    else:
        visited[start_r][start_c] = 1
        back(start_r, start_c)