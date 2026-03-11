import sys
input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
cnt = 0
for i in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
visit = []
MAX = 10**30
min_change_cnt = MAX
q = deque([(a, 0)])
while q:
    cur, dist = q.popleft()
    if cur == b:
        min_change_cnt = min(min_change_cnt, dist)
    for next in graph[cur]:
        if next not in visit:
            visit.append(next)
            q.append((next, dist+1))
            
if min_change_cnt == MAX:
    min_change_cnt = -1
print(min_change_cnt)