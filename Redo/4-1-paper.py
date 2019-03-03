""" 4. Stack1 
4869. [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기

"""

fac = [1, 1, 2] + [0] * 30 # memoization: record calculated factorial values

def factorial(n):
    global fac
    if fac[n]:
        return fac[n]
    fac[n] = n * factorial(n-1)
    return fac[n]

def combination(n, r): # nCr
    return factorial(n) // (factorial(r) * factorial(n-r))

for T in range(int(input())):
    N = int(input()) // 10

    ans = 0
    Q = N // 2
    for i in range(Q+1): # i, j : number of 2's and 1's, respectively
        j = N - (2*i)
        ans += (2**i) * combination(i+j, i)

    print(f"#{T+1} {ans}")
