from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
cal_lst = list(map(int, input().split()))    # +, -, *, /
max_r = -1*100000000
min_r = 10**1000
operator = '+' * cal_lst[0] + '-' * cal_lst[1] + '*' * cal_lst[2] + '/'* cal_lst[3]
op = permutations(operator, n-1)

for o in op:
    result = arr[0]
    for i in range(1, n):
        if o[i-1] == '+':
            result += arr[i]
        elif o[i-1] == '-':
            result -= arr[i]
        elif o[i-1] == '*':
            result *= arr[i]
        elif o[i-1] == '/':
            if result < 0 and arr[i] > 0:
                result = -1 * (result*(-1) // arr[i])
            else:
                result //= arr[i]

    max_r = max(max_r, result)
    min_r = min(min_r, result)

print(max_r)
print(min_r)