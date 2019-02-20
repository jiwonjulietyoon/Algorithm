# 4834. [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드



# 2차 시도
T = int(input())
for t in range(T):
    N = int(input())
    num = list(input())
    num.sort(reverse=True)
    cnt = [num.count(x) for x in num]
    maxfreq = max(cnt)
    maxfreqnum = num[cnt.index(max(cnt))]
    print(f"#{t+1} {maxfreqnum} {maxfreq}")




# 강사님 답안:

N = int(input())
cards = input()
cnt = [0] * 10
for i in range(N):
    cnt[int(cards[i])] += 1
maxl = 0
for i in range(10):
    if cnt[maxl] <= cnt[i]:
        maxl = i











# 통과는 되었으나 정확하지 않은 코드:
T = int(input())
for t in range(T):
    N = int(input())
    num = list(input())
    cnt = [num.count(x) for x in set(num)]
    if len(set(cnt)) == 1:
        freqnum = max(num)
        freqmax = num.count(freqnum)
    else:
        freqmax = 0
        for x in set(num):
            if num.count(x) > freqmax:
                freqmax = num.count(x)
                freqnum = x
    print(f"#{t+1} {freqnum} {freqmax}")
        