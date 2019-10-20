# 10개 수 입력 받아서 홀수만 더한 값을 출력


T = int(input())
for i in range(1, T + 1):
    num = map(int, input().split())
    sum_odd = sum([x for x in num if x % 2 == 1])
    print(f"#{i} {sum_odd}")
