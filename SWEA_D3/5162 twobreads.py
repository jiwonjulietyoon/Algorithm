# 5162. 두가지 빵의 딜레마



for T in range(int(input())):
    A, B, C = map(int, input().split())
    ans = int(C/A) if A <= B else int(C/B)
    print(f"#{T+1} {ans}")