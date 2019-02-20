###  1220. [S/W 문제해결 기본] 5일차 - Magnetic

"""
EXAMPLE:

---------------------------------------
<Initial State>

N 극: attracts '2'

i 0 1 2 3 4 5 6
| 1   2   1   1 |
|   2           |
|     1     1   |
|         1 2 2 |
|           1   |
|     2 1   2 1 |
|     1 2 2   2 |

S 극: attracts '1'


----------------------------------------
<Step 1>

[1] : delete if there are no "2"s below
[2] : delete if there are no "1"s above

N 극: attracts '2'

i 0 1 2 3 4 5 6
|         1   1 |
|               |
|     1     1   |
|         1 2 2 |
|           1   |
|     2 1   2 1 |
|       2 2   2 |

S 극: attracts '1'


------------------------------------------
<Step 2>

Go through each column.
Collect 1's and 2's only (Ignore 0's)
Upon encountering a '1'+'2' or '2'+'1' pair, cnt += 1
=================================================




N 극: attracts '2'

i 0 1 2 3 4 5 6
| 1   2   1   1 |
|   2           |
|     1     1   |
|         1 2 2 |
|           1   |
|     2 1   2 1 |
|     1 2 2   2 |

S 극: attracts '1'


"""

############# 강사님 답안 ############ 

for T in range(10):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    cnt = 0
    
    for i in range(N): # move through each column
        flag = 0
        for j in range(N): # move through each row (down)
            if arr[j][i] == "1":
                flag = 1
            elif arr[j][i] == "2" and flag == 1:
                cnt += 1
                flag = 0
    print(f"#{T+1} {cnt}")




################# 2nd  try ############################

for T in range(10):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    cnt = 0
    
    for i in range(N): # move through each column
        stack = [0] * N
        top = 0
        for j in range(N): # move through each row (down)
            if arr[j][i] == "1" or arr[j][i] == "2":   # ignore all 0's
                stack[top] = arr[j][i]
                top += 1
        for k in range(N):
            if stack[k] == 0:
                break
            if stack[k] == "1" and stack[k+1] == "2":
                cnt += 1
    print(f"#{T+1} {cnt}")







################# 1st  try ############################

for T in range(10):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    cnt = 0
    
    for i in range(N): # move through each column
        string = ""
        for j in range(N): # move through each row (down)
            if arr[j][i] == "1" or arr[j][i] == "2":   # ignore all 0's
                string += arr[j][i]
        cnt += string.count("12")
    print(f"#{T+1} {cnt}")



















############## doesn't work

## only count "1"+"2" pairs

for T in range(10):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    cnt = 0
    
    for i in range(N): # move through each column
        stack = [0] * 100
        top = -1
        for j in range(N): # move through each row (down)
            if arr[j][i] == "1" or arr[j][i] == "2":   # ignore all 0's
                if top == 0 and arr[j][i] == "2" and stack[top] == "1":
                    cnt += 1
                    top = -1
                elif arr[j][i] == "1":
                    top += 1
                    stack[top] = arr[j][i]
    print(f"#{T+1} {cnt}")


####################################################

