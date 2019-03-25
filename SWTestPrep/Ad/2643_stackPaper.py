# 색종이 올려 놓기 => unfinished


import sys
sys.stdin = open('../Input/2643.txt', 'r')
# sys.stdin = open('../Input/tmp.txt', 'r')


def count_paper(stack, k, cnt):
    global paper, N, Max
    if k == N:
        if cnt > Max:
            Max = cnt
    else:
        for i in range(k, N):
            if paper[i][0] <= stack[-1][0] and paper[i][1] <= stack[-1][1]:
                stack.append(paper[i])
                cnt += 1
                count_paper(stack, i+1, cnt)
                stack.pop()
                cnt -= 1


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

for x in paper:
    x.sort()
paper.sort(key=lambda x: x[0]*x[1], reverse=True)

Max = 0

for i in range(N):
    if N-Max <= i:
        break
    stack = [paper[i]]
    cnt = 1
    count_paper(stack, i+1, cnt)

print(Max)













###############################################################
# 1st try: time over


#
# def count_paper(stack, k, cnt):
#     global paper, N, Max
#     if k == N:
#         if cnt > Max:
#             Max = cnt
#     else:
#         for i in range(k, N):
#             if paper[i][0] <= stack[-1][0] and paper[i][1] <= stack[-1][1]:
#                 stack.append(paper[i])
#                 cnt += 1
#                 count_paper(stack, i+1, cnt)
#                 stack.pop()
#                 cnt -= 1
#
#
# N = int(input())
# paper = [list(map(int, input().split())) for _ in range(N)]
#
# for x in paper:
#     x.sort()
# paper.sort(key=lambda x: x[0]*x[1], reverse=True)
#
# Max = 0
#
# for i in range(N):
#     stack = [paper[i]]
#     cnt = 1
#     count_paper(stack, i+1, cnt)
#
# print(Max)



