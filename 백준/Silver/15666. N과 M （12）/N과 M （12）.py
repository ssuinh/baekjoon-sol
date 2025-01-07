import sys
input = sys.stdin.readline
def back(start, number):
    if number == m:
        print(*arr)
        return
    tmp = 0
    # 이미 뽑은 수와 중복 체크하던 visited 삭제
    for i in range(start, n):
        if tmp != lst[i]:
            arr.append(lst[i])
            tmp = lst[i]
            back(i, number + 1)
            arr.pop()

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

arr = []
back(0, 0)