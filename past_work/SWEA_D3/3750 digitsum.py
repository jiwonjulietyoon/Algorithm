








######################### incomplete

# (N-1) % 9 , and then +1




def digitsum(N):
    

for T in range(int(input())):
    num = list(map(int, list(input())))

    print(f"#{T+1} {ans}")








##############################################################
# 시간 초과 3

def digitsum(n): 
    Sum = 0 
    while(n > 0 or Sum > 9): 
        if n == 0: 
            n = Sum
            Sum = 0
        Sum += n % 10
        n //= 10
    return Sum

for T in range(int(input())):
    print(f"#{T+1} {digitsum(int(input()))}")





###########################################################
# 시간 초과 2

def digitsum(n):
    return sum(list(n))

for T in range(int(input())):
    N = input()
    while len(N) > 1:
        N = digitsum(N)
    print(f"#{T+1} {N}")


###########################################################
# 시간 초과


def digitsum(n):
    Sum = 0
    while n:
        Sum += n % 10
        n //= 10
    return Sum

for T in range(int(input())):
    N = int(input())
    while N > 9:
        N = digitsum(N)
    print(f"#{T+1} {N}")