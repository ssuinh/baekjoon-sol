import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    num1 = int(input())
    lst1 = set(map(int, input().split()))
    num2 = int(input())
    lst2 = tuple(map(int, input().split()))

    for i in lst2:
        if i in lst1:
            print(1)
        else:
            print(0)