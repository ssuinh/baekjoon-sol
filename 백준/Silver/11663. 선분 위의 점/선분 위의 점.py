import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

# 이분탐색 함수인 bisect 활용
n, m = map(int, input().split())
dot_lst = list(map(int, input().split()))
dot_lst.sort()

for i in range(m):
    start, end = map(int, input().split())
    # 찾는 범위의 시작점 인덱스 반환
    start_idx = bisect_left(dot_lst, start)
    # 찾는 범위의 가장 오른쪽 인덱스 반환
    end_idx = bisect_right(dot_lst, end)
    
    # 찾는 범위의 끝 점 - 시작 점 == 찾고자하는 범위의 점의 수 (리스트는 정렬되어 있기에 가능)
    print(end_idx - start_idx)