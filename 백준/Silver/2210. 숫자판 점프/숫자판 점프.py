import sys
input = sys.stdin.readline

def back(number, r, c, tmp):
    if number == 6:
        if tmp not in ans:
            ans.append(tmp)
        return

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if 0<=nx<5 and 0<=ny<5:
            back(number+1, nx, ny, tmp + [lst[nx][ny]])

lst = [list(map(int, input().split())) for _ in range(5)]
ans = []
for i in range(5):
    for j in range(5):
        back(1, i, j, [lst[i][j]])

print(len(ans))