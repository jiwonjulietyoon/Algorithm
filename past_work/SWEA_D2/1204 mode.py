# 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기


# someone else's solution
for t in range(int(input())):
    n, r = int(input()), {}
    for s in input().split():
        r[s] = r[s] + 1 if r.get(s) is not None else 1
    print(f'#{n} {max(sorted(r.items(),reverse=True), key=lambda x: x[1])[0]}')




# my solution
for _ in range(int(input())):
    T = int(input()) # test case
    raw = list(map(int, input().split())) # raw data
    s = list(set(raw)) # duplicates removed
    s.sort(reverse=True)
    cnt = [raw.count(x) for x in s]
    maxidx = cnt.index(max(cnt))
    mode = s[maxidx]
    print(f"#{T} {mode}")