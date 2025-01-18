import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
Q = deque()
for _ in range(n):
    tmp = input().strip("\n")
    if tmp == 'pop':
        if Q:
            print(Q.popleft())
        else:
            print(-1)
    elif tmp == 'size':
        print(len(Q))
    elif tmp == 'empty':
        if Q:
            print(0)
        else:
            print(1)
    elif tmp == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)
    elif tmp == 'back':
        if Q:
            print(Q[-1])
        else:
            print(-1)
    else:
        a, b = map(str, tmp.split())
        X = int(b)
        Q.append(X)