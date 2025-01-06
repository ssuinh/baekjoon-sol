# 배열에서 이전 값 사용하는 경우 범위 고려하지 않기 위해 첫 행, 열에 0으로 채우는 방식 !
# 완탐 시간초과 => dp풀이

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
prefix = [[0] * (n+1) for _ in range(n+1)]

# # prefix 만들기
for i in range(1, n+1):
    for j in range(1, n+1):
        prefix[i][j] = lst[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    ans = prefix[x2][y2] - prefix[x2][y1-1] - prefix[x1-1][y2] + prefix[x1-1][y1-1]

    print(ans)