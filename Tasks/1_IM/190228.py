# 1974. 스도쿠 검증

def sudoku(arr): # 9x9 sudoku
    for i in range(9): # search each row and column
        col = [arr[j][i] for j in range(9)]
        if len(set(arr[i])) != 9 or len(set(col)) != 9:
            return 0
    for i in [0, 3, 6]: # search each 3x3 section
        for k in [0, 3, 6]:
            sub = []
            for j in range(3):
                sub.extend(arr[i+j][k:k+3])
            if len(set(sub)) != 9:
                return 0
    return 1
        
for T in range(int(input())):
    arr = [list(map(int, input().split())) for _ in range(9)]
    print(f"#{T+1} {sudoku(arr)}")