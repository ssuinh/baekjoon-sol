import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
x = int(input())

lst.sort()
ans = 0
left, right = 0, n-1

while left < right:
    if (lst[left] + lst[right]) == x:
        ans += 1
        left += 1
    elif (lst[left] + lst[right]) < x:
        left += 1
    else:
        right -= 1
print(ans)