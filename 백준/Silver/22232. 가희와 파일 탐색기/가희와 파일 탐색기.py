import sys
input=sys.stdin.readline

n,m=map(int, input().split())

jo_test = [input().rstrip() for _ in range(n)]
ext = set(input().rstrip() for _ in range(m))

jo_test_split = []
for item in jo_test:
    jo_test_split.append(item.split("."))

# 첫 번째 정렬  
jo_test_split = sorted(jo_test_split, key=lambda x : (x[0], x[1]))

for i in range(n-1):
    if jo_test_split[i][0] == jo_test_split[i+1][0]:
        if jo_test_split[i][1] not in ext and jo_test_split[i+1][1] in ext:
            tmp = jo_test_split[i]
            jo_test_split[i] = jo_test_split[i+1]
            jo_test_split[i+1] = tmp
for i in jo_test_split:
    print(i[0]+"."+i[1])