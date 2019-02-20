# 4864. [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교



# 라이브러리/내장함수 사용
for T in range(int(input())):  # T = test case
    str1, str2, ans = input(), input(), 0
    if str1 in str2:
        ans = 1
    print(f"#{T+1} {ans}")





# 라이브러리/내장함수 미사용
# Brute Force Method2
# built-in functions used: len, range, int
for T in range(int(input())):  # T = test case
    str1, str2 = input(), input()
    len1, len2 = len(str1), len(str2)
    ans = 0
    for i in range(len2-len1+1):
        for j in range(len1):
            if str1[j] != str2[i+j]:
                break
            if j == len1-1:
                ans = 1
        if ans == 1:
            break
    print(f"#{T+1} {ans}")






# 라이브러리/내장함수 미사용
# Brute Force Method
# built-in functions used: len, range, int
for T in range(int(input())):  # T = test case
    str1, str2 = input(), input()
    len1, len2 = len(str1), len(str2)
    ans = 0
    for i in range(len2-len1+1):
        cnt = 0
        for j in range(len1):
            if str1[j] == str2[i+j]:
                cnt += 1
        if cnt == len1:
            ans = 1
            break
    print(f"#{T+1} {ans}")