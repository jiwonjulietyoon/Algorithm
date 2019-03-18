# 6190. 정곤이의 단조 증가하는 수

def isMonInc(n):
    tmp, b = n // 10, n % 10
    a = tmp % 10
    while tmp:
        if a > b:
            return False
        tmp = tmp // 10
        b = a
        a = tmp % 10
    return True

for T in range(int(input())):
    N, nums = int(input()), list(map(int, input().split()))
    ans = -1
    for i in range(N-2, -1, -1):
        for j in range(N-1, i, -1):
            num = nums[i]*nums[j]
            if num <= ans:
                continue
            if isMonInc(num):
                ans = num
    print(f"#{T+1} {ans}")