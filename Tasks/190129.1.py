# 1216. [S/W 문제해결 기본] 3일차 - 회문2

import sys
sys.stdin = open('input.txt', 'r')



def isPalindrome(word):
    l = len(word)
    for i in range(int(l/2)):
        if word[i] != word[l-i-1]:
            return False
    return True

for _ in range(10):
    T = input()
    arr = [0] * 100
    for x in range(100):
        arr[x] = input()      # arr created

    M = 2

    for i in range(100):
        j = 0
        tmp = 100
        col = [arr[idx][i] for idx in range(100)]
        while(1):
            for j in range(101-tmp):
                if isPalindrome(arr[i][j:j+tmp]) or isPalindrome(col[j:j+tmp]):
                    M = tmp
                    break
            if tmp == M:
                break
            tmp -= 1

    print(f"#{T} {M}")


















##############################################################





def isPalindrome(word):
    l = len(word)
    for i in range(int(l/2)):
        if word[i] != word[l-i-1]:
            return False
    return True

def arrTranspose(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(0, i):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    return arr

for _ in range(10):
    T = input()
    arr = [0] * 100
    for x in range(100):
        arr[x] = list(input())       # arr created

    M = 2

    for i in range(100):
        j = 0
        tmp = 100
        while(1):
            for j in range(100-tmp+1):
                if isPalindrome(arr[i][j:j+tmp]):
                    M = tmp
                    break
            tmp -= 1
            if tmp + 1 == M:
                break

    arr = arrTranspose(arr)

    for i in range(100):
        j = 0
        tmp = 100
        while(1):
            for j in range(100-tmp+1):
                if isPalindrome(arr[i][j:j+tmp]):
                    M = tmp
                    break
            tmp -= 1
            if tmp + 1 == M:
                break

    print(f"#{T} {M}")





























#############################################################################


def isPalindrome(word):
    l = len(word)
    for i in range(int(l/2)):
        if word[i] != word[l-i-1]:
            return False
    return True

for _ in range(10):
    T = input()
    arr = []
    for _ in range(100):
        arr.append(input())
    arr_t = list(zip(*arr))

    M = 2  # maximum count record: length of the longest palindrome encountered

    for i in range(100):  # go through each row
        j = 0
        while (1):
            tmp = M + 1
            if j + tmp > 100:
                break
            while (1):
                if isPalindrome(arr[i][j:j + tmp]):
                    M = tmp
                    j = 0
                    break
                tmp += 1
                if tmp == 101 - j:
                    j += 1
                    break

    for i in range(100):  # go through each col
        j = 0
        while (1):
            tmp = M + 1
            if j + tmp > 100:
                break
            while (1):
                if isPalindrome(arr_t[i][j:j + tmp]):
                    M = tmp
                    j = 0
                    break
                tmp += 1
                if tmp == 101 - j:
                    j += 1
                    break

    print(f"#{T} {M}")