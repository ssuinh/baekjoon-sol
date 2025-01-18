import sys
input = sys.stdin.readline

ans = []
k = int(input())
for i in range(k):
    tmp = int(input())
    if tmp == 0:
        ans.pop()
    else:
        ans.append(tmp)

print(sum(ans))