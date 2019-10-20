# YYYYMMDD 형태로 8자리의 날짜가 주어진다.
# 날짜의 유효성을 판단하여,
# 유효하다면 YYYY/MM/DD 로 출력.
# 유효하지 않다면 -1 출력.

T = int(input())
end = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
for i in range(1, T + 1):
    date = input()
    y, m, d = map(int, [date[:4], date[4:6], date[-2:]])
    if m < 1 or m > 12:
        res = -1
    elif d < 1 or d > end[m]:
        res = -1
    else:
        res = f"{y:0>4}/{m:0>2}/{d:0>2}"
    print(f"#{i} {res}")