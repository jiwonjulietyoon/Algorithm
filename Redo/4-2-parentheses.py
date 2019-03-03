"""
4. Stack1

4866. [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사

"""

def check(s):
    p = {'(': ')', ')': '(', '{': '}', '}': '{'} # list of parentheses
    stack = []
    for x in s:
        if x in p:
            if x == '(' or x == '{':
                stack.append(x)
            else:
                if not stack: # if stack is empty
                    return 0
                if stack.pop() != p[x]: # parentheses don't match
                    return 0
    if stack: # if stack is not empty
        return 0
    return 1


for T in range(int(input())):
    print(f"#{T+1} {check(input())}")