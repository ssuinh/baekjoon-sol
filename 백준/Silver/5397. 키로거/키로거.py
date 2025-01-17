import sys
input = sys.stdin.readline

t = int(input())
for tc in range(t):
    L = list(input())
    ans = []
    tmp = []
    for i in range(len(L)):
        if L[i] == '<':
            if len(ans) > 0:
                tmp.append(ans.pop())
        elif L[i] == '>':
            if len(tmp) != 0:
                ans.append(tmp.pop())
            else:
                continue

        elif L[i] == '-':
            if len(ans) != 0:
                ans.pop()

        elif L[i] == '\n':
            continue

        else:  # 일반 문자일 경우
            ans.append(L[i])
    while len(tmp) > 0:
        ans.append(tmp.pop())

    for i in ans:
        print(i, end='')
    if tc < t-1:
        print()