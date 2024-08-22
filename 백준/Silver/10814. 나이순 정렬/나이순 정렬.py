N = int(input())
a = [list(input().split()) for _ in range(N)]

a.sort(key=lambda x : int(x[0]))

for i in a:
    print(int(i[0]), i[1])