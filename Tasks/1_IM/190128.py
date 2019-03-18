# range, len, chr, ord 만 사용 가능

# ZRO, ONE, TWO, THR, FOR, FIV, SIX, SVN, EGT, NIN



for T in range(int(input())):
    _ = input()
    arr = input().split()
    cnt = [0] * 10
    num = ['ZRO ', 'ONE ', 'TWO ', 'THR ', 'FOR ', 'FIV ', 'SIX ', 'SVN ', 'EGT ', 'NIN ']
    for x in arr:
        for y in range(len(num)):
            if x == num[y][:-1]:
                cnt[y] += 1
    print(f"#{T+1}")
    for x in range(len(num)):
        print(num[x] * cnt[x], end='')
    print()




# using dictionary
for T in range(int(input())):
    _, N = input().split()
    arr = input().split()
    num = {'ZRO ': 0, 'ONE ': 0, 'TWO ': 0, 'THR ': 0, 'FOR ': 0, 'FIV ': 0, 'SIX ': 0, 'SVN ': 0, 'EGT ': 0, 'NIN ': 0}
    for x in arr:
        num[x+" "] += 1
    print(f"#{T+1}")
    for k, v in num.items():
        print(k*v, end="")
    print()
    

