n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
lst = []

def back(start):
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return

    for i in range(n):
        if arr[i] not in lst:
            lst.append(arr[i])
            back(i+1)
            lst.pop()
back(0)