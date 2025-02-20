import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# dp테이블 생성
dp = [[1]*n]
for _ in range(k-1):
    dp.append([0]*n)

for i in range(k):
    dp[i][0] = i+1

# n과 k의 연관성을 따져 보았을 때 아래와 같은 점화식이 만들어짐.
# dp테이블을 만들어 연산하도록함.
for i in range(1, k):
    for j in range(1, n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[-1][-1] % 1000000000)