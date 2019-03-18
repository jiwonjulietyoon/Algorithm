# 4843. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬


for T in range(int(input())):    # test case
    N = int(input())             # number of unordered integers
    arr = list(map(int, input().split()))
    new_arr = []         # sorted list of integers
    for i in range(10):     # sort 10 times
        if i%2:   # i is odd => Find min
            Min = 101
            for x in arr:
                if x < Min:
                    Min = x
            new_arr.append(Min)
            arr.remove(Min)
        else:    # i is even => Find max
            Max = 0
            for x in arr:
                if x > Max:
                    Max = x
            new_arr.append(Max)
            arr.remove(Max)
    print(f"#{T+1} {' '.join(map(str, new_arr))}")












for T in range(int(input())):    # test case
    N = int(input())             # number of unordered integers
    nums = list(map(int, input().split()))
    minl = maxl = i
    for i in range(10):     # sort 10 times
        if i%2 == 0:
            for j in range(i + 1, N):
                if nums[maxl] < nums[j]:
                    maxl = j
            nums[i], nums[maxl] = nums[maxl], nums[i]
        else:
            for j in range(i + 1, N):
                if nums[minl] > nums[j]:
                    minl = j
            nums[i], nums[minl] = nums[minl], nums[i]

    print(f"#{T+1} {' '.join(map(str, nums))}") # check that this works