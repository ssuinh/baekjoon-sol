# 이모스법
# 누적합

import sys
input = sys.stdin.readline

n, h = map(int, input().split())
cave = [0] * (h+1)

for i in range(n):
    l = int(input())
    if i % 2 == 0:  # 왼
        cave[0] += 1
        cave[l] -= 1
    else:  # 오
        cave[-1] -= 1
        cave[-1-l] += 1

cave.pop()
result = []
tmp = 0
for i in cave:
    tmp += i
    result.append(tmp)

ans = min(result)
print(ans, result.count(ans))