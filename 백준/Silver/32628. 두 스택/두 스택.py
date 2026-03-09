import sys
input = sys.stdin.readline

n, k = map(int, input().split())
bag1 = list(map(int, input().split()))
bag2 = list(map(int, input().split()))
bag1.insert(0,0)
bag2.insert(0,0)
    
for i in range(1, n+1):
    bag1[i] = bag1[i-1] + bag1[i]
for i in range(1, n+1):
    bag2[i] = bag2[i-1] + bag2[i]

result = 10**30
for i in range(n+1):
    j = 2 * n - i - k
    if 0 <= j <= n:
        result = min(result, max(bag1[i], bag2[j]))
print(result)