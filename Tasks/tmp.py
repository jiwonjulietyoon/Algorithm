

a = [1, 2, 3, 4, 5]

print(*a, sep="\n")




# tmp = {}
# for num in range(10):
#     tmp[str(num)] = (bin(int(str(num), 16))[2:].zfill(4))
# for alpha in ['A', 'B', 'C', 'D', 'E', 'F']:
#     tmp[alpha] = (bin(int(alpha, 16))[2:].zfill(4))
#
# print(tmp)


# import sys
# sys.stdin = open('Input/tmp.txt', 'r')
#
#
# for T in range(int(input())):
#     b, c = input(), input()
#     lb, lc = len(b), len(c)
#     db, dc = int(b, 2), int(c, 3)
#
#     found = 0
#     for i in range(lb):
#         if b[i] == '1':
#             tb = db - 2**(lb-1-i)
#         else:
#             tb = db + 2**(lb-1-i)
#         for j in range(lc):
#             if c[j] == '0':
#                 tc1 = dc + 3**(lc-1-j)  # change to 1
#                 tc2 = dc + 2*(3**(lc-1-j))  # change to 2
#             elif c[j] == '1':
#                 tc1 = dc - 3**(lc-1-j)  # change to 0
#                 tc2 = dc + 3**(lc-1-j)  # change to 2
#             else:  # 2
#                 tc1 = dc - 2*(3**(lc-1-j))   # change to 0
#                 tc2 = dc - 3**(lc-1-j)  # change to 1
#             if tb == tc1 or tb == tc2:
#                 ans, found = tb, 1
#                 break
#         if found:
#             break
#
#     print(ans)
#









# def opp(n):
#     return '0' if n == '1' else '1'
#
# def opp3(c, j, p, q): # p, q: whatever is not c[j]
#
#
# for T in range(int(input())):
#     b, c = input(), input()  # 2진수, 3진수
#     print(f"[2진수]: {b} // [3진수]: {c}")
#
#     tmp = 0
#     for i in range(len(b)):
#         b2 = b[:i] + opp(b[i])
#         if i < len(b)-1:
#             b2 += b[i+1:]
#         b3 = int(b2, 2)
#         for j in range(len(c)):
#             if c[j] == '0':
#
#             elif c[j] == '1':
#
#
#             else:  # 2:
#
#
#
#             c2 = c[:j] + opp(c[j])
#             if j < len(c)-1:
#                 c2 += c[j+1:]
#             print(f"2진수: {b2}->{b3} // 3진수: {c2}->{int(c2, 3)}")
#     print("=====")
