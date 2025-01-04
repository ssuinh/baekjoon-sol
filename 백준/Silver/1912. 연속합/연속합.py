import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

prefix = [0 for _ in range(n+1)]   # 수열 요소간 차

for i in range(n):
    prefix[i+1] = max(prefix[i]+lst[i], lst[i])

prefix.pop(0)   # 마지막 오답.. 모두 음수일 경우를 대비해 지워야함.
print(max(prefix))


#-----------------------------------------------------------------------------------------------------------------------------

# 아래 코드는 잘못됐어....
# 30
# 2 -3 10 -6 -2 -4 -5 3 -9 3 8 -6 -6 4 6 -7 5 -7 3 4 10 0 -3 -6 6 -9 -7 -10 0 -2
# 이 경우에 내가 한 논리로는 답을 찾지 못해..ㅠㅠㅠㅠㅠㅠㅠ
"""
for i in lst:
    tmp += i
    prefix.append(tmp)

max_val = max(prefix)
min_val = min(prefix)

max_idx = prefix.index(max_val)
min_idx = prefix.index(min_val)
# print(max_idx)
# 최댓값 인덱스가 0인경우, 최솟값 인덱스가 -1인 경우에 성립이 안되기 때문에 조건문 걸어줌.
if max_idx == 0 and min_idx != n-1:
    sel_max_val = max(prefix[min_idx:])

    print(sel_max_val-min_val)
elif max_idx != 0 and min_idx == n-1:
    sel_min_val = min(prefix[:max_idx])
    print(max(max_val-sel_min_val, max(prefix)))
elif max_idx == 0 and min_idx == n-1:
    if max_val < 0:
        for i in range(1, n):
            if prefix[i] == max_val:
                print(0)
                break
        else:
            print(max(prefix[-1] - prefix[-2], max(prefix)))
    else:
        print(max(prefix))
else:
    sel_min_val = min(prefix[:max_idx])
    sel_max_val = max(prefix[min_idx:])
    print(max(sel_max_val-min_val, max_val-sel_min_val, max(prefix)))
"""