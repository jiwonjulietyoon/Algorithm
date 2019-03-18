# 4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합


##### Binary Counting
A = list(range(1, 13))
lenA = len(A)

for T in range(int(input())):     # test case
    N, K = map(int, input().split())  # N elements, sum == K
    cnt = 0    # number of subsets with (N elements & sum K)
    for i in range(1, 1<<lenA):
        bitCnt = Sum = 0
        for j in range(lenA):
            if i & (1<<j):
                Sum += (j + 1)
                bitCnt += 1
        if Sum == K and bitCnt == N:
            cnt += 1
    print(f"#{T+1} {cnt}")




##### 1차 시도: 
# 일단 모든 부분집합을 구한 후, 
# 조건 N과 조건 K에 맞는 부분집합만 따로 걸러내기

A = list(range(1, 13))
lenA = len(A)

for T in range(int(input())):     # test case
    N, K = map(int, input().split())  # N elements, sum == K
    cnt = 0    # number of subsets with (N elements & sum K)
    for i in range(1, 1<<lenA):
        ss_sum = 0  # sum of all elements in subset
        ss = []     # subset
        for j in range(lenA):
            if i & (1<<j):
                ss.append(A[j])
                ss_sum += A[j]
        if ss_sum == K and len(ss) == N:
            cnt += 1
    print(f"#{T+1} {cnt}")