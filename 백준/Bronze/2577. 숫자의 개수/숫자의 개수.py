import sys
input = sys.stdin.readline

ans = 1
for i in range(3):
    ans *= int(input())

lst = [0] * 10
for i in str(ans):
    lst[int(i)] += 1

for i in lst:
    print(i)