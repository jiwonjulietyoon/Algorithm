# 1959. 두 개의 배열

def getSOP(s, l):   # shorter list, longer list
    SOP = []
    for i in range(len(l)-len(s)+1):
        tmp = 0
        for j in range(len(s)):
            tmp += s[j]*l[j+i]
        SOP.append(tmp)
    return max(SOP)

for T in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if len(A) >= len(B):
        res = getSOP(B, A)
    else:
        res = getSOP(A, B)
    print(f"#{T+1} {res}")