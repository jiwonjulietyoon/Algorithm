# 6485 삼성시의 버스 노선 


for T in range(int(input())):     # Test Case
    st = [0] * 5000       # bus stations
    for _ in range(int(input())): # N
        a, b = map(int, input().split())
        for i in range(a-1, b):
            st[i] += 1
    ans = []
    for _ in range(int(input())): # P
        ans.append(st[int(input())-1])
    print(f"#{T+1} {' '.join(map(str, ans))}")





for T in range(int(input())):     # Test Case
    st = [0] * 5000       # bus stations
    for _ in range(int(input())): # N
        a, b = map(int, input().split())
        for i in range(a-1, b):
            st[i] += 1
    ans = []
    for _ in range(int(input())): # P
        ans.append(st[int(input())-1])
    print(f"#{T+1}", end=" ")
    print(*ans)