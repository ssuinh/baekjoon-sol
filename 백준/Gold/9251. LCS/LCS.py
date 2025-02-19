import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

graph = [[0] * (len(b)+1) for _ in range(len(a)+1)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        # 문자가 같으면 카운트 +1
        if a[i-1] == b[j-1]:
            graph[i][j] = graph[i-1][j-1] + 1
        # 문자가 다르면 지금 값 중 최댓값으로 채움.
        else:
            graph[i][j] = max(graph[i][j-1], graph[i-1][j])

print(graph[-1][-1])