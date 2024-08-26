start, end = map(int, input().split())
result = end
cnt = 1

while start != result:
    if result % 2 != 0 and result % 10 == 1:
        result = result // 10
        cnt += 1
    else:
        result /= 2
        cnt += 1
    if result < start:
        cnt = -1
        break

print(cnt)