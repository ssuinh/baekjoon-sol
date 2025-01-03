n = int(input())
lst = []

for i in range(n):
    lst.append(list(map(int, input().split())))

x_lst = []
y_lst = []
# 거리를 계산할 후보들 죄표 생성.
for x, y in lst:
    x_lst.append(x)
    y_lst.append(y)

final_ans = [int(1e9)] * n

for x_pnt in x_lst:
    for y_pnt in y_lst:
        ans = []
        for x, y in lst:
            dis = abs(x_pnt - x) + abs(y_pnt - y)
            ans.append(dis)

        distance = 0
        ans.sort()
        for k in range(n):
            distance += ans[k]
            if distance < final_ans[k]:
                final_ans[k] = distance

print(*final_ans)