import sys

tc = int(input())
for _ in range(tc):
    L = input()
    ans = []
    tmp = []

    for i in L:
        if i == '<':
            if len(ans) > 0:
                tmp.append(ans.pop())
        elif i == '>':
            if len(tmp) > 0:
                ans.append(tmp.pop())
        elif i == '-':
            if len(ans) > 0:
                ans.pop()
        else:
            ans.append(i)
    while len(tmp) > 0:
        ans.append(tmp.pop())
    print(''.join(ans))