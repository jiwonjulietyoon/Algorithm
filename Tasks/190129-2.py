# 4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문


# 라이브러리/내장함수 사용
for T in range(int(input())):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(input())
    arr_t = list(zip(*arr))
    for y in range(N):
        for x in range(N-M+1):
            if arr[y][x:x+M] == arr[y][x:x+M][::-1]:
                ans = arr[y][x:x+M]
                break
            if arr_t[y][x:x+M] == arr_t[y][x:x+M][::-1]:
                ans = "".join(arr_t[y][x:x+M])
                break
    print(f"#{T+1} {ans}")





# 라이브러리/내장함수 미사용
# built-in functions used: range, len, int

def isPal(word):
    l = len(word)
    for i in range(int(l/2)):
        if word[i] != word[l-i-1]:
            return False
    return True

def arrTranspose(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(0, i):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    return arr

for T in range(int(input())):
    N, M = map(int, input().split())
    arr = [0]*N
    for i in range(N):
        arr[i] = [0]*N       # blank arr
    for i in range(N):
        tmp = input()
        for j in range(N):
            arr[i][j] = tmp[j]    # complete arr created
    
    ans = ''
    for y in range(N):
        for x in range(N-M+1):
            if isPal(arr[y][x:x+M]):
                ans = arr[y][x:x+M]
                break
    if ans == '':
        arr = arrTranspose(arr)
        for y in range(N):
            for x in range(N-M+1):
                if isPal(arr[y][x:x+M]):
                    ans = arr[y][x:x+M]
                    break
    print(f"#{T+1} {''.join(ans)}")