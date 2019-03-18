# 2005. 파스칼의 삼각형

for T in range(int(input())):
    N = int(input())
    pascal = [ [1]+[0]*(N-1) for _ in range(N) ]

    print("#{}".format(T + 1))
    print(1)

    for i in range(1, N):
        print(1, end=" ")
        for j in range(1, i+1):
            pascal[i][j] = pascal[i-1][j-1]+pascal[i-1][j]
            print(pascal[i][j], end=" ")
        print()

