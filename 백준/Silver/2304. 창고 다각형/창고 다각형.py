# 증가하는 로직으로만 구하기 위해서 최고점을 기준으로 구간합. 누적합을 사용한것..?

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
# lst = deque()
lst = [list(map(int, input().split())) for _ in range(n)]

lst.sort(key=lambda x:x[0])  # 2차원 리스트 행에 대해 오름차순 정렬 (위치 순으로 정렬)

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

elif stop_point == -1:   # 오름차순 계단형
    tmp = [0][1]
    location = lst[0][0]
    for i in range(1, stop_point):
        ans += (lst[i][0] - location) * tmp

        if lst[i][1] > tmp:
            tmp = lst[i][1]
        location = lst[i][0]

else:  # 최고 층수가 가운데 일 경우
    # 최고층수 기준 왼쪽 (증가하는 부분)
    tmp = lst[0][1]
    location = lst[0][0]
    for i in range(1, stop_point+1):
        ans += (lst[i][0]-location ) * tmp
        if lst[i][1] > tmp:
            tmp = lst[i][1]
        location = lst[i][0]

    # 최고층수 기준 오른쪽 ( 감소하는 부분)
    tmp = lst[-1][1]
    location = lst[-1][0]

    # 증가하는 부분과 같은 논리로 풀이하기 위해서 역순으로 반복
    for i in range(n-2, stop_point-1, -1):
        ans += (abs(lst[i][0] - location)) * tmp
        if lst[i][1] > tmp:
            tmp = lst[i][1]
        location = lst[i][0]  # 위치 갱신

ans += max(height_lst)   # 다음 위치에서 이전까지의 위치 층수를 더하는 풀이임으로 반복문의 마지막(최댓값) 층수를 포함하지 않음. 따라서 마지막에 더해줌.
print(ans)
