import sys
input = sys.stdin.readline
def back(start, number):
    if number == m:
        print(*arr)
        return
    tmp = 0
    # 뽑은 수보다 다음 뽑을 수가 커야하는 경우 시작 범위를 조절하면 됨.
    for i in range(start, n):
        if visited[i] == 0 and tmp != lst[i]:
            arr.append(lst[i])
            visited[i] = 1
            tmp = lst[i]
            back(i, number + 1)
            visited[i] = 0
            arr.pop()

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
visited = [0] * n

arr = []
back(0, 0)

