import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
lst = list(map(int, input().split()))   # 꺼낼 수

Q = deque(i for i in range(1, n+1))   # 전체 요소
cnt = 0
for num in lst:
    idx = Q.index(num)
    while num != Q[0]:
        if idx <= len(Q) // 2:   # 찾을 인덱스가 앞쪽이면 2번 연산.
            Q.append(Q.popleft())
            cnt += 1
        else:  # 3번 연산
            Q.appendleft(Q.pop())
            cnt += 1
    if num == Q[0]:
        Q.popleft()

print(cnt)