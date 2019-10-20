# 1945. 간단한 소인수분해 

for T in range(int(input())):
    f = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}
    N = int(input())
    for x in f:
        while(1):
            if not N % x: 
                N /= x
                f[x] += 1
            else:
                break
    ans = " ".join(map(str, f.values()))
    print(f"#{T+1} {ans}")