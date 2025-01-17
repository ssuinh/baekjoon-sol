import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
Q = deque(i for i in range(1, n+1))

idx = 1
print('<', end='')
while Q:
    if idx == k:
        if len(Q) == 1:
            print(Q.popleft(), end='>')
        else:
            print(Q.popleft(), end=', ')
            idx = 1
    else:
        Q.append(Q.popleft())
        idx += 1