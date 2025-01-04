import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

prefix = [0 for _ in range(n+1)]   # 수열 요소간 차

for i in range(n):
    prefix[i+1] = max(prefix[i]+lst[i], lst[i])

prefix.pop(0)
print(max(prefix))
