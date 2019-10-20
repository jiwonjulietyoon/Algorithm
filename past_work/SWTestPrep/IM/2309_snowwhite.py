# 일곱 난쟁이
"""
Sum of 7 must equal 100

diff = (sum of all 9 numbers) - 100

find two numbers that sum up to 'diff'

"""


import sys
sys.stdin = open('../Input/2309.txt', 'r')

h = [int(input()) for _ in range(9)]
diff = sum(h) - 100

tmp = 0
for i in range(1, 9):
    for j in range(i):
        if h[i]+h[j] == diff:
            m, n = h[i], h[j]
            tmp = 1
            break
    if tmp:
        break

h.remove(m)
h.remove(n)

print(*sorted(h), sep="\n")


