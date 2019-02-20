# 1970. 쉬운 거스름돈

# 50,000 => 10,000 => 5,000 => 1,000 => 500 => 100 => 50 => 10

coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
T = int(input())
for t in range(1, T+1):
    cash = int(input())
    cnt = [0] * 8
    for x in range(len(coins)):
        if cash >= coins[x]:
            n = cash // coins[x]
            cash -= n * coins[x]
            cnt[x] += n
    print(f"#{t}")
    print(" ".join(map(str, cnt)))










    x = 0
    while(1):
        if cash >= coins[x]:
            cash -= coins[x]
            cnt[x] += 1
            if cash == 0:
                break
            continue
        

