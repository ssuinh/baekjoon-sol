import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
sum_val = sum(arr[:k])
pre_idx = 0
max_val = sum_val

for i in range(n-k):
    sum_val = sum_val - arr[pre_idx] + arr[i+k]
    pre_idx += 1
    if sum_val >= max_val:
        max_val = sum_val

print(max_val)