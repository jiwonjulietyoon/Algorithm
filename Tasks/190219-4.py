# 4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합


for T in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    idx = [0] * N    # record selected columns (index number)
    sel = [0] * N    # record selected numbers from each row

    for r in range(N): # for each row
        sel[r] = min(arr[r])  # select the minimum
        idx[r] = arr[r].index(sel[r])  # and record its index

    while(1):
        if len(set(idx)) == N:
            break
        else:  # if there are any redundant index numbers
         

    print(f"#{T+1} {ans}")




########################################################################

"""
[
    [(1, 1), (0, 2), (2, 2)], 
    [(0, 5), (2, 5), (1, 8)], 
    [(1, 2), (2, 2), (0, 7)]
]

Try all elements of each row, starting from the bottom row




"""





