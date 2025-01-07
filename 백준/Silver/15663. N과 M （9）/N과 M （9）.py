import sys
input = sys.stdin.readline
def back(number):
    if number == m:
        print(*arr)
        return
    tmp = 0
    
    for i in range(n):
        # visited는 이미 뽑은 숫자가 다음 뽑을수와 안겹치기 위함
        # tmp는 같은 자리의 수를 뽑을 때 반복문 내에서 같은 숫자를 안뽑기 위함. 9가 두개면 1 9가 두번 출력되는 것 방지
        if visited[i] == 0 and tmp != lst[i]:
            arr.append(lst[i])
            visited[i] = 1
            tmp = lst[i]
            back(number + 1)
            visited[i] = 0
            arr.pop()

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
visited = [0] * n

arr = []
back(0)

