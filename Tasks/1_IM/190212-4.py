# 4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기





# 2nd try
# stack 활용하기
# if two consecutive identical letters are stacked, delete both from stack


def removeDup(s):
    stack = [0] * len(s)
    top = -1
    for x in s:
        if top == -1:
            top += 1
            stack[top] = x
        else:
            if x == stack[top]:
                top -= 1
            else:
                top += 1
                stack[top] = x
    return stack[:top+1]


for T in range(int(input())):
    print(f"#{T+1} {len(removeDup(input()))}")









################################################################
# 1st try

def removeDup(s):
    c = 0
    s_list = list(s)
    if len(s) == 1:
        return s_list
    else:
        while(1):
            if s_list[c] == s_list[c+1]:
                s_list[c:c+2] = []
                c = 0
            else:
                c += 1
            if c == len(s_list) - 1:
                return s_list

for T in range(int(input())):
    s = input()
    new = removeDup(s)
    print(f"#{T+1} {len(new)}")


# 3
# ABCCB
# NNNASBBSNV
# UKJWHGGHNFTCRRCTWLALX