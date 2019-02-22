# 3408. 세가지 합 구하기


### PASS
for T in range(int(input())):
    N = int(input())
    S1 = (N+1) * (N//2)
    if N % 2:
        S1 += N//2 + 1
    print(f"#{T+1} {S1} {2*S1-N} {2*S1}")




##########################################

for T in range(int(input())):
    N = int(input())
    S1 = int((N+1) * (N/2))
    print(f"#{T+1} {S1} {2*S1-N} {2*S1}")

######################################################
### sb else's code : 시간이 훨씬 더 적게 소요

t = int(input())
s1,s2,s3 = [],[],[]
for T in range(t):
    n = int(input())
    ss1 = (n+1) * (n//2)
    if n % 2:
        ss1 += n//2 + 1
    s1.append(ss1); s2.append(ss1*2-n); s3.append(ss1*2)
for i in range(t):
    print(f"#{i+1} {s1[i]} {s2[i]} {s3[i]}")









##################################################################


for T in range(int(input())):
    N = int(input())
    S1 = int((N+1) * (N/2))
    S2 = int((2*N) * (N/2))   
    print(f"#{T+1} {S1} {S2} {2*S1}")