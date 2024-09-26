lst = []  # input
stack = []
result = []


n = int(input())
for i in range(n):
    a = int(input())
    lst.append(a)

r_lst = list(reversed(lst))


for i in range(n):
    stack.append(i+1)
    result.append('+')

    
    while True:
        if len(stack) != 0 and len(r_lst) != 0:
            if stack[-1] == r_lst[-1]:
                stack.pop()
                r_lst.pop()
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