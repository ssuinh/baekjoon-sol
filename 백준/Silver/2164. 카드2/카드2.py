import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
Q = deque(i for i in range(1, n+1))

cnt = 0
while len(Q) > 1:
    if cnt % 2 == 0:
        Q.popleft()
    else:
        Q.append(Q.popleft())
    cnt += 1
print(*Q)