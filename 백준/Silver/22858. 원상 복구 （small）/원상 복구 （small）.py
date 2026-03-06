from copy import deepcopy

n, k =map(int, input().split())

s = list(map(int, input().split()))
d = list(map(int, input().split()))

# 셔플
tmp = [0 for _ in range(n)]
for _ in range(k):
    for i in range(n):
        tmp[d[i]-1] = s[i]
    s = deepcopy(tmp)

print(*tmp)
    