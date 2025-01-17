import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

lst.sort()
start = 0
end = n-1
ans = (lst[0], lst[-1])
result = 99999999999999999999999

while start < end:
    tmp = lst[start] + lst[end]

    if tmp > 0:
        if abs(result) > abs(tmp):
            result = tmp
            ans = (lst[start], lst[end])
        end -= 1
    elif tmp < 0:
        if abs(result) > abs(tmp):
            result = tmp
            ans = (lst[start], lst[end])
        start += 1
    else:
        ans = (lst[start], lst[end])
        break
        
print(*ans)