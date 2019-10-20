# 1948. 날짜 계산기

end = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def getDays(m, d):  # month, date
    days = sum(end[:m-1]) + d
    return days     # total days from Jan 1

for T in range(int(input())):
    m1, d1, m2, d2 = map(int, input().split())
    ans = getDays(m2, d2) - getDays(m1, d1) + 1
    print(f"#{T+1} {ans}")