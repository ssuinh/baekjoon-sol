import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
D = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            D[i] = max(D[i], D[j] + 1)

print(max(D))