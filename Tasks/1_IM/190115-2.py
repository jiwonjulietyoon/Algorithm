# 4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스
# 최소 충전 횟수는?


T = int(input())    # 노선 개수
for t in range(T):
    K, N, M = map(int, input().split())
        # K: 충전 이후 최대 이동 정류장
        # N: 정류장 종점 번호
        # M: 충전기 설치된 정류장 개수
    st = list(map(int, input().split())) # 충전기 설치된 정류장 번호
    pos = 0 # current bus position (정류장 번호)
    cnt = 0 # 충전한 횟수
    while True:
        n = [a for a in st if a > pos and a - pos <= K]
        if len(n) == 0:
            cnt = 0
            break
        elif len(n) > 0:
            cnt += 1
            pos = max(n)    # -> pos = n[-1] 로 연산 개수 줄이기
            if N - pos <= K:
                break
    print(f"#{t+1} {cnt}")



