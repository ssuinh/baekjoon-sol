import sys
input = sys.stdin.readline

n, k = map(int, input().split())

lst = set()
visit = set()
for i in range(k):
    a, b = map(int, input().split())
    lst.add((a-1, b-1))


cnt = 0
di = [0, 0, -2, 2]
dj = [2, -2, 0, 0]

def check(r, c):
    global cnt
    for i in range(4):
        ni = r + di[i]
        nj = c + dj[i]
        if 0 <= ni <= n-1 and 0 <= nj <= n-1:
            if (ni, nj) not in lst and (ni, nj) not in visit:
                visit.add((ni, nj))
                cnt += 1
                
    
for i in lst:
    check(i[0], i[1])
print(cnt)