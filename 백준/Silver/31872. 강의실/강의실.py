import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = [0] + list(map(int, input().split()))

lst.sort()
gap = []
for i in range(n):
    tmp = lst[i+1] - lst[i]
    gap.append(tmp)

gap.sort()
print(sum(gap[:n-k]))