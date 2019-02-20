# 4866. [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사

def check(s):
    p = {'{': '}', '}': '{', '(': ')', ')': '('}
    stack = [0] * len(s)
    top = -1
    for x in s:
        if x == '{' or x == '(':
            top += 1
            stack[top] = x
        elif x == '}' or x == ')':
            d = stack[top]
            top -= 1
            if top == -2 or p[d] != x:
                return 0
    if top != -1:
        return 0
    return 1

for T in range(int(input())):
    print(f"#{T+1} {check(input())}")

