# 4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth
# 후위표기법

def calc(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a // b

for T in range(int(input())):
    exp = input().split()
    stack = [0] * len(exp)
    top = -1
    for x in exp:
        if x.isdigit():
            top += 1
            stack[top] = int(x)
        elif x == ".":
            if top != 0:
                ans = "error"
                break
            ans = stack[top]
        else:
            b = stack[top]
            top -= 1
            a = stack[top]
            stack[top] = calc(a, b, x)
    print(f"#{T+1} {ans}")

