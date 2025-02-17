f0=[1,0,1]
f1=[0,1,1]

def fibo(n):
    l=len(f0)
    if l<=n:
        for i in range(l,n+1):
            f0.append(f0[i-1]+f0[i-2])
            f1.append(f1[i-1]+f1[i-2])
    print(f0[n],f1[n])
for i in range(int(input())):
    fibo(int(input()))