import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
ans = []
result = ''
cnt = 0
Q = deque()

for i in range(n):
    tmp = int(input())
    Q.append(tmp)

for i in range(1, n+1):
    ans.append(i)
    result += '+'

    while ans and ans[-1] == Q[0]:
        Q.popleft()
        ans.pop()
        result += '-'

if Q:
    print('NO')
else:
    for i in result:
        print(i)