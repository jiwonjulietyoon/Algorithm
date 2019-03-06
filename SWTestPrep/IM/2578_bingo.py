import sys
sys.stdin = open('../Input/2578.txt', 'r')

#########################################

def markZero(num):
    global board
    tmp = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                board[i][j] = 0
                tmp = 1
                break
        if tmp:
            break
    return (i, j)

def checkLine(line):
    for x in line:
        if x:  # anything other than 0
            return False
    return True

def checkBingo(i, j):
    global board, b_r, b_c, b_d, cnt
    # row
    if i not in b_r:
        if checkLine(board[i]):
            cnt += 1
            b_r.append(i)
    # column
    if cnt < 3 and j not in b_c:
        col = [board[a][j] for a in range(5)]
        if checkLine(col):
            cnt += 1
            b_c.append(j)
    # diag
    if i == j or i+j == 4:
        if cnt < 3 and 0 not in b_d:
            diag = [board[a][a] for a in range(5)]
            if checkLine(diag):
                cnt += 1
                b_d.append(0)
        if cnt < 3 and 5 not in b_d:
            diag = [board[a][4-a] for a in range(5)]
            if checkLine(diag):
                cnt += 1
                b_d.append(5)

#######################################

board = [input().split() for _ in range(5)]
called = []
for _ in range(5):
    called.extend(input().split())

cnt = 0
b_r = []
b_c = []
b_d = []

for x in range(25):
    idx = markZero(called[x])
    checkBingo(idx[0], idx[1])
    if cnt >= 3:
        break

print(x+1)