import sys
input = sys.stdin.readline

def back(idx, pay):
    global max_pay

    if idx == n-1:
        if lst[idx][0] == 1:
            max_pay = max(max_pay, pay+lst[idx][1])
        else:
            max_pay = max(max_pay, pay)
        return
    elif idx == n:
        max_pay = max(max_pay, pay)
        return
    elif idx > n:
        return

    # 스케줄에 넣는 경우
    back(idx+lst[idx][0], pay+lst[idx][1])
    # 안 넣는 경우
    back(idx+1, pay)

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

# 백준이의 퇴사 전까지 상담할 스케줄 표
schedule = [0] * (n+1)
max_pay = 0
back(0, 0)

print(max_pay)