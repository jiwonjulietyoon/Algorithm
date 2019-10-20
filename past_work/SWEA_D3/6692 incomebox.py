# 6692 다솔이의 월급 상자 


for T in range(int(input())):
    N = int(input())
    P = []
    for _ in range(N):
        a, b = map(float, input().split())
        P.append(a*b)
    print(f"#{T+1} {sum(P)}")