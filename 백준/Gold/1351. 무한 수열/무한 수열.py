import sys
input = sys.stdin.readline

n, p, q = map(int, input().split())

memo = {}
memo[0] = 1

def back(i):
    # 값이 없으면 함수를 호출하여 계산하고 있으면 값을 가져옴.
    if i not in memo:
        memo[i] = back(i//p) + back(i//q)
    return memo[i]

print(back(n))