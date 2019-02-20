# 2005 Pascal's Triangle

T = int(input())
for i in range(1, T+1):
    N = int(input())
    line = [1] + [0]*9
    print(f"#{i}")
    for x in range(N):
        print(" ".join(n for n in map(str, line) if n != '0'))
        newline = line[:]
        for y in range(1, 10):
            newline[y] = line[y-1] + line[y]
        line = newline[:]





