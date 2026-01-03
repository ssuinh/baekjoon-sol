import sys

n, m = map(int, input().split())
lst = list(map(int, input().split()))
sum_val = sum(lst[0:m])
ans = sum_val
for i in range(n-m):
    sum_val = sum_val - lst[i] + lst[i+m]
    ans = max(sum_val, ans)

print(ans)