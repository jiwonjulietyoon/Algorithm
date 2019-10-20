# 1984. 중간 평균값 구하기

# centered average : average excluding max and min

T = int(input())
for t in range(1, T+1):
    num = list(map(int, input().split()))
    num.remove(max(num))
    num.remove(min(num))
    print(f"#{t} {round(sum(num) / len(num))}")

