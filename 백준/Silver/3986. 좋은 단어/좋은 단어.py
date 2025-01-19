import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
cnt = 0
for _ in range(n):
    stack = []
    word = input().rstrip()
    if len(word) % 2 == 1:
        continue
    for i in word:
        if stack:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    if not stack:
        cnt += 1
print(cnt)