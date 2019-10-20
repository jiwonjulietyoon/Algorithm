
# 문자열 교집합

import sys
sys.stdin = open('../Input/input2948.txt', 'r')


"""
compare letter by letter, via separate function?

"""



for T in range(int(input())):
    N, M = map(int, input().split())
    s1, s2 = input().split(), input().split()

    cnt = 0

    for word in s1:
        if word in s2:
            cnt += 1
            s2.remove(word)

    print("#{} {}".format(T + 1, cnt))



##################################################################
# 시간 초과


# for T in range(int(input())):
#     N, M = map(int, input().split())
#     s1, s2 = input().split(), input().split()
# 
#     cnt = 0
# 
#     for i in range(N):
#         for j in range(M):
#             if s2[j] and s1[i] == s2[j]:
#                 cnt += 1
#                 s2[j] = ''
# 
#     print("#{} {}".format(T + 1, cnt))



###############################################
# 시간 초과

# for T in range(int(input())):
#     N, M = map(int, input().split())
#     s1, s2 = input().split(), input().split()
# 
#     cnt = 0
#     for word in s1:
#         if word in s2:
#             cnt += 1
# 
#     print("#{} {}".format(T+1, cnt))


