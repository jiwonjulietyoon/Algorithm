# 5948. 새샘이의 7-3-5 게임

for T in range(int(input())):
    nums = list(map(int, input().split()))
    sums = []
    for i in range(7):
        for j in range(i+1, 7):
            for k in range(j+1, 7):
                Sum = nums[i] + nums[j] + nums[k]
                if Sum not in sums:
                    sums.append(Sum)
    sums.sort(reverse=True)
    print(f"#{T+1} {sums[4]}")