n, m = map(int, input().split())
lst = []


def back(start):
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return

    for i in range(start, n+1):
        lst.append(i)
        back(i)
        lst.pop()
back(1)