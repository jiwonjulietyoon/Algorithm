import sys
sys.stdin = open('Input/14500_1.txt', 'r')

""" 테트로미노

"""

def cyan1():
    global Max
    for i in range(N):
        for j in range(M-3):
            Sum = sum(arr[i][j:j+4])
            if Sum > Max:
                Max = Sum

def cyan2():
    global Max
    for j in range(M):
        for i in range(N-3):
            Sum = 0
            for k in range(4):
                Sum += arr[i+k][j]
            if Sum > Max:
                Max = Sum

def yellow():
    global Max
    for i in range(N-1):
        for j in range(M-1):
            Sum = sum(arr[i][j:j+2]) + sum(arr[i+1][j:j+2])
            if Sum > Max:
                Max = Sum

def

N, M = map(int, input().split())
arr = [0]*N
for i in range(N):
    arr[i] = list(map(int, input().split()))

Max = 0

# cyan1()
# cyan2()
yellow()

print(Max)





