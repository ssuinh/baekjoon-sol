ans = 0
n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a == b or b == c or c == a:
                # 서로 다른 세 수
                continue

            check = 0   # 힌트 비교 횟수
            for arr in lst:
                number = str(arr[0])
                strike = arr[1]
                ball = arr[2]

                s = 0
                bll = 0
                cnt = 0
                # 한자리씩 숫자 비교
                for k in (a, b, c):
                    if k == int(number[cnt]):
                        s += 1
                    elif str(k) in number:
                        bll += 1
                    cnt += 1

                if s != strike or bll != ball:
                    check = 0
                    break
                check += 1

            if check == n:
                ans += 1

print(ans)