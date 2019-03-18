# 5431. 민석이의 과제 체크하기



# shorter version
for T in range(int(input())):
    N, K = map(int, input().split())     # N total students
    P = input().split()   # K students who turned in their HW
    ans = []
    for x in range(1, N+1):
        if str(x) not in P:
            ans.append(str(x))
    print(f"#{T+1} {' '.join(ans)}")





# longer version
for T in range(int(input())):
    N, K = map(int, input().split())
    P = list(map(int, input().split()))    # // inputs

    for i in range(K):
        minidx = i
        for j in range(i+1, K):
            if P[minidx] > P[j]:
                minidx = j
        P[i], P[minidx] = P[minidx], P[i]   # // P - selection sort

    arr = [0] * N
    for i in range(N):
        arr[i] = i+1                       # // arr with elements from 1 to N

    for i in range(K):
        idx = i
        for j in range(idx, N):
            if P[i] == arr[j]:
                arr[j] = 0
                idx = j
                break               # if an element in arr is also in P, change it to '0'
    
    ans = [0] * (N-K) 
    tmp = 0
    for i in range(N):
        if arr[i] != 0:
            ans[tmp] = arr[i]
            tmp += 1               # move non-zero elements in arr to ans
    
    print(f"#{T+1} {' '.join(map(str, ans))}")
    