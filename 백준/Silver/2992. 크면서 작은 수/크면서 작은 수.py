import copy
import sys
input = sys.stdin.readline

def back(number):
    global min_num
    global flag

    # x보다 큰 수라면 정지
    if number == len(lst):  # 숫자를 완성
        result = 0
        for i in range(len(lst)):
            result += int(ans[i]) * 10 ** (len(lst) - i - 1)
        if x < result < min_num:
            min_num = result
            flag = True

    for i in range(len(lst)):
        if visited[i] == 0:  # 방문하지 않았다면 추가
            ans.append(sorted_lst[i])
            visited[i] = 1
            back(number + 1)
            visited[i] = 0
            ans.pop()

x = int(input())

lst = []
for i in str(x):
    lst.append(i)
first_num = lst[0]

sorted_lst = copy.deepcopy(lst)
sorted_lst.sort()
ans = []
min_num = x * 10 ** 99
visited = [0] * len(lst)

flag = False
back(0)

if not flag:
    print(0)
else:
    print(min_num)
