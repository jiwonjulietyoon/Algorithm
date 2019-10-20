# 10개 수 입력 받아 평균값을 출력하기. 소수점 첫 째 자리에서 반올림한 정수 출력.

T = int(input())
for i in range(1, T + 1):
    avg = round(sum(map(int, input().split())) / 10)
    print(f"#{i} {avg}")