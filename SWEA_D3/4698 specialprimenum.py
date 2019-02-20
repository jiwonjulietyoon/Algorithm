# 4698. 테네스의 특별한 소수

# after referring to sb else's solution:
pn = []
num = [0, 0] + [1] * 999999
for i in range(2,1000001):
    if num[i]:
        pn.append(i)
        for j in range(i*2,1000001,i):
            num[j] = 0

for T in range(int(input())):
    D, A, B = input().split()
    A, B = int(A), int(B)
    cnt = 0
    for i in pn:
        if i < A:
            continue
        if i > B:
            break
        if D in str(i):
            cnt += 1
    print(f"#{T+1} {cnt}")
















###############################




def isPrime(n):
    sqrt = int(n**0.5)
    for x in range(2, sqrt+1):
        if n % x == 0:
            return False
    return True

pn = [2]


for T in range(int(input())):
    D, A, B = input().split()
    A, B = int(A), int(B)
    cnt = 0
    for x in pn:
        if x >= A and D in str(x):
            cnt += 1
        if x > B:
            break
    print(f"#{T+1} {cnt}")





