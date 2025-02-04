import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
ans = 1

r = min(n, m)

# 전체 그래프 순회
for i in range(n-1):
    for j in range(m-1):
        num = graph[i][j]
        
        # 전체 그래프의 짧은 변의 크기만큼 거리에서부터 거꾸로 탐색(불필요한 연산 최소화)
        for k in range(j+r-1, j, -1):
            if k < m:
                if graph[i][k] == num:
                    l = k-j  # 정사각형 한변의 크기
                    if 0 < i+l < n and 0 < j+l < m:
                        if graph[i+l][j] == num and graph[i+l][j+l] == num:
                            ans = max(ans, (l+1)**2)
print(ans)