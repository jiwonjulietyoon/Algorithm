# 2개 수를 입력받아 크기를 비교하여 등호/부등호 출력하기



T = int(input())
for i in range(1, T + 1):
    a, b = map(int, input().split())
    if a > b:
        res = ">"
    elif a == b:
        res = "="
    elif a < b:
        res = "<"
    print(f"#{i} {res}")