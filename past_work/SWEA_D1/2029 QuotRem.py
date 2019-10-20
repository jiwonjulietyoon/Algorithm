# Quotient and Remainder


T = int(input())
for i in range(1, T + 1):
    a, b = map(int, input().split())
    q = a // b
    r = a % b
    print(f"#{i} {q} {r}")


