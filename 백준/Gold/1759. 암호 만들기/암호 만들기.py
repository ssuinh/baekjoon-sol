l, c = map(int, input().split())
arr = list(input().split())
arr.sort()
lst = []

def back(start):
    if len(lst) == l:
        cnt = 0
        for i in lst:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                cnt += 1
        if 0 < cnt <= l-2:
            print(''.join(map(str, lst)))
        return

    for i in range(start, c):
        if arr[i] not in lst:
            lst.append(arr[i])
            back(i+1)
            lst.pop()
back(0)