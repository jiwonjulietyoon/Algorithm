# 1284. 수도 요금 경쟁

for T in range(int(input())):
    P, Q, R, S, W = map(int, input().split())
    if W <= R:
        ans = min(P*W, Q)
    else:
        ans = min(P*W, (W-R)*S+Q)
    print(f"#{T+1} {ans}")