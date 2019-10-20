# 5688. 세제곱근을 찾아라



# 2nd try
for T in range(int(input())):
    c_root = int(input()) ** (1/3)
    if abs(c_root - round(c_root)) < 0.00001:
        X = round(c_root)
    else:
        X = -1
    print(f"#{T+1} {X}")







# 1st try

for T in range(int(input())):
    N = int(input())
    X = -1
    if N == 1:
        X = 1
    else:
        l = 1
        r = int(N/4)
        while(1):
            m = int((l+r)/2)
            if m**3 == N:
                X = m
                break
            if l**3 <= N and N < m**3:
                r = m - 1
            elif m**3 < N and N <= r**3:
                l = m + 1
            else:
                break
    print(f"#{T+1} {X}")