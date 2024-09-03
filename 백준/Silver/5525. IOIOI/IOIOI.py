n = int(input())
m = int(input())
a = list(input())
result = 0

for i in range(m-(2*n+1)+1):
    if a[i] == 'I':
        for j in range(2*n+1):
            if j == 0:
                pre = a[i]
            else:
                if a[i+j] != pre:
                    pre=a[i+j]
                    continue
                else:
                    break
        else:
            result += 1
print(result)