import sys
input = sys.stdin.readline

li=list(map(int, input().rstrip()))
lst = [0] * 10
for i in li:
    lst[i] += 1

# 6, 9는 교차 사용가능 => (six+nine)//2로 판단
six = lst.pop(6)
nine = lst.pop(-1)

max_val = max(lst)

if (six+nine) % 2 != 0:
    val = (six+nine)//2 + 1
else:
    val = (six+nine)//2

ans = max(max_val, val)
print(ans)