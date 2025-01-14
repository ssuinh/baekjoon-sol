import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# start == 1, end == 가장 긴 끈의 길이

def binary_search(start, end):
    global result
    global mid
    if start > end:
        print(result)
        return
    else:
        mid = (start + end) // 2
        cnt = 0
        for i in lst:
            cnt += i // mid

        # 선의 갯수가 적을 경우 => 길이를 줄여야함.
        if cnt < n:
            binary_search(start, mid-1)
        elif cnt >= n:
            result = mid
            binary_search(mid+1, end)

lst = []
k, n = map(int, input().split())
for i in range(k):
    lst.append(int(input()))
result = 0
mid = 0
binary_search(1, max(lst))