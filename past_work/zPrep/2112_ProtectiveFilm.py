import sys
sys.stdin = open('Input/2112.txt', 'r')

""" 2112. [모의 SW 역량테스트] 보호 필름


"""


def isPass(arr):
    # 세로줄 검사
    # n = 0
    for y in range(W):
        A, B = 0, 0
        for x in range(D):
            if arr[x][y]:
                B += 1
                A = 0
            else:
                A += 1
                B = 0
            if A >= K or B >= K:
                # n += 1
                break
        # 만약 K개의 연속된 값이 없다면 정지
        if A < K and B < K:
            return False
    return True


# 부분집합으로 계산하기
def powerset(arr):
    global result
    for i in range(1 << D):
        n, breakPT = 0, False
        arrA = arr[:]
        arrB = arr[:]
        for j in range(D):
            if i & (1 << j):
                n += 1
                if n >= result:
                    breakPT = True
                    break
                arrA[j] = [0] * W
                arrB[j] = [1] * W
        if not breakPT:
            if isPass(arrA) or isPass(arrB):
                if result > n:
                    result = n


T = int(input())
for test_case in range(1, 1 + T):
    D, W, K = map(int, input().split())
    F = [list(map(int, input().split())) for _ in range(D)]
    print(F)
    # visited = [0] * D
    result = D
    powerset(F)

    print('#{} {}'.format(test_case, result))







# def check_col(arr, K, c):  # check specified column; return 1 if pass
#     same = 0
#     for r in range(1, D):
#         if arr[r-1][c] == arr[r][c]:
#             same += 1
#         else:
#             same = 0
#         if same == 2:
#             return 1
#     return 0
#
# def check_all_col(arr, K):  # check if all columns pass the K test
#     for c in range(W): # col by col
#         if check_col(arr, K, c) == 0:
#             return 0
#     return 1
#
# def change_row(arr, r, res):  # change specified row into either "0" or "1"
#     arr[r] = [res]*W
#
#
#
# for T in range(1, int(input())+1):
#     D, W, K = map(int, input().split())  # Depth(row), Width(col), K
#     arr = [0]*D
#     for i in range(D):
#         arr[i] = input().split()
#     print(arr)
#
#     cnt = 0
#     while 1:
#         if check_all_col(K):
#             break
#
#
#     print("#{} {}".format(T, cnt))





