# 2차원 dp 이해가 잘안댐...!!!!!!!!!!!!!!!!!

import sys
input = sys.stdin.readline

def back(idx, weight):
    if weight > k:
        return -999999999999
    if idx == n:
        return 0
    if dp[idx][weight] != -1:
        return dp[idx][weight]

    dp[idx][weight] = max( back(idx+1, weight + lst[idx][0]) + lst[idx][1], back(idx+1, weight))

    return dp[idx][weight]

n, k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(100010)] for _ in range(n)]

ans = back(0, 0)
print(ans)