# 1224. [S/W 문제해결 기본] 6일차 - 계산기3


def calc(a, b, op):
    return a + b if op == "+" else a * b

for T in range(10):
    N, exp = int(input()), input()
    post = [0] * N
    stack = [0] * N
    p = s = -1

    for x in exp:
        if x.isdigit():
            p += 1
            post[p] = x
        elif x == "(" or x == "*":
            s += 1
            stack[s] = x
        elif x == ")":
            while(1):
                if stack[s] == "(":
                    s -= 1
                    break
                else:
                    p += 1
                    post[p] = stack[s]
                    s -= 1
        elif x == "+":
            while(1):
                if stack[s] == "(":
                    s += 1
                    stack[s] = x
                    break
                else:
                    p += 1
                    post[p] = stack[s]
                    s -= 1

    s = -1
    for x in post:
        if x == 0:
            break
        if x.isdigit():
            s += 1
            stack[s] = int(x)
        else:
            b = stack[s]
            s -= 1
            a = stack[s]
            stack[s] = calc(a, b, x)

    print(f"#{T+1} {stack[s]}")