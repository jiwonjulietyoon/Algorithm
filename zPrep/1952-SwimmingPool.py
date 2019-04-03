import sys
sys.stdin = open('Input/1952.txt', 'r')

"""
1952. [모의 SW 역량테스트] 수영장


"""

def cost(i, Sum):
    global Min
    if Sum > Min:
        return
    if i > e:
        if Sum < Min:
            Min = Sum
    else:
        cost(i+3, Sum+c)
        if M[i] >= days:
            cost(i+1, Sum+b)
        else:
            cost(i+1, Sum+M[i]*a)

for T in range(1, int(input())+1):
    a, b, c, d = map(int, input().split())  # 1 Day, 1 Month, 3 Months, 1 Year
    M = list(map(int, input().split()))
    for s in range(12):  # s: start idx
        if M[s]:
            break
    for e in range(11, -1, -1):  # e: end idx
        if M[e]:
            break
    Min = d   # Year Pass
    days = b//a + 1  # minimum days for a monthly pass to become cheaper than multiple daily passes
    cost(s, 0)

    print(f"#{T} {Min}")







###################################################
# 49 out of 50 correct

# def cost(i, Sum):
#     global Min
#     if Sum > Min:
#         return
#     if i > e:
#         if Sum < Min:
#             Min = Sum
#     else:
#         if e-i+1 >= 3:
#             cost(i+3, Sum+c)
#             if M[i] >= days:
#                 cost(i+1, Sum+b)
#             else:
#                 cost(i+1, Sum+M[i]*a)
#         else:
#             if M[i] >= days:
#                 cost(i+1, Sum+b)
#             else:
#                 cost(i+1, Sum+M[i]*a)
#
# for T in range(1, int(input())+1):
#     a, b, c, d = map(int, input().split())  # 1 Day, 1 Month, 3 Months, 1 Year
#     M = list(map(int, input().split()))
#     for s in range(12):  # s: start idx
#         if M[s]:
#             break
#     for e in range(11, -1, -1):  # e: end idx
#         if M[e]:
#             break
#     Min = d   # Year Pass
#     days = b//a + 1  # minimum days for a monthly pass to become cheaper than multiple daily passes
#     cost(s, 0)
#
#     print(f"#{T} {Min}")

