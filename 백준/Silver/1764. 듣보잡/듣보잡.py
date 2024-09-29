n, m = map(int, input().split())
ans = set()
lst1 = set()

for i in range(n):
    lst1.add(input())

for i in range(m):
    a = input()
    if a in lst1:
        ans.add(a)
ans = sorted(ans)
print(len(ans))
for i in ans:
    print(i)