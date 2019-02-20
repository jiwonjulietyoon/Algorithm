N = int(input())
for i in range(1, N+1):
    if {int(x) for x in str(i)}.intersection({3, 6, 9}):
        cnt = 0
        for y in [int(x) for x in str(i)]:
            if y in [3, 6, 9]:
                cnt += 1
        print("-"*cnt, end=" ")
    else:
        print(i, end=" ")


