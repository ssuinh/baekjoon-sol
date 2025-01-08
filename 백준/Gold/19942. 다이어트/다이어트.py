import copy
import sys
input = sys.stdin.readline

def back(idx, mp, mf, ms, mv, price):
    global min_price
    global used
    global result
    global flag

    if idx == n:
        if mp >= standard[0] and mf >= standard[1] and ms >= standard[2] and mv >= standard[3]:
            if price < min_price:
                min_price = price
                flag = True
                result.clear()
                result.append(copy.deepcopy(used))
            elif price == min_price:
                flag = True
                result.append(copy.deepcopy(used))
            return
        else:
            return

    # 모든 경우의 수가 나옴.
    # 재료를 사용하는 경우
    used[idx+1] = '1'
    back(idx+1, mp+lst[idx][0], mf+lst[idx][1], ms+lst[idx][2], mv+lst[idx][3], price+lst[idx][4])
    used[idx+1] = '0'
    # 사용하지 않는 경우
    back(idx+1, mp, mf, ms, mv, price)

n = int(input())
standard = list(map(int, input().split()))
lst = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-1, -1, -1):
    if lst[i][0]==0 and lst[i][1]==0 and lst[i][2]==0 and lst[i][3] ==0: # 영양소가 모두 0일 경우 아예 제외.
        lst.pop(i)

n = len(lst)

used =['1'] + ['0'] * (n+1)
min_price = 99999999999999999999
flag = False
result = []
back(0, 0, 0, 0, 0, 0)
ans = 0

for i in result:
    a = int(''.join(i))
    if a > ans:
        ans = a

ans = str(ans)

if flag == True:
    print(min_price)
    for i in range(1, n+1):
        if ans[i] == '1':
            print(int(i), end=' ')
else:
    print(-1)