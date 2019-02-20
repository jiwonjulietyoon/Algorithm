# 5431 민석이의 과제 체크하기 

for T in range(int(input())):
    N, K = map(int, input().split())
    klist = list(map(int, input().split()))
    ans = list(range(1, N+1))
    for k in klist:
        if k in ans:
            ans.remove(k)
    print(f"#{T+1} ", end="")
    print(*ans)
