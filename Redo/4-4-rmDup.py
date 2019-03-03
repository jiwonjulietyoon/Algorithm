"""
4. Stack1

4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기



"""

for T in range(int(input())):
    s = input()
    stack = []

    for x in s:
        if not stack:
            stack.append(x)
        elif stack[-1] == x:
            stack.pop()
        else:
            stack.append(x)

    print(f"#{T+1} {len(stack)}")
