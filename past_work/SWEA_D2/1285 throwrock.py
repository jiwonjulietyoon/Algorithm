# 1285 아름이의 돌 던지기 

# wasn't able to submit solution as system only accepted c++ codes


for T in range(int(input())):
    _, num = input(), list(map(lambda x: abs(int(x)), input().split()))
    ans = min(num)
    cnt = num.count(ans)

    print(f"#{T+1} {ans} {cnt}")