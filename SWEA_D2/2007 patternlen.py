# 2007 Finding the length of a pattern in each string



N = int(input())
for i in range(1, N+1):
    s = input()
    x = 1
    while True:
        if s[:x] == s[x:2*x] and s[:x] == s[2*x:3*x]:
            break
        x += 1
    print(f"#{i} {x}")