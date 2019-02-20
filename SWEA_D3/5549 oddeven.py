# 5549 odd or even?

for T in range(int(input())):
    N = input()
    print(f"#{T+1} Odd") if int(N[-1]) % 2 else print(f"#{T+1} Even")