import sys
input = sys.stdin.readline

def back(idx, sour, bitter, cnt):
    global min_num
    if idx == n:
        if cnt != 0:  # 재료를 하나라도 사용해야함.
            ans = abs(sour-bitter)
            min_num = min(ans, min_num)
            return min_num
        else:
            return

    # 모든 경우의 수가 나옴.
    # 재료를 사용하는 경우
    back(idx+1, sour * lst[idx][0], bitter + lst[idx][1], cnt + 1)

    # 사용하지 않는 경우
    back(idx+1, sour, bitter, cnt)

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

used = [0] * n
min_num = 99999999999999999999

back(0,1,0,0)
print(min_num)
