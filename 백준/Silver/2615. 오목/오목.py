import sys
input = sys.stdin.readline

# 오목 시작 돌이 0,0일 경우 이전 돌 확인 시 편하게 첫 행, 모든 행의 첫 열에 0 추가
graph = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
for i in range(19):
    tmp = [0]
    tmp+=(list(map(int, input().split())))
    graph.append(tmp)

# 좌하, 하, 우하, 우 체크에서
# 하, 우하, 우, 우상 방향으로 수정함 (가장 왼쪽의 인덱스를 답으로 출력하라는 조건 떄문)
di = [1, 1, 0, -1]
dj = [0, 1, 1, 1]

flag = False
for i in range(1, 20):
    for j in range(1, 20):
        if graph[i][j] == 1 or graph[i][j] == 2:
            tmp = graph[i][j]
            # 8방향 중 4방향에 같은 색 체크
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                # 발견한 방향으로 이전 돌이 같은 색이 아니어야함.
                # 같은 방향으로 5개의 돌이 같아야함.
                if 0 <= ni < 20 and 0 <= nj < 20 and graph[ni][nj] == tmp and 0 <= i-di[k] < 20 and 0 <= j-dj[k] < 20 and graph[i-di[k]][j-dj[k]] != tmp:
                    if 0 <= ni+di[k] < 20 and 0 <= nj+dj[k] < 20 and graph[ni+di[k]][nj+dj[k]] == tmp:
                        if 0 <= ni+di[k]*2 < 20 and 0 <= nj+dj[k]*2 < 20 and graph[ni+di[k]*2][nj+dj[k]*2] == tmp:
                            if 0 <= ni+di[k]*3 < 20 and 0 <= nj+dj[k]*3 < 20 and graph[ni+di[k]*3][nj+dj[k]*3] == tmp:
                                # 5개까지 색이 같고 6번째 돌은 달라야함.
                                if 0 <= ni + di[k] * 4 < 20 and 0 <= nj + dj[k] * 4 < 20 and graph[ni + di[k] * 4][nj + dj[k] * 4] == tmp:
                                    continue
                                else:
                                    flag = True
                                    print(tmp)
                                    print(i, j)
                                    break

if flag == False:
    print(0)
