# 1232. [S/W 문제해결 기본] 9일차 - 사칙연산
import sys
sys.stdin = open('../Input/input1232.txt', 'r')

def calc(op, a, b):
    if op == "+":
        return a+b
    if op == "-":
        return a-b
    if op == "*":
        return a*b
    if op == "/":
        return a/b

for T in range(1, 11):
    N = int(input())
    nodes = [input().split() for _ in range(N)]
    tree = [[0, 0] for _ in range(N+1)]
    exp = [None] * (N+1)  # values -- numbers and operators

    for x in nodes:
        if x[1].isdigit():
            exp[int(x[0])] = int(x[1])
        else:  # operator
            exp[int(x[0])] = x[1]
            tree[int(x[0])][0], tree[int(x[0])][1] = int(x[2]), int(x[3])

    for i in range(N, 0, -1):
        if exp[i] in ["+", "-", "*", "/"]: # if an operator
            exp[i] = calc(exp[i], exp[tree[i][0]], exp[tree[i][1]])

    print("#{} {}".format(T, int(exp[1])))