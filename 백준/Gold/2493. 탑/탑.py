import sys
input = sys.stdin.readline

# 입력 값을 하나 씩 넣으면서 이전 값이 더 작으면 비교할 필요가 없으므로 기존값은 pop한 뒤 추가
n = int(input())
lst = list(map(int, input().split()))
stack = []
ans = []

# 스택의 마지막 값이 답이 됨.
for i in range(n):
    while stack:
        if stack[-1][1] < lst[i]:  # 원소보다 작은 경우 모두 pop (뒤의 값은 현재 건물이 수신함.)
            stack.pop()
        else:
            ans.append(stack[-1][0]+1)  # 현재 값 보다 클 경우 답.
            break
            
    if not stack:  # 첫번 째 건물 or stack의 값이 모두 작아서 답이 없는 경우 0
        ans.append(0)
    stack.append([i, lst[i]])  # 현재 값 stack에 추가.

print(*ans)