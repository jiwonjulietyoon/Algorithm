#   6190 정곤이의 단조 증가하는 수



################## 5th try ##############################

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





## sb else's answer #################################

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
 
    ans = -1
    for i in range(N):
        for j in range(i + 1, N):
            num = data[i] * data[j]
            if ans >= num:
                continue
            b = num % 10
            val = num//10
            ok = True
            while val:
                a = val % 10
                if a > b:
                    ok = False
                    break
                val = val//10
                b = a
            if ok:
                ans = max(ans, num)
 
    print("#{} {}".format(test_case, ans))





############### 4th try ###########################
# 39/50

def isMonInc(n):
    nstr = str(n)
    for i in range(len(nstr)-1):
        if nstr[i] > nstr[i+1]:
            return False
    return True

for T in range(int(input())):
    _, num = input(), list(map(int, input().split()))
    num = sorted(list(set(num)))
    N = len(num)
    ans = -1
    for i in range(N-2, -1, -1):
        for j in range(N-1, i, -1):
            if isMonInc(num[i]*num[j]):
                ans = num[i]*num[j]
                break
        if ans != -1:
            break
    print(f"#{T+1} {ans}")







############### 2nd-3rd try ###########################
# following code only works if given list of numbers are unique
# 40/50

def isMonInc(n): # Monotonic Increase
    nstr = str(n)
    for i in range(len(nstr)-1):
        if nstr[i] > nstr[i+1]:
            return False
    return True

for T in range(int(input())):
    N, num = int(input()), sorted(list(map(int, input().split())))
    ans = -1 # default value
    for i in range(N-2, -1, -1):
        for j in range(N-1, i, -1):
            if isMonInc(num[i]*num[j]):
                ans = num[i]*num[j]
                break
        if ans != -1:
            break
    print(f"#{T+1} {ans}")




############### 1st try ###########################
# runtime error


def isMonInc(n): # Monotonic Increase
    nstr = str(n)
    for i in range(len(nstr)-1):
        if nstr[i] > nstr[i+1]:
            return False
    return True

for T in range(int(input())):
    N, num = int(input()), list(map(int, input().split()))
    products = []
    for i in range(N):
        for j in range(i+1, N):
            if isMonInc(num[i]*num[j]):
                products.append(num[i]*num[j])
    print(f"#{T+1} {max(products)}")