"""
비밀번호 P : 000 ~ 999

K부터 1씩 증가


"""


#P, K = int(input().split()[0]), int(input().split()[1])
#P, K = map(int, input().split())
P, K = [int(x) for x in input().split()]
print(P - K + 1)