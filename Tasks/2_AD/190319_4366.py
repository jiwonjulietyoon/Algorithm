""" 4366. 정식이의 은행업무



"""

import sys
sys.stdin = open('../Input/4366.txt', 'r')


for T in range(int(input())):
    b, c = input(), input()
    lb, lc = len(b), len(c)
    db, dc = int(b, 2), int(c, 3)

    found = 0
    for i in range(lb):
        if b[i] == '1':
            tb = db - 2**(lb-1-i)
        else:
            tb = db + 2**(lb-1-i)
        for j in range(lc):
            if c[j] == '0':
                tc1 = dc + 3**(lc-1-j)  # change to 1
                tc2 = dc + 2*(3**(lc-1-j))  # change to 2
            elif c[j] == '1':
                tc1 = dc - 3**(lc-1-j)  # change to 0
                tc2 = dc + 3**(lc-1-j)  # change to 2
            else:  # 2
                tc1 = dc - 2*(3**(lc-1-j))   # change to 0
                tc2 = dc - 3**(lc-1-j)  # change to 1
            if tb == tc1 or tb == tc2:
                ans, found = tb, 1
                break
        if found:
            break

    print(f"#{T+1} {ans}")


