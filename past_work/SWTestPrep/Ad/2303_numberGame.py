

import sys
sys.stdin = open('../Input/2303.txt', 'r')

def findMax(num):  # num: list of 5 integers








N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]

res = [0]*N
for i in range(N):
    # nums[i] => res[N-1-i]





