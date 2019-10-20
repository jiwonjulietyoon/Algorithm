# 10개 수 입력받아 가장 큰 수 출력

T = int(input())
for i in range(1, T + 1):
    max_num = max(map(int, input().split()))
    print(f"#{i} {max_num}")