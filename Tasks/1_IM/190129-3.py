# 4865. [파이썬 S/W 문제해결 기본] 3일차 - 글자수

# 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 그중 가장 많은 글자의 개수를 출력하는 프로그램을 만드시오.





# 라이브러리/내장함수 사용
for T in range(int(input())):
    str1, str2 = input(), input()
    cnt = []
    for x in set(str1):
        cnt.append(str2.count(x))
    print(f"#{T+1} {max(cnt)}")




# 라이브러리/내장함수 미사용
for T in range(int(input())):
    str1, str2 = input(), input()
    str1_l = len(str1)
    cnt = [0] * str1_l
    for x in range(str1_l):
        for y in str2:
            if str1[x] == y:
                cnt[x] += 1
    Max = cnt[0]
    for i in range(1, str1_l):
        if cnt[i] > Max:
            Max = cnt[i]
    print(f"#{T+1} {Max}")
