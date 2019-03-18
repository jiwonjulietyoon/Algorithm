# 4869. [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기


# memoization: 
# - keep track of already calculated factorial values 
# - so as to avoid redundant calculations 
#  (especially considering that factorials are recursive)

fac = {}

def factorial(n):
    if n == 0:
        return 1
    if fac.get(n):
        return fac[n]
    fac[n] = n * factorial(n-1)
    return fac[n]

def combination(n, r):
    return int(factorial(n) / (factorial(r) * factorial(n-r)))

for T in range(int(input())):
    N = int(input()) // 10
    ans = 0
    for i in range(N//2 + 1):
        j = N - 2 * i
        ans += (2**i) * combination(i+j, i)
    print(f"#{T+1} {ans}")






######################### 1st try


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def combination(n, r):
    return int(factorial(n) / (factorial(r) * factorial(n-r)))

for T in range(int(input())):
    N = int(input()) // 10
    ans = 0
    for i in range(N//2 + 1):
        j = N - 2 * i
        ans += (2**i) * combination(i+j, i)
    print(f"#{T+1} {ans}")