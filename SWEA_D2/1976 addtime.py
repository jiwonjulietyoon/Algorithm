# 1976. 시각 덧셈

# 시 분 으로 이루어진 시각 2개를 입력 받아, 시는 시끼리 더하고 분은 분끼리 더하여 출력


T = int(input())
for t in range(1, T+1):
    time = list(map(int, input().split()))
    hour = time[0] + time[2]
    minute = time[1] + time[3]
    if hour > 12:
        hour -= 12
    if minute > 59:
        hour += 1
        minute -= 60
    print(f"#{t} {hour} {minute}")