import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    if lst[i-1] > lst[i]:
        lst[i-1] = lst[i]

print(sum(lst))