import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
ans = 500
for i in range(n):
    tmp =[]
    for w in input().rstrip():
        tmp.append(w)
    graph.append(tmp)

def find(r, c):
    global ans
    cnt_b=0
    cnt_w=0

    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 1:
                if graph[r+i][j+c] != "B":
                    cnt_w += 1
                if graph[r+i][j+c] != "W":
                    cnt_b += 1
            else:
                if graph[r+i][j+c] != "B":
                    cnt_b += 1
                if graph[r+i][j+c] != "W":
                    cnt_w += 1

    ans = min(cnt_b, cnt_w, ans)

for i in range(n-7):
    for j in range(m-7):
        find(i, j)

print(ans)