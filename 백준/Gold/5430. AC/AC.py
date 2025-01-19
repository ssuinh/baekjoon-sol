import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    R_flag = False
    fx = input().rstrip()
    size = int(input())
    Q = input().rstrip()
    Q = Q[1:-1]
    if size > 0:
        Q = deque(map(int, Q.split(',')))
    else:
        Q = deque(Q)
    flag = False
    for i in fx:
        if i == 'R':
            R_flag = not R_flag
            # Q.reverse()     # 굳이 리버스하지 않아도 R_flag에 따라서 pop위치 판단 & 출력 전 reverse하여 출력할지 여부 판단하면 됨.
        elif i == 'D':
            if Q:
                if not R_flag:
                    Q.popleft()
                else:
                    Q.pop()
            else:
                print('error')
                flag = True
                break

    if not flag:
        print('[', end='')
        if not R_flag:
            for i in range(len(Q)):
                if i != len(Q)-1:
                    print(f'{Q[i]},', end='')
                else:
                    print(Q[i], end='')
        else:
            for i in range(len(Q)-1, -1, -1):
                if i != 0:
                    print(f'{Q[i]},', end='')
                else:
                    print(Q[i], end='')
        print(']')