# 1244. [S/W 문제해결 응용] 2일차 - 최대 상금

import sys
# sys.stdin = open('../Input/1244.txt', 'r')
sys.stdin = open('../Input/tmp.txt', 'r')

def best(num):
    return 1 if num == sorted(num, reverse=True) and num.count(max(num)) > 1 else 0

for T in range(1, int(input())+1):
    inp = input().split()
    num, cnt = [int(x) for x in inp[0]], int(inp[1])
    N = len(num)

    if best(num):
        pass
    elif N - num.count(max(num)) <= cnt < num.count(max(num)):
        for i in range(cnt):
            min_i = num.index(min(num[:N-i]))
            max_i = num.index(max(num[:N-i]))
            for j in range(N-1-i, -1, -1):
                if num[j] == num[max_i]:
                    break
            num[min_i], num[j] = num[j], num[min_i]
            if best(num):
                break
    else:
        t = 0
        i = 0
        while t < cnt:
            Max = max(num[i:])
            if num[i] == Max and i < N-2:
                if i < N-2:
                    i += 1
                    continue
            else:
                for j in range(N-1, i, -1):
                    if num[j] == Max:
                        break
                num[i], num[j] = num[j], num[i]
                if i < N-2:
                    i += 1
                t += 1
            if best(num):
                break

    print(f"#{T}", end=" ")
    print(*num, sep="")


###############################################################



# for T in range(1, int(input())+1):
#     inp = input().split()
#     num, cnt = [int(x) for x in inp[0]], int(inp[1])
#     # print(num, cnt)
#
#     N = len(num)
#     t = 0
#     i = 0
#     while t < cnt:
#         Max = max(num[i:])
#         if num[i] == Max and i < N-2:
#             if i < N-2:
#                 i += 1
#                 continue
#         else:
#             for j in range(N-1, i, -1):
#                 if num[j] == Max:
#                     break
#             num[i], num[j] = num[j], num[i]
#             # print(num)
#             if i < N-2:
#                 i += 1
#             t += 1
#     # print(num)
#     # print()
#
#     print(f"#{T}", end=" ")
#     print(*num, sep="")


#################################################################


# for T in range(1, int(input())+1):
#     inp = input().split()
#     num, cnt = [int(x) for x in inp[0]], int(inp[1])
#     print(num, cnt)
#
#     N = len(num)
#     i = 0
#     for _ in range(cnt):
#         max_i = i+1
#         # for j in range(i+2, N):
#         for j in range(N-1, i+1, -1):
#             if num[j] > num[max_i]:
#                 max_i = j
#         num[i], num[max_i] = num[max_i], num[i]
#         if i < N-2:
#             i += 1
#
#     print(num)
#
#
#     # print(f"#{T} {Max}")