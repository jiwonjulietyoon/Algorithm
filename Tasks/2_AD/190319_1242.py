# 1242. [S/W 문제해결 응용] 1일차 - 암호코드 스캔
"""
0. (after converting into binary character format)
- 7k (binary) characters => 1 number
- 8 numbers => 1 code
- at least 1 code per test case; print all valid codes


1. read through arr (row by row) until reaching a non zero character (start from the end of the row)
-
- add the consecutive hex code strip to empty array called 'hexa'
  (only for unvisited columns)

2. Convert each strip in 'hexa' into binary format
- e.g) b += bin(int(x, 16))[2:].zfill(4)

3. for each element in 'hexa':
- variable 'ratio' -> number of characters that each number consists of
                      ( how many multiples of 7 )
- check each binary strip from the end (since all numbers end with a '1')
- upon encountering a '1', check if the last bit of the substrip matches one of the patterns
    - length of sub-strip must be 7k; start with k as 1 and then k++
    - when sub-strip matches a pattern, update 'ratio' as 7*k
- finish converting rest of the strip (7*k*7 binary characters) and retrieve all 8 numbers
- check if the 8 numbers make up a valid code. If valid, append to array 'ans'

4. print
- if ans, print(f"#{T+1}", end=" "); print(*ans)
- if not ans, print(f"#{T+1} 0")

0001110110110001011101101100010110001000110100100110111011 00

"""



import sys
sys.stdin = open('../Input/1242.txt', 'r')
# sys.stdin = open('../Input/1242-2.txt', 'r')


def find_ver(i, j):  # find vertical dimension of each code block encountered
    global arr, N
    for p in range(i, N):
        if arr[p][j] == '0':
            return i, p-1
    return i, p

def check_ver_up(i, j):  # check vertical dimension of any code column, upwards
    global arr
    for m in range(i-1, -1, -1):
        if arr[m][j] == '0':
            return m+1
    return 0

def check_ver_down(i, j):  # check vertical dimension of any code column, downwards
    global arr, N
    for m in range(i+1, N):
        if arr[m][j] == '0':
            return m-1
    return m

hex_to_bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

def patt(r):
    ratio = [
        '0'*(3*r) + '1'*(2*r) + '0'*r + '1'*r,
        '0'*(2*r) + '1'*(2*r) + '0'*(2*r) + '1'*r,
        '0'*(2*r) + '1'*(1*r) + '0'*(2*r) + '1'*(2*r),
        '0'*(1*r) + '1'*(4*r) + '0'*(1*r) + '1'*(1*r),
        '0'*(1*r) + '1'*(1*r) + '0'*(3*r) + '1'*(2*r),
        '0'*(1*r) + '1'*(2*r) + '0'*(3*r) + '1'*(1*r),
        '0'*(1*r) + '1'*(1*r) + '0'*(1*r) + '1'*(4*r),
        '0'*(1*r) + '1'*(3*r) + '0'*(1*r) + '1'*(2*r),
        '0'*(1*r) + '1'*(2*r) + '0'*(1*r) + '1'*(3*r),
        '0'*(3*r) + '1'*(1*r) + '0'*(1*r) + '1'*(2*r)
    ]
    return ratio

def pattern(sub, r):
    if sub[0] != '0':
        return 0
    if sub in patt(r//7):
        return 1

for T in range(int(input())):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    vis = [[0] * M for _ in range(N)]  # visited
    hexa = []   # record all hex strips

    for i in range(N):
        for j in range(M-1, -1, -1):  # traverse left
            if arr[i][j] != '0' and not vis[i][j]:
                h1, h2 = find_ver(i, j)
                w1, w2 = 0, j   # start, end col idx of code block
                z = 0
                for q in range(j, -1, -1):  # continue to traverse left to detect beginning of code block
                    if arr[i][q] != '0' and z:
                        if vis[i][q] or (h1, h2) != (check_ver_up(i, q), check_ver_down(i, q)):  # diff code block encountered
                            w1 = q+1  # col start idx of code block
                            break
                    if arr[i][q] == '0':
                        z = 1
                    else:
                        z = 0
                # move right again to find real w1
                for w in range(w1, w2):
                    if arr[i][w] != '0':
                        w1 = w
                        break
                # after finding exact dimensions of the current code block (rows: h1~h2 / cols: w1~w2):
                #   - mark entire block as visited
                #   - append code strip to 'hexa'
                for ii in range(h1, h2+1):  # mark as visited
                    for jj in range(w1, w2+1):
                        vis[ii][jj] = 1
                hexa.append(arr[h1][w1:w2+1])  # record code strip

    ### finished finding all code strips at this point

    # convert code strip into binary format
    binary = []
    for strip in hexa:
        tmp = ''
        for x in strip:
            tmp += hex_to_bin[x]
        binary.append(tmp)

    ans = []
    for x in binary:
        strip = x.rstrip('0')
        ratio = 7
        while 1:  # find ratio
            if pattern(strip[len(strip)-ratio:], ratio):  # if this matches one of the 10 patterns
                break
            else:
                ratio += 7
        if len(strip) > (8*ratio):
            diff = len(strip) - (8*ratio)
            strip = strip[diff:]
        elif len(strip) < (8*ratio):
            diff = (8*ratio) - len(strip)
            strip = '0'*diff + strip

        code = []
        r_patt = patt(ratio//7)
        for i in range(0, 8*ratio, ratio):
            code.append(r_patt.index(strip[i:i+ratio]))

        odd = sum(code[0:7:2]) * 3
        even = sum(code[1:7:2])
        if (odd + even + code[-1]) % 10 == 0:
            ans.append(sum(code))

    if ans:
        print(f"#{T+1} {sum(ans)}")
    else:
        print(f"#{T+1} 0")


