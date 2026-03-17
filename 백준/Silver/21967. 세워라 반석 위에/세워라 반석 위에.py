import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

cnt = [0] * 11  # 인덱스의 숫자가 몇 번 나왔는지 카운팅(max, min 값을 찾는데 사용함)
ans = 0
left = 0

for right in range(n):
    cnt[lst[right]] += 1
    
    while True:
        min_val = -1
        max_val = -1
        
        for i in range(1, 11):  # 현재 수열의 최소값 찾기
            if cnt[i] > 0:
                min_val = i
                break
            
        for i in range(10, 0, -1):  # 현재 수열의 최댓값 찾기
            if cnt[i] > 0:
                max_val = i
                break
        
        if max_val-min_val <= 2:  # 반석이라면 right 옮기기
            break
        
        cnt[lst[left]] -= 1   # 반석이 아니라면 left를 옮김 (즉 배열의 맨 처음 요소가 사라지는 것.)
        left += 1
        
    ans = max(ans, right-left+1)
    
print(ans)