import sys
input = sys.stdin.readline

a = input().rstrip()

stack = []
cnt = 0
for i in a:
    if i == '(':
        stack.append(i)
        last = '('
    else:
        # stack[-1]값으로 판단하는 경우 닫는 괄호는 stack에 넣지 않으므로 다음 닫는 괄호가 레이저라고 판단하게됨.
        if last == '(':   # 레이저인 경우
            stack.pop()
            cnt += len(stack)   # stack의 여는 괄호 수 == 막대의 갯수
            last = ')'
        else:   # 레이저가 아닌 )
            stack.pop()
            cnt += 1   # 막대의 끝부분, 막대가 끊기는 부분이므로 하나가 더 생김.
print(cnt)