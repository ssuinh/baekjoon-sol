lst = []  # input
stack = []
result = []

idx = 0   # 입력 받은 수열 lst의 idx를 한칸씩 옮기면 굳이 pop안해도 됨.(reversed도 안해도 됨)
n = int(input())
for i in range(n):
    a = int(input())
    lst.append(a)

for i in range(n):
    stack.append(i+1)
    result.append('+')

    
    while True:
        if len(stack) != 0 and len(lst) != 0:
            if stack[-1] == lst[idx]:
                stack.pop()
                idx+=1   # 지우면서 다음 수열 요소인지 판별하기
                result.append('-')
            else:
                break
        else:
            break

if len(stack) != 0:
    print("NO")
else:
    for i in result:
        print(i)