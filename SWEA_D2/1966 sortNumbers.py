# 1966. 숫자를 정렬하자

for T in range(int(input())):
    N = int(input())
    num = list(map(int, input().split()))
    new_list = []
    while len(num) > 0:
        Min = num[0]
        for i in range(1, len(num)):
            if num[i] < Min:
                Min = num[i]
        new_list.append(Min)
        num.remove(Min)
    print(f"#{T+1} {' '.join(map(str, new_list))}")