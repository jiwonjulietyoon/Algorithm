# 5986. 새샘이와 세 소수



############ 3rd try ######################

def isPrime(n):
    sqrt = int(n**0.5)
    for x in range(2, sqrt+1):
        if n % x == 0:
            return False
    return True
pn = [2]
for i in range(3, 996, 2):
    if isPrime(i):
        pn.append(i)

for T in range(int(input())):
    N = int(input())
    cnt = 0
    for i in range(len(pn)):
        if pn[i] > N - 4:
            break
        for j in range(i, len(pn)):
            if pn[i] + pn[j] > N - 2:
                break
            for k in range(j, len(pn)):
                if pn[i] + pn[j] + pn[k] == N:
                    cnt += 1
                    break
    print(f"#{T+1} {cnt}")






############ sb else's solution ###################

T = int(input())
sosu = []
num_list = [x for x in range(1000)]
for x in range(2,32):
    if num_list[x]:
        for i in range(2 , 500):
            temp = x*i
            if temp>999: break
            num_list[temp]=0
for i in range(2,1000):
    if num_list[i]: sosu.append(i)
 
for test_case in range(1, T + 1):
    n= int(input())
    out=0
    for a in sosu:
        if a+4>n:break
        for b in sosu:
            if a+b+2>n:break
            if b>a:break
            for c in sosu:
                if c>b:break
                if a+b+c==n:
                    out+=1
                    break
     
    print(f"#{test_case} {out}")






########## 2nd try


def isPrime(n):
    sqrt = int(n**0.5)
    for x in range(2, sqrt+1):
        if n % x == 0:
            return False
    return True

pn = [2]
for i in range(3, 996, 2):
    if isPrime(i):
        pn.append(i)         # list of prime numbers created


for T in range(int(input())):
    N = int(input())       # 7 <= N <= 999
    cnt = 0
    
    if N / 3 in pn:
        cnt += 1
    
    for i in range(len(pn)):
        for j in range(i+1, len(pn)):
            if 2*pn[i]+pn[j] == N:
                cnt += 1
            if 2*pn[j]+pn[i] == N:
                cnt += 1
    
    for i in range(len(pn)):
        for j in range(i+1, len(pn)):
            for k in range(j+1, len(pn)):
                if pn[i] + pn[j] + pn[k] == N:
                    cnt += 1
    print(f"#{T+1} {cnt}")


#############################################################
########## 1st try : 3,504 ms / 58,332kb / 482 / PASS


def isPrime(n):
    sqrt = int(n**0.5)
    for x in range(2, sqrt+1):
        if n % x == 0:
            return False
    return True

pn = [2]
for i in range(3, 996, 2):
    if isPrime(i):
        pn.append(i)         # list of prime numbers created


for T in range(int(input())):
    N = int(input())       # 7 <= N <= 999
    cnt = 0
    for i in range(len(pn)):
        for j in range(i, len(pn)):
            for k in range(j, len(pn)):
                if pn[i] + pn[j] + pn[k] == N:
                    cnt += 1
    print(f"#{T+1} {cnt}")




