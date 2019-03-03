import sys
sys.stdin = open('Input/input4874.txt', 'r')

"""
5. Stack 2

4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth



"""

def calc(op, a, b):
    if op == "+":
        return a+b
    if op == "*":
        return a*b
    if op == "-":
        return a-b
    if op == "/":
        return a//b

def forth(s):
    stack = [0] * len(s)
    top = -1

    for x in s:
        if x == ".":
            if top != 0:
                return "error"
            return stack[top]
        if x.isdigit():
            top += 1
            stack[top] = int(x)
        else:
            if top < 1: # less than 2 numbers in stack => can't compute
                return "error"
            b = stack[top]
            top -= 1
            a = stack[top]
            stack[top] = calc(x, a, b)


for T in range(int(input())):
    s = input().split()

    print(f"#{T+1} {forth(s)}")