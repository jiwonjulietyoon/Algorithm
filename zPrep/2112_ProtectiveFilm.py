import sys
sys.stdin = open('Input/2112.txt', 'r')

""" 2112. [모의 SW 역량테스트] 보호 필름


"""

def check_col(arr, K, c):  # check specified column; return 1 if pass
    same = 0
    for r in range(1, D):
        if arr[r-1][c] == arr[r][c]:
            same += 1
        else:
            same = 0
        if same == 2:
            return 1
    return 0

def check_all_col(arr, K):  # check if all columns pass the K test
    for c in range(W): # col by col
        if check_col(arr, K, c) == 0:
            return 0
    return 1

def change_row(arr, r, res):  # change specified row into either "0" or "1"
    arr[r] = [res]*W



for T in range(1, int(input())+1):
    D, W, K = map(int, input().split())  # Depth(row), Width(col), K
    arr = [0]*D
    for i in range(D):
        arr[i] = input().split()
    print(arr)

    cnt = 0
    while 1:
        if check_all_col(K):
            break


    print("#{} {}".format(T, cnt))





