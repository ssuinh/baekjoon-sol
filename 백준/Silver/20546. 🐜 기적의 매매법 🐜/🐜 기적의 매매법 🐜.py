cash_timing = int(input())
cash_bnp = cash_timing
graph = list(map(int, input().split()))
tmp = 0
cnt = 0
bnp_cnt = 0
stack_down = 0
stack_up = 0

def cal(price, how):
    global cnt
    global cash_timing
    if how == "sell":
        cash_timing += price*cnt
        cnt = 0
        
    elif how == "buy":
        cnt = cash_timing // graph[i]
        cash_timing -= graph[i] * cnt
        
for i in range(1, 14): 
    if graph[i] > graph[i-1]:
        stack_up += 1
        stack_down = 0
        if stack_up >= 3:
            cal(graph[i], "sell")
        
    elif graph[i] < graph[i-1]:
        stack_up = 0 
        stack_down += 1
        if stack_down >= 3:
            cal(graph[i], "buy")
        
    else:
        stack_down = 0
        stack_up = 0
        
    if cash_bnp >= graph[i]:
        bnp_cnt += cash_bnp // graph[i]
        cash_bnp -= bnp_cnt * graph[i]
        
if cash_bnp+graph[-1]*bnp_cnt > cash_timing+graph[-1]*cnt:
    result = "BNP"
elif cash_bnp+graph[-1]*bnp_cnt < cash_timing+graph[-1]*cnt:
    result = "TIMING"
else:
    result = "SAMESAME"
print(result)