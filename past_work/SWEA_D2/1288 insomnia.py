# 1288. 새로운 불면증 치료법 

for T in range(int(input())):
    N = n = int(input())
    numset = set()
    while True:
        numset.update(str(N))
        if len(numset) == 10:
            break
        N += n
    print(f"#{T+1} {N}")