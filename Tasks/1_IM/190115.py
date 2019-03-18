# 1208 - Flatten, Dump

## 1st try
for T in range(10):
    N = int(input())
    cols = list(map(int, input().split()))
    for _ in range(N):
        for x in range(len(cols)):
            if cols[x] == max(cols):
                maxidx = x
            if cols[x] == min(cols):
                minidx = x
        cols[maxidx] -= 1
        cols[minidx] += 1
    diff = max(cols) - min(cols)
    print(f"#{T+1} {diff}")



## 2nd try
for T in range(10):
    N = int(input())
    cols = sorted(list(map(int, input().split())))
    for _ in range(N):
        cols[0] += 1
        cols[-1] -= 1
        cols = sorted(cols)
    diff = max(cols) - min(cols)
    print(f"#{T+1} {diff}")

