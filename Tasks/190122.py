# 1259. [S/W 문제해결 응용] 7일차 - 금속막대

for T in range(int(input())):   # test case
    n = int(input())
    data = list(map(int, input().split()))
    arr = list(zip(data[::2], data[1::2]))
    new_arr = [arr[0]]
    arr.pop(0)
    x = 0
    while len(arr) > 0:
        if arr[x][1] == new_arr[0][0]:
            new_arr.insert(0, arr[x])
            arr.pop(x)
            x = 0
            continue
        elif arr[x][0] == new_arr[-1][1]:
            new_arr.append(arr[x])
            arr.pop(x)
            x = 0
            continue
        x += 1
    ans = []
    for x in new_arr:
        for y in x:
            ans.append(str(y))
    print(f"#{T+1} {' '.join(ans)}")

