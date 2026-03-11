import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [0]+list(map(int, input().split()))

def DFS(index, size, time):
    global ans
    
    if time > m:
        return 
    if time <= m :
        ans = max(ans, size)
    if index <= n-1:
        DFS(index+1, size+lst[index+1], time+1)
    if index <= n-2:
        DFS(index+2, size//2+lst[index+2], time+1)
        
ans = -1
DFS(0,1,0)
print(ans)