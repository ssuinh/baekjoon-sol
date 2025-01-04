# 슬라이딩 방식 아닌 메모이제이션 DP 접근법

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))

# 틀린이유 : prefix의 길이는 맨 앞 0이 있어야함. k=1일 경우 뺄 이전 요소가 없기 때문에 runtimeerror 발생.
prefix = [0]   # 수열 요소간 차
tmp = 0
for i in lst:
    tmp += i
    prefix.append(tmp)

ans = []
temp = 0
for i in range(k, n+1):   
    # index 4까지의 누적합 - 2까지의 누적합 == (2+1)~4 요소의 누적합
    temp = prefix[i] - prefix[i-k]
    ans.append(temp)  # k=2 두개 요소들의 합을 저장한 리스트

print(max(ans))