# 1986. 지그재그 숫자

# 1~N 숫자 중 홀수는 더하고 짝수는 뺀다. 최종 누적 값은?

T = int(input())
for t in range(T):
    N = int(input())
    q, r = divmod(N, 2)
    Sum = -1 * q
    if r == 1:
        Sum += N
    print(f"#{t+1} {Sum}")