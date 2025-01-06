import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
# lst = deque()
lst = [list(map(int, input().split())) for _ in range(n)]


lst.sort(key=lambda x:x[0])  # 2차원 리스트 행에 대해 오름차순 정렬
# print(lst)

height_lst = deque()
for i in lst:
    height_lst.append(i[1])

ans = 0
stop_point = height_lst.index(max(height_lst))

if stop_point == 0: # 내림차순 계단형
    tmp = lst[-1][1]
    location = lst[-1][0]
    for i in range(n-2, stop_point-1, -1):
        ans += ( abs(lst[i][0] - location) ) * tmp

        if lst[i][1] > tmp:
            tmp = lst[i][1]
        location = lst[i][0]

elif stop_point == -1:
    tmp = [0][1]
    location = lst[0][0]
    for i in range(1, stop_point):
        ans += (lst[i][0] - location) * tmp

        if lst[i][1] > tmp:
            tmp = lst[i][1]
        location = lst[i][0]

else:  # 최고 층수가 가운데 일 경우
    tmp = lst[0][1]
    location = lst[0][0]
    for i in range(1, stop_point+1):
        ans += (lst[i][0]-location ) * tmp
        if lst[i][1] > tmp:
            tmp = lst[i][1]
        location = lst[i][0]

    tmp = lst[-1][1]
    location = lst[-1][0]

    for i in range(n-2, stop_point-1, -1):
        ans += (abs(lst[i][0] - location)) * tmp
        if lst[i][1] > tmp:
            tmp = lst[i][1]
        location = lst[i][0]

ans += max(height_lst)
print(ans)
