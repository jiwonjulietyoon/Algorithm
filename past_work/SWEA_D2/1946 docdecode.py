# 1946. 간단한 압축 풀기

# for T in range(int(input())):
#     doc = {}
#     N = int(input())
#     for _ in N:
#         k, v = input().split()
#         v = int(v)
#         doc[k] = v
#     print(f"#{T+1}")
#     for k in doc:
#         for


for T in range(int(input())):
    N = int(input())
    print(f"#{T+1}")
    cnt = 0
    for _ in range(N):
        ch, n = input().split()
        n = int(n)
        for _ in range(n):
            print(ch, end='')
            cnt += 1
            if not cnt%10:
                print()
    print()







for T in range(int(input())):
    doc = []
    N = int(input())
    for _ in range(N):
        ch, n = input().split()
        n = int(n)
        doc.extend([ch] * n)
    print(f"#{T+1}")
    cnt = 0
    for x in doc:
        print(x, end='')
        cnt += 1
        if not cnt % 10:
            print()
    print()

