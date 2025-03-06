x_lst = []
y_lst = []

for i in range(3):
    x, y = list(map(int, input().split()))
    x_lst.append(x)
    y_lst.append(y)

for i in x_lst:
    if x_lst.count(i) == 1:
        result_x = i

for j in y_lst:
    if y_lst.count(j) == 1:
        result_y = j

print(result_x, result_y)