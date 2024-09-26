from collections import deque

n, k = map(int, input().split())
MAX = 10 ** 5
check=[0]*(MAX+1)

def bfs():
    Q = deque()
    Q.append(n)

    while Q:
        c = Q.popleft()

        if c == k:
            print(check[k])
            break

        for i in (c+1, c-1, c*2):
            if 0<=i<=MAX and not check[i]:
                Q.append(i)
                check[i] = check[c]+1

bfs()