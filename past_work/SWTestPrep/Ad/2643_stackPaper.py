# 색종이 올려 놓기 => unfinished


import sys
sys.stdin = open('../Input/2643.txt', 'r')
# sys.stdin = open('../Input/tmp.txt', 'r')



N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

for x in paper:
    x.sort()
# paper.sort(key=lambda x: x[0]*x[1], reverse=True)
paper.sort(key=lambda x: (x[0], x[1]), reverse=True)
print(*paper, sep="\n")

print()

count = [[] for _ in range(N)]  # which (smaller) papers can fit on top?
for i in range(N):  # for each paper
    for j in range(i+1, N):
        if paper[j][0] <= paper[i][0] and paper[j][1] <= paper[i][1]:
            count[i] += [j]
print(*count, sep="\n")

Max = 1  # at least one paper can be stacked

for i in range(N):  # go through count
    if i >= N-Max:
        break









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
#     if N-Max <= i:
#         break
#     stack = [paper[i]]
#     cnt = 1
#     count_paper(stack, i+1, cnt)
#
# print(Max)



