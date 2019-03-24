# 색종이 올려 놓기


import sys
sys.stdin = open('../Input/2643.txt', 'r')

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

for x in paper:
    x.sort()
paper.sort(key=lambda x: x[0]*x[1])

print(paper)




stack = [paper[0]]
cnt = 1

for i in range(1, N):
    if paper[i][0] >= stack[-1][0] and paper[i][1] >= stack[-1][1]:
        stack.append(paper[i])
        cnt += 1

print(stack)
print(cnt)



# print(type(paper[0][1]))
# print(type(stack[-1][1]))

# for i in range(1, N):
#     if paper[i][1] <= stack[-1][1]:
#         stack.append(paper)
#         cnt += 1
#
# print(cnt)


