N = int(input())
p = list(map(int, input().split()))
p.sort()

result = []
sum_i = 0
for i in range(N):
    sum_i += p[i]
    result.append(sum_i)

print(sum(result))