n = int(input())
m = int(input())
a = input()
i, result, count = 0,0,0

while i < (m-1):
    if a[i: i+3] == 'IOI':
        count +=1
        i +=2
        if count == n:
            result += 1
            count -=1
    else:
        i +=1
        count = 0

print(result)